## Quickstart Directory API

This quickstart can be used as template. It has calls for insert/delete groups or members

## Requirements

- Activate Admin SDK API in the Google Cloud Platform console

- In GCP console, API & Services > Credentials, create a OAuth 2.0 Client IDs and select Desktop app as application type.

- Generate a json of this client id, name it `key.json` and add it to config/credentials/)

- (Requires Google Workspace admin account) Go to admin.google.com. Go to Security > API controls > Manage Domain Wide Delegation. Add a new API clients with your previously created Oauth Client Id as the Client ID, and the scopes (https://www.googleapis.com/auth/admin.directory.user and https://www.googleapis.com/auth/admin.directory.group) in OAuth scopes.

- Python3 (https://www.python.org/downloads/windows/)

- Python virtualenv and pip installed

## Setup

```bash
# Create virtualenv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install requirements
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

## Main

```bash
# Execute examples in main
python main.py
```

Warning: It might be possible that calling insert/delete groups or members returns a 403 Not authorized, depending on your Google Workspace policies. Even the Google Workspace admin account might not be authorized to use these methods.

## Documentation

Link to the official Lumapps API documentation: https://developers.google.com/admin-sdk/directory/reference/rest
