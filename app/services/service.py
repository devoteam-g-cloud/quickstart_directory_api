import os

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from config import (
    SERVICE_ACCOUNT_KEY_FILE,
    SCOPES
)


class Service:
    """Service builder"""

    def __init__(self, service_name, version):
        self.service_name = service_name
        self.version = version
        self.credentials = None
        
        if os.path.exists('token.json'):
            self.credentials = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    SERVICE_ACCOUNT_KEY_FILE, SCOPES)
                self.credentials = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(self.credentials.to_json())
        
        self.service = self.build(self.service_name, self.version)

    def build(self, service, version):
        """build the service from name, version and credentials"""
        return build(
            service, 
            version, 
            credentials=self.credentials
        )
