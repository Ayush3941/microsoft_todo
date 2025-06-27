# Privacy Policy for Microsoft Todo Dify Plugin

This Privacy Policy explains how the **Microsoft Todo Plugin** ("the Plugin") collects, uses, and handles your information when used within the Dify platform.

## 1. Information We Handle

### a. **Microsoft Account Access Token**

To use the Plugin, you are required to provide an access token obtained via Microsoft OAuth. This credential is securely stored by the Dify platform in accordance with its security protocols. The Plugin uses it solely to authenticate requests to the Microsoft Graph API on your behalf.

### b. **Todo Task Data**

Depending on the tool function you invoke — including:

* **Create Todo** (`create-todo`)
* **Get Todos** (`get-todos`)
* **Delete Todo** (`delete-todo`)
* **Mark Todo Completed** (`mark-todo-completed`)

— the Plugin interacts with the Microsoft Graph API to fetch or manipulate your task data. This may include task titles, due dates, status, and associated metadata. The Plugin does **not** persist this data. All information is processed in-memory and returned directly to the Dify interface.

### c. **Usage Data**

General usage data (e.g., frequency of tool usage, tool invocation logs) may be collected by the Dify platform as part of its standard analytics. This is governed by Dify’s [Privacy Policy](https://dify.ai/privacy).

## 2. How We Use Your Information

* **OAuth Access Token**: Used strictly to authenticate API requests to Microsoft Graph on your behalf.
* **Task Data**: Accessed only to perform the operation you explicitly request. No task content is stored by the Plugin after processing.

## 3. Data Storage

The Plugin does not maintain its own persistent storage.

* Your Microsoft token is managed by the Dify platform in accordance with its secure handling practices.
* All task-related data is retrieved and discarded during a single processing session.

## 4. Third-Party Services

This Plugin exclusively interacts with the **Microsoft Graph API** for task management. By using the Plugin, you agree to Microsoft’s [Terms of Use](https://learn.microsoft.com/en-us/legal/microsoft-api-terms) and [Privacy Policy](https://privacy.microsoft.com/).

## 5. Your Choices

You may revoke the Plugin’s access to your Microsoft account at any time by:

* Revoking the access token in your [Microsoft Account Settings](https://account.microsoft.com/).
* Removing or reconfiguring the Plugin within your Dify application settings.

## 6. Changes to This Policy

We may update this Privacy Policy from time to time. Any changes will be reflected in the Plugin’s documentation or description. Continued use of the Plugin after updates constitutes your acceptance of the revised policy.

## 7. Contact Us

If you have questions about this privacy policy, please contact the plugin author: \[Ayush3941 / microsoft\_todo]
