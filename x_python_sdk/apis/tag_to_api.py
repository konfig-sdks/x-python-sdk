import typing_extensions

from x_python_sdk.apis.tags import TagValues
from x_python_sdk.apis.tags.tweets_api import TweetsApi
from x_python_sdk.apis.tags.users_api import UsersApi
from x_python_sdk.apis.tags.lists_api import ListsApi
from x_python_sdk.apis.tags.compliance_api import ComplianceApi
from x_python_sdk.apis.tags.direct_messages_api import DirectMessagesApi
from x_python_sdk.apis.tags.spaces_api import SpacesApi
from x_python_sdk.apis.tags.bookmarks_api import BookmarksApi
from x_python_sdk.apis.tags.general_api import GeneralApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.TWEETS: TweetsApi,
        TagValues.USERS: UsersApi,
        TagValues.LISTS: ListsApi,
        TagValues.COMPLIANCE: ComplianceApi,
        TagValues.DIRECT_MESSAGES: DirectMessagesApi,
        TagValues.SPACES: SpacesApi,
        TagValues.BOOKMARKS: BookmarksApi,
        TagValues.GENERAL: GeneralApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.TWEETS: TweetsApi,
        TagValues.USERS: UsersApi,
        TagValues.LISTS: ListsApi,
        TagValues.COMPLIANCE: ComplianceApi,
        TagValues.DIRECT_MESSAGES: DirectMessagesApi,
        TagValues.SPACES: SpacesApi,
        TagValues.BOOKMARKS: BookmarksApi,
        TagValues.GENERAL: GeneralApi,
    }
)
