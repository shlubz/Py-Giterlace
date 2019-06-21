# Py-Giterlace
Documentation is WIP (Work-In-Progress)

[![License](https://img.shields.io/badge/license-LGPL-blue.svg)](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)

Py-Giterlace (Name still pending) is a Python 3 cli-based application used to combine methos in creating, deleting and listing repositoires from APICentric
git hosting platforms that are supported.

With a goal in mind to interlace several of these git platform's commonly used functionalities to run at the same time, such as uploading or deleting repositories
through single line command arguments.

Currently supported or being worked on:

[GitHub API v3]: https://developer.github.com/v3
[GitLab API v4]: https://docs.gitlab.com/ee/api/README.html

**IMPORTANT**
GitLab features are currently being worked on. Some of the features may not work right or way or haven't been fully bug scrubbed.

Using the application features allows you to currently manage both [GitHub] and [GitLab] resources, currently only supporting interaction with repositories
such as listing, creating or deleting respositories.

## Installation

git clone https://github.com/shlubz/Py-Giterlace.git

## How To Use
An account on either GitHub or GitLab (depending on which is used) is required before interacting with a majority of APIs that are offered by GitHub and GitLab.

Currently, Py-Giterlace supports token and username/password based authentication on GitHub and GitLab only supported for token-based.

## Pesonal Access Token Method
Create a personal access token on either github or gitlab. Documentation can be found at the following links.

[GitHub]: https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
[GitLab]: https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html

Py-Giterlace supports three methods of inputting authentication information and will try to automate a majority of the process.

### Configuration File
The configuration file 'config.py' is python dictionary that can be used to add username/password/token data and also supports
using environmental variable calling os.environ.get('variable_name') from within the file.
Add video


### Environemental Variables
If the configuration file isn't used, the application will search the local environmental variables set as the user.
The default names can be changed but it is recommended not to unless going through all the code to replace the searching strings.

Username: 'github_username' or 'gitlab_username'
Token:    'github_token' or 'gitlab_token
Password: 'github_password' or 'gitlab_password'

## Manual Input
If both the configuration file isn't used and no environmental variables are used, the program will prompt the user with manually entering the authentication data.

### Demo GitHub - WIP
Add video

### Demo GitLab - WIP
Add video

## Documentation - WIP

## Development - WIP

### Contributing - WIP
