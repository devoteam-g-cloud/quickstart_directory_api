from app.services.directory_api import DirectoryService


def main():
    directory_service = DirectoryService()

    ## Examples
    directory_service.list_users()

    directory_service.list_groups()

    # Insert group
    # group_email = 'new_group@test.com'
    # name = 'New group name'
    # description = 'New group description'
    # directory_service.insert_group(group_email, name, description)
    
    # Insert member in group
    # member_email = 'member@test.com'
    # directory_service.insert_member(group_email, member_email)

if __name__ == '__main__':
    main()
