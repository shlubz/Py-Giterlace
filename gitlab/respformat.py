def response_loop(response_dicts, option):
    """Loops through a given dictionary and one layer of nested dictionaries.

    Loop path is dependent on the option passed as argument using if/elif.
    Recursive function with option-based pathing would better approach.
    """

    # Matching strings for response output, can be modified
    str_match_repo_resp = []
    print()

    def create_repo_loop():
        """Loop for formatting response data output for repo creation."""

        # If option is create_repo
        for key1, val1 in response_dicts.items():
            if isinstance(val1, dict):
                for key2, val2 in val1.items():
                     print(f'{key2}: {val2}')
            else:
                print(f'{key1}: {val1}')
        print()

    def list_groups_loop():
        """Loop for formatting response data output for groups"""

        for list_item in response_dicts:
            if isinstance(list_item, dict):
                for key, val in list_item.items():
                    if key == 'name':
                        print(f'{key}: {val}')
        print()

    def list_repo_owned_loop():
        """Loop for formatting response data output in listing repos."""

        for i in response_dicts:
            for key, val in i.items():
                if isinstance(val, dict):
                    for key2, val2 in val.items():
                        print(f'{key2}: {val2}')
                else:
                    print(f'{key}: {val}')
        print()

    def list_repo_groups_loop():
        """Loop for formatting response data output in listing repos of a
        partciular group.
        """
        for key1, val1 in response_dicts.items():
            if isinstance(val1, dict):
                for key2, val2 in val1.items():
                    print(f'{key2}: {val2}')
            else:
                print(f'{key1}: {val1}')
        print()

    # Option determines which loop function to call
    if option == 1:
        create_repo_loop()
    elif option == 3:
        list_groups_loop()
    elif option == 4:
        list_repo_owned_loop()
    elif option == 5:
        list_repo_groups_loop()
    else:
        pass
