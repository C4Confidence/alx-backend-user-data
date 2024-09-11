#!/usr/bin/env python3
"""
Definition of class SessionAuth
"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    Manages session authentication
    """
    #  Class attribute to store session IDs and their user IDs
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session ID for a given user_id and stores it in the dictionary
        Args:
            - user_id: The ID of the user for whom the session is being created
        Returns:
            - The generated session ID if successful, None otherwise.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        #  Generate a new Session ID using uuid4()
        session_id = str(uuid.uuid4())

        #  Store the session ID and associate it with the user_id
        self.user_id_by_session_id[session_id] = user_id

        #  Return the generated session ID
        return session_id
