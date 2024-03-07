# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from x_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    TWEETS = "Tweets"
    USERS = "Users"
    LISTS = "Lists"
    COMPLIANCE = "Compliance"
    DIRECT_MESSAGES = "Direct Messages"
    SPACES = "Spaces"
    BOOKMARKS = "Bookmarks"
    GENERAL = "General"
