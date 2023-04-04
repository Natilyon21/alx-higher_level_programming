#!/usr/bin/python3
"""it defines a locked class."""


class LockedClass:
    """
    This prevent the user from instantiating new LockedClass
    """

    __slots__ = ["first_name"]
