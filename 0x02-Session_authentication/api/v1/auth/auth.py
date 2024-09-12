#!/usr/bin/env python3
"""
Definition of class Auth
"""
from flask import request
from typing import (
    List,
    TypeVar
)


from os import getenv  # import getenv to get environment variable


class Auth:
    """
    Manages the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication or not
        Args:
            - path(str): Url path to be checked
            - excluded_paths(List of str): List of paths that do not require
              authentication
        Return:
            - True if path is not in excluded_paths, else False
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for i in excluded_paths:
                if i.startswith(path):
                    return False
                if path.startswith(i):
                    return False
                if i[-1] == "*":
                    if path.startswith(i[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from a request object
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """
        Returns a User instance from information from a request object
        """
        return None

    def session_cookie(self, request=None):
        """
        Returns the value of the cookie named _my_session_id from the request.
        The cookie name is defined by the environment variable SESSION_NAME.

        Args:
            request: The Flask request object

        Returns:
            The value of the session cookie if it exists, otherwise None.
        """
        if request is None:
            return None

        # Get the session cookie name from environment variable
        session_name = getenv("SESSION_NAME", "_my_session_id")

        # Return the value of the cookie from the request
        return request.cookies.get(session_name)
