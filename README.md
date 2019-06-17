# PyGitWeave
Documentation is WIP (Work-In-Progress)
[![License](https://img.shields.io/badge/license-LGPL-blue.svg)](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)

PyGitWeave is a Python 3 application that supports and encapsulates any supported git repository hosting provider's APIs into a single package.

Currently supported or being worked on:

[GitHub API v3]: https://developer.github.com/v3
[GitLab API v4]: https://docs.gitlab.com/ee/api/README.html

**IMPORTANT**
GitLab features are currently being worked on.

Using the application features allows you to currently manage both [GitHub] and [GitLab] resources, currently only supporting interaction with repositories.

## Installation

```bash
$ pip install PyGitWeave
```

## How To Use
An account on either GitHub or GitLab (depending on which is used) is required before interacting with a majority of APIs that are offered by GitHub and GitLab.

Currently, PyGitWeave supports token and username/password based authentication on GitHub and GitLab only supported for token-based.
1
## Pesonal Access Token Method
Create a personal access token on either github or gitlab. Documentation can be found at the following links.

[GitHub]: https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
[GitLab]: https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html

Preferably use environmental variables to keep information input more secure but manual input is supported:

Token: 'GITHUB_TOKEN' or 'GITLAB_TOKEN:

### Demo GitHub - WIP
'''bash
$ python3 main.py
'''

### Demo GitLab - WIP
'''bash
$ python3 main.py
'''

## Username/Password Method
Again, preferably use with environmental variables with manual input supported:

Username: 'GITHUB_USERNAME' or 'GITLAB_USERNAME'

Password: 'GITHUB_PASSWORD'

## Documentation - WIP

## Development - WIP

### Contributing - WIP
