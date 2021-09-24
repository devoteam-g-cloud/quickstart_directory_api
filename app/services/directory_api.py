"""
Iam Client

https://cloud.google.com/iam/docs/reference/rest/v1/projects.roles
"""

import logging

from googleapiclient.errors import HttpError
from app.services.service import Service
from config import DIRECTORY_SERVICE_NAME, DIRECTORY_API_VERSION


class DirectoryService(Service):
    """Directory Service"""

    def __init__(self):
        Service.__init__(self, DIRECTORY_SERVICE_NAME, DIRECTORY_API_VERSION)

    def list_users(self, maxResults=5):
        try:
            results = self.service.users().list(
                customer='my_customer', 
                maxResults=maxResults,
                orderBy='email'
            ).execute()
            users = results.get('users', [])

            if not users:
                print(f'No users in domain')
            else:
                print(f'Users:')
                for user in users:
                    print(f"{user['primaryEmail']} ({user['name']['fullName']})")
        except Exception as err:
            print(f'Error listing users: {err}')

    def list_groups(self, maxResults=5):
        try:
            results = self.service.groups().list(
                customer='my_customer', 
                maxResults=maxResults,
                orderBy='email'
            ).execute()
            groups = results.get('groups', [])

            if not groups:
                print(f'No groups in domain')
            else:
                print(f'Groups:')
                for group in groups:
                    print(f"{group['email']} ({group['name']})")
        except Exception as err:
            print(f'Error listing groups: {err}')

    def insert_group(self, email, name, description):
        try:
            group = {
                'email': email,
                'name': name,
                'description': description
            }
            self.service.groups().insert(body=group).execute()
            logging.info(f'Group {email} has been created')
        except Exception as err:
            logging.error(f'Error inserting group {email}: {err}')
        
    def delete_group(self, email):
        try:
            self.service.groups().delete(groupKey=email).execute()
            logging.info(f'Deleted group {email}')
        except HttpError as err:
            if err.resp.status == 404:
                logging.info(f'Group {email} not found')
            else:
                logging.info(f'Error deleting group {email}: {err}')

    def insert_member(self, group_email, member_email):
        try:
            member = {'email': member_email}
            self.service.members().insert(
                groupKey=group_email,
                body=member
            ).execute()
            logging.info(f'Added member {member_email} to group {group_email}')
        except HttpError as err:
            if err.resp.status == 404:
                logging.warning(f'Group {group_email} not found')
            elif err.resp.status == 409:
                logging.info(f'Member {member_email} already in group {group_email}')
            else:
                logging.info(f'Error inserting member {member_email} in group {group_email}: {err}')
        
    def delete_member(self, group_email, member_email):
        try:
            self.service.members().delete(
                groupKey=group_email,
                memberKey=member_email
            ).execute()
            logging.info(f'Deleted member {member_email} in group {group_email}')
        except HttpError as err:
            if err.resp.status == 404:
                logging.info(f'Member {member_email} not found in group {group_email}')
            else:
                logging.info(f'Error deleting member {member_email} in group {group_email}: {err}')
