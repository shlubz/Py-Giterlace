# -*- coding: utf-8 -*-
"""PyGiterlace/github/start.py

This module is the entrypoint in the program.

Current Options:
    0.) Exit Program - Exits the program
    1.) GitHub - Starts GitHub client
    2.) GitLab - Starts GitLab client
"""

import sys

from github.start import start_github
from gitlab.start import start_gitlab

from global_tools.tools import text_wrap

def exit_program():
    """Simply exits the program."""

    print('Exiting program!')
    sys.exit()


def prog_desc():
    """Just prints the program description of how it's intended to be used."""

    text = """\n\
           Py-Giterlace is a python cli-based application used to combine
           methods in creating, deleting and listing repositories from
           API-centric git hosting platforms that are supported.

           With a goal in mind to interlace several of these git platforms
           commonly used functionalities to run at the same time, such as
           uploading or deleting repositories through single line command
           arguments.

           Currently this application supports GitHub and GitLab but intends
           to eventually work with other git hosting platforms as well."""
    print(text_wrap(text))


def banner():
    """Just prints the banner for the program."""

    print()
    print('===================================================================')
    print('||                        PY-GITERLACE                           ||')
    print('===================================================================')


def main():
    """Starts chosen git API caller"""

    option = None
    while option != 0:
        banner()
        prog_desc()
        text = """\n\
               To get started, please select one of the following options to use:
               0. Exit Program
               1. GitHub
               2. GitLab\n"""

        print(text_wrap(text))

        try:
            option = int(input('Option: '))

            # Check if invalid option was selected
            if option not in range(0, 2):
                raise ValueError

        except ValueError:
            print('\nInvalid selection in response, please try again.')

        else:
            # Get response based on option selected
            if option == 0:
                exit_program()

            elif option == 1:
                start_github()

            elif option == 2:
                start_gitlab()


if __name__ == '__main__':
    main()
