import requests


class MicrosoftTodoApiException(Exception):
    def __init__(self, message: str, code: int = None):
        self.message = message
        self.code = code
        super().__init__(message)

    def __str__(self):
        if self.code:
            return f"[Error {self.code}] {self.message}"
        return self.message


BASE_URL = "https://graph.microsoft.com/v1.0/me/todo/lists"


def _headers(access_token: str) -> dict:
    return {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }


def get_default_task_list_id(access_token: str) -> str:
    try:
        response = requests.get(BASE_URL, headers=_headers(access_token))
        response.raise_for_status()
        data = response.json()
        return data["value"][0]["id"]  # Assuming default = first list
    except requests.RequestException as e:
        raise MicrosoftTodoApiException("Failed to get default task list.", code=response.status_code)


def create_todo(access_token: str, title: str, due_date: str = None) -> dict:
    try:
        task_list_id = get_default_task_list_id(access_token)
        payload = {
            "title": title
        }
        if due_date:
            payload["dueDateTime"] = {
                "dateTime": due_date,
                "timeZone": "UTC"
            }

        response = requests.post(
            f"{BASE_URL}/{task_list_id}/tasks",
            headers=_headers(access_token),
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise MicrosoftTodoApiException("Failed to create todo.", code=response.status_code)


def get_todos(access_token: str, include_completed: str = "false") -> list[dict]:
    """
    include_completed options:
    - "false": only active tasks
    - "true": all tasks
    - "only": only completed tasks
    """
    try:
        task_list_id = get_default_task_list_id(access_token)

        if include_completed == "only":
            filter_query = "?$filter=status eq 'completed'"
        elif include_completed == "false":
            filter_query = "?$filter=status ne 'completed'"
        else:
            filter_query = ""  # include all

        response = requests.get(
            f"{BASE_URL}/{task_list_id}/tasks{filter_query}",
            headers=_headers(access_token)
        )
        response.raise_for_status()
        return response.json()["value"]
    except requests.RequestException as e:
        raise MicrosoftTodoApiException("Failed to fetch todos.", code=response.status_code)



def delete_todo(access_token: str, task_id: str) -> bool:
    try:
        task_list_id = get_default_task_list_id(access_token)
        response = requests.delete(
            f"{BASE_URL}/{task_list_id}/tasks/{task_id}",
            headers=_headers(access_token)
        )
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        raise MicrosoftTodoApiException("Failed to delete todo.", code=response.status_code)


def mark_todo_completed(access_token: str, task_id: str) -> dict:
    try:
        task_list_id = get_default_task_list_id(access_token)
        payload = {
            "status": "completed"
        }
        response = requests.patch(
            f"{BASE_URL}/{task_list_id}/tasks/{task_id}",
            headers=_headers(access_token),
            json=payload
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise MicrosoftTodoApiException("Failed to mark todo as completed.", code=response.status_code)
