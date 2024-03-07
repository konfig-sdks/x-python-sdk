# coding: utf-8

"""
    Twitter API v2

    Twitter API v2 available endpoints

    The version of the OpenAPI document: 2.62
    Created by: https://developer.twitter.com/
"""

from x_python_sdk.paths._2_lists_id_members.post import AddMember
from x_python_sdk.paths._2_lists.post import CreateNewList
from x_python_sdk.paths._2_lists_id.delete import DeleteOwnedList
from x_python_sdk.paths._2_users_id_followed_lists.post import FollowList
from x_python_sdk.paths._2_users_id_followed_lists.get import GetFollowed
from x_python_sdk.paths._2_users_id_list_memberships.get import GetUserMemberships
from x_python_sdk.paths._2_users_id_owned_lists.get import GetUserOwnedLists
from x_python_sdk.paths._2_users_id_pinned_lists.get import GetUserPinnedLists
from x_python_sdk.paths._2_lists_id.get import LookupByListId
from x_python_sdk.paths._2_users_id_pinned_lists.post import PinList
from x_python_sdk.paths._2_lists_id_members_user_id.delete import RemoveMember
from x_python_sdk.paths._2_users_id_followed_lists_list_id.delete import UnfollowList
from x_python_sdk.paths._2_users_id_pinned_lists_list_id.delete import UnpinList
from x_python_sdk.paths._2_lists_id.put import UpdateOwnedList
from x_python_sdk.apis.tags.lists_api_raw import ListsApiRaw


class ListsApi(
    AddMember,
    CreateNewList,
    DeleteOwnedList,
    FollowList,
    GetFollowed,
    GetUserMemberships,
    GetUserOwnedLists,
    GetUserPinnedLists,
    LookupByListId,
    PinList,
    RemoveMember,
    UnfollowList,
    UnpinList,
    UpdateOwnedList,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ListsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ListsApiRaw(api_client)
