# -*- coding: utf-8 -*-
"""Py-Giterlace/global_tools/tools.py

This module is used to store tools that require repetitive use throughout the
entire application.
"""

import textwrap

def does_pass(var, reqs):
    """Simply checks if variable is not equal to requirements."""

    # Check if variable is not requirements
    if var is reqs:
        raise_pass = False
    else:
        raise_pass = True

    return raise_pass


def text_wrap(text):
    """Returns dedented text with variable in text string."""

    text = textwrap.dedent(text)
    return text


def raise_value(var, reqs):
    """Checks if variable is in requirements and raises a value error if value
    doesn't exist.
    """

    try:
        # Check if variable passed is in requirements
        if var in reqs:
            raise_pass = True
        else:
            raise ValueError

    except ValueError:
        print(f'\nInvalid selection in response, please try again.')
        raise_pass = False

    return raise_pass
