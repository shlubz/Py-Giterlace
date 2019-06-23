# -*- coding: utf-8 -*-
"""Py-Giterlace/github/start.py

This module is used to start the github client by passing in a
username/password or token to authenticate against GitHub API.
A session is created by instantiating an object of a GitHub client and passing
in the desired method of authentication.  This object is used in calling the
APIs from the caller.py module.
"""

import os
import getpass
import config as cfg

from github.client import GitHub
from github.caller import api_caller
from global_tools.tools import does_pass, text_wrap, raise_value


def password_or_token():
    """Loops if input is not in passing values list.
    An additional call is called to raise_value function to return a True or
    False to the passing variable.
    """

    passing_vals = ['p', 'password', 't', 'token']
    passing = False

    while not passing:
        pass_or_tok = input('\nPlease enter p for password or t for token: ')
        passing = raise_value(pass_or_tok, passing_vals)

    return passing_vals, pass_or_tok, passing


def auth_session_call(username, **kwargs):
    """Returns an authenticated session object based on given method.

    Method 1: Username & Password
    Method 2: Token

    Additionally, prints out the session info after method decision.
    """

    if 'api_token' and 'password' in kwargs != '':
        text = """\n\
                Both the API token and password were found in config file.\n
                Tokens have higher priority, using token.\n"""
        print(text_wrap(text))

    if 'api_token' in kwargs != '':
        api_token = kwargs['api_token']
        auth_session = GitHub(username, api_token=api_token)

    elif 'password' in kwargs != '':
        password = kwargs['password']
        auth_session = GitHub(username, password=password)

    auth_session.print_session()
    return auth_session


def config_file_use():
    """Checks the config file for proper usage and either returns empty
    information or returns data used in authentication session.
    """

    conf_list = ['username', 'password', 'api_token']

    # if username is nothing or username and password or token is nothing
    if cfg.github_client[conf_list[0]] == '' or\
       cfg.github_client[conf_list[0 and 1 or 2]] == '':

        text = ("""\n\
                Config file shows values that are not set!\n
                Returning to standard checks.""")
        print(text_wrap(text))

        # Set configuration values
        use_config = False
        username = ''
        password = ''
        api_token = ''
    else:
        print('\nFound config file with values set.')
        use_config = True
        username = cfg.github_client['username']
        password = cfg.github_client['password']
        api_token = cfg.github_client['api_token']

    return use_config, username, password, api_token


def session_builder(use_config, **kwargs):
    """Either uses the configuration file for the authenticated session
    otherwise attempts to find environmental variables and prompts if not
    found.
    """

    # If configuration is True, use that data for authenticated session
    if use_config:
        username = kwargs['username']
        password = kwargs['password']
        api_token = kwargs['api_token']

        if password == '':
            auth_session = auth_session_call(username, api_token=api_token)

        auth_session = auth_session_call(username, password=password)

    if not use_config:
        empty_string = ''
        env_vars = ['github_username', 'github_password', 'github_token']
        text = """\n\
               No data found in environmental or user input found for """

        raise_pass1 = False
        raise_pass2 = False
        raise_pass3 = False
        raise_all_pass = [raise_pass1, raise_pass2, raise_pass3]

        username = os.environ.get(env_vars[0])
        password = os.environ.get(env_vars[1])
        api_token = os.environ.get(env_vars[2])

        # Stop loop after all raise_passes are True
        while not all(raise_all_pass):
            raise_all_pass = [raise_pass1, raise_pass2, raise_pass3]

            # Username check loop
            while not raise_pass1:
                raise_pass1 = does_pass(username, empty_string)

                if not raise_pass1:
                    print(text_wrap(text) + env_vars[0] + '.\n')
                    username = input('Please enter your GitHub username: ')

            # Check valid password or token method of authentication loop
            while not raise_pass2:
                passing_vals, pass_or_tok, raise_pass2 = password_or_token()

            # Check for password or token option loop
            while not raise_pass3:
                # Password
                if pass_or_tok in passing_vals[0:1]:
                    raise_pass3 = does_pass(password, empty_string)

                    if not raise_pass3:
                        print(text_wrap(text) + env_vars[1] + '.\n')
                        password = getpass.getpass('Please enter your Github password: ')

                    auth_session = auth_session_call(username, password=password)

                # Token
                else:
                    raise_pass3 = does_pass(api_token, empty_string)

                    if not raise_pass3:
                        print(text_wrap(text) + env_vars[2] + '.\n')
                        api_token = getpass.getpass('Please enter your Github token: ')

                    auth_session = auth_session_call(username, api_token=api_token)

    # Returns the authenticated session to use in the api caller
    print('All conditions are satisified, building authenticated session!\n')
    return auth_session


def start_github():
    """Starts the GitHub client with an authentication session depending on
    user's choice with using a Password method or a Token-based method.
    """

    print('\nStarting GitHub client!\n')

    github_api = 'https://api.github.com'
    raise_pass = False
    passing_vals = ['t', 'true', 'f', 'false']
    username = ''
    password = ''
    api_token = ''

    # Check for proper input on using the config file
    while not raise_pass:
        use_config = input('Please enter true or false if the configuration file is used: ')
        raise_pass = raise_value(use_config.lower(), passing_vals)

        # Check if input was true or false for using the config file
        if use_config.lower() in passing_vals[0:2]:
            use_config, username, password, api_token = config_file_use()

        elif use_config.lower() in passing_vals[2:4]:
            use_config = False

    # Returns the authenticated session using password_or_token method
    auth_session = session_builder(use_config,
                                   username=username,
                                   password=password,
                                   api_token=api_token)

    # Start program with the api caller
    api_caller(github_api, auth_session)
