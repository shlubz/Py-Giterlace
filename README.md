# PyGit-HubLab
Documentation is WIP (Work-In-Progress)

PyGit-HubLab is a Python 3 application that encapsulates both GitHub's and GitLab's API functions into a single package.

[GitHub API v3]: https://developer.github.com/v3
[GitLab API v4]: https://docs.gitlab.com/ee/api/README.html

Using the application features allows you to manage both [GitHub] and [GitLab] resources, currently only supporting interaction with repositories.

## Installation

```bash
$ pip install PyGit-HubLab
```

## How To Use
An account on either GitHub or GitLab (depending on which is used) is required before interacting with a majority of APIs that are offered by GitHub and GitLab.

Currently, PyGit-HubLab supports two methods of interacting with the APIs, one being token based and the other being username/password.

## Pesonal Access Token Method
Create a personal access token on either github or gitlab. Documentation can be found at the following links.

[GitHub]: https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
[GitLab]: https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html

Preferably use environmental variables to keep information input more secure but manual input is supported:

Token: 'GITHUB_TOKEN' or 'GITLAB_TOKEN:

### Demo GitHub - WIP
'''bash
$ python3 __init__.py
'''

### Demo GitLab - WIP
'''bash
$ python3 __init__.py
'''

## Username/Password Method
Again, preferably use with environmental variables with manual input supported:

Username: 'GITHUB_USERNAME' or 'GITLAB_USERNAME'
Password: 'GITHUB_PASSWORD' or 'GITLAB_PASSWORD'

## Documentation - WIP

## Development - WIP

### Contributing - WIP
