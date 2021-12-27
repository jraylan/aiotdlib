# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class EditChatInviteLink(BaseObject):
    """
    Edits a non-primary invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param invite_link: Invite link to be edited
    :type invite_link: :class:`str`
    
    :param name: Invite link name; 0-32 characters, defaults to None
    :type name: :class:`str`, optional
    
    :param expiration_date: Point in time (Unix timestamp) when the link will expire; pass 0 if never
    :type expiration_date: :class:`int`
    
    :param member_limit: The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited
    :type member_limit: :class:`int`
    
    :param creates_join_request: True, if the link only creates join request. If true, member_limit must not be specified
    :type creates_join_request: :class:`bool`
    
    """

    ID: str = Field("editChatInviteLink", alias="@type")
    chat_id: int
    invite_link: str
    name: typing.Optional[str] = Field(None, max_length=32)
    expiration_date: int
    member_limit: int
    creates_join_request: bool

    @staticmethod
    def read(q: dict) -> EditChatInviteLink:
        return EditChatInviteLink.construct(**q)
