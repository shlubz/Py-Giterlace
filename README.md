# py-giterlace
Documentation is WIP (Work-In-Progress)

[![License](https://img.shields.io/badge/license-LGPL-blue.svg)](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)

Py-Giterlace (Name still pending) is a Python 3 cli-based application used to combine methods in creating, deleting and listing repositoires from APICentric
git hosting platforms that are supported.

With a goal in mind to interlace several of these git platform's commonly used functionalities to run at the same time, such as uploading or deleting repositories
through single line command arguments.

Currently supported or being worked on:

[GitHub API v3]: https://developer.github.com/v3
[GitLab API v4]: https://docs.gitlab.com/ee/api/README.html

[GitHub API v3]

[GitLab API v4]

**IMPORTANT**
GitLab features are currently being worked on. Some of the features may not work right or way or haven't been fully bug scrubbed.

[GitHub]: https://github.com/about
[GitLab]: https://about.gitlab.com/

Using the application features allows you to currently manage both [GitHub] and [GitLab] resources, currently only supporting interaction with repositories
such as listing, creating or deleting respositories.

## Installation

git clone https://github.com/shlubz/Py-Giterlace.git

## How To Use
An account on GitHub, GitLab or both is required before interacting with a majority of APIs that are offered from these hosting platforms.

Currently, Py-Giterlace supports token and username/password based authentication on GitHub and GitLab only supports token-based.

## Pesonal Access Token
Create a personal access token on either github or gitlab. Documentation can be found at the following links.

[GitHub Personal Access Token]: https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
[GitLab Personal Access Token]: https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html

[GitHub Personal Access Token]

[GitLab Personal Access Token]

Py-Giterlace supports three methods of inputting authentication information and will try to automate a majority of the process.

### Configuration File
The configuration file 'config.py' is python dictionary that can be used to add username/password/token data and also supports
using environmental variable calling os.environ.get('variable_name') from within the file.

Add video

### Environmental Variables
If the configuration file isn't used, the application will search the local environmental variables set as the user.
The default names for these envrionmental variables can be changed but it is recommended not to unless doing a find/replace for every file that involves the app
searching these strings.  This will be a feature that may be looked into at some point.

Username: 'github_username' or 'gitlab_username'

Token:    'github_token' or 'gitlab_token'

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
