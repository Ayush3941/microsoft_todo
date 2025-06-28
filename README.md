## microsoft\_todo

## Overview

**microsoft\_todo** is a task management plugin powered by the Microsoft Graph API.
It allows users to create, fetch, delete, and complete tasks within Microsoft Todo.
Designed for developers building productivity and workflow tools, microsoft\_todo offers a one-time integration with long-term convenience for task-based apps.

## Configure

### 1. Register a Microsoft Azure App

Create an app on the [Azure Portal](https://portal.azure.com/) to obtain your client ID and configure Microsoft Graph API permissions.

![](./_assets/azure-app-registration.jpg)

### 2. Get microsoft\_todo tools from Plugin Marketplace

The microsoft\_todo tools can be found in the Plugin Marketplace. Please install the plugin first.

### 3. Fill in the configuration in Dify

---

### TO GET MICROSOFT ACCESS TOKEN

## 🔧 Setup Instructions

### 1. Register an Azure App

1. Visit the [Azure Portal](https://portal.azure.com/).
2. Register a new application.
3. Set the **Redirect URI** to:  
   `http://localhost:8000/callback`
4. Add the following **Delegated API Permissions** under Microsoft Graph:
   - `offline_access`
   - `Tasks.ReadWrite`
   - `User.Read`
   - `email`
   - `profile`
   - `openid`
5. Grant **Admin Consent** for all the above permissions.

---

### 2. Token Exchange (Access + Refresh Token)

Run a Flask server to complete OAuth2 flow and decode the token:

```bash
pip install flask requests pyjwt[crypto]
```

```python
# auth_server.py
from flask import Flask, request
import requests, jwt

CLIENT_ID = "<your-client-id>"
CLIENT_SECRET = "<your-client-secret>"
TENANT_ID = "<your-tenant-id>"
REDIRECT_URI = "http://localhost:8000/callback"
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
TOKEN_URL = f"{AUTHORITY}/oauth2/v2.0/token"

app = Flask(__name__)

@app.route("/")
def index():
    return '''
    <a href="{AUTHORITY}/oauth2/v2.0/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&response_mode=query&scope=offline_access%20Tasks.ReadWrite%20User.Read%20email%20profile%20openid">Login with Microsoft</a>
    '''

@app.route("/callback")
def callback():
    code = request.args.get("code")
    data = {
        "client_id": CLIENT_ID,
        "scope": "offline_access Tasks.ReadWrite User.Read email profile openid",
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
        "client_secret": CLIENT_SECRET
    }

    resp = requests.post(TOKEN_URL, data=data)
    token_json = resp.json()
    access_token = token_json.get("access_token")
    refresh_token = token_json.get("refresh_token")

    decoded = jwt.decode(access_token, options={"verify_signature": False})
    return f'''
    ✅ Access Token: {access_token}<br><br>
    🔁 Refresh Token: {refresh_token}<br><br>
    👤 User: {decoded.get('name')}<br>
    🔑 Scopes: {decoded.get('scp')}<br>
    '''

if __name__ == "__main__":
    app.run(port=8000)
```

---

## 🛠 Plugin Usage in Dify

1. Upload or install the plugin via Dify's Plugin Marketplace.
2. Go to:  
   `Tools > microsoft_todo > Authorize`
3. Paste your `Access Token` and you're ready to use the tool.

---

On the Dify navigation page, click `Tools > microsoft_todo > Authorize` and enter the required OAuth credentials or access token.

![](./_assets/auth.jpg)

### 4. The microsoft\_todo tool includes the following functions:

#### Create Todo

Create a new task inside your Microsoft Todo default list.

#### Get Todos

Fetch all active tasks from your Todo list.

#### Delete Todo

Delete a specific task using its unique ID.

#### Mark Todo Completed

Mark a task as completed in Microsoft Todo.

## Features

* 📝 Create tasks instantly
* 📋 Retrieve all your todos
* ❌ Delete any task
* ✅ Mark tasks as completed
* 🔒 Secure OAuth-based access

### 5. Use the tool

You can use the microsoft\_todo tool in the following application types:

![](./_assets/use-the-tool.jpg)

#### Chatflow / Workflow applications

Both Chatflow and Workflow applications support adding a microsoft\_todo tool node.

#### Agent applications

This tool is currently not supported in Agent applications.

Contact me: [https://github.com/Ayush3941/microsoft\_todo](https://github.com/Ayush3941/microsoft_todo)
@Ayush3941
