import typing_extensions

from x_python_sdk.paths import PathValues
from x_python_sdk.apis.paths._2_compliance_jobs import Model2ComplianceJobs
from x_python_sdk.apis.paths._2_compliance_jobs_id import Model2ComplianceJobsId
from x_python_sdk.apis.paths._2_dm_conversations import Model2DmConversations
from x_python_sdk.apis.paths._2_dm_conversations_with_participant_id_dm_events import Model2DmConversationsWithParticipantIdDmEvents
from x_python_sdk.apis.paths._2_dm_conversations_with_participant_id_messages import Model2DmConversationsWithParticipantIdMessages
from x_python_sdk.apis.paths._2_dm_conversations_dm_conversation_id_messages import Model2DmConversationsDmConversationIdMessages
from x_python_sdk.apis.paths._2_dm_conversations_id_dm_events import Model2DmConversationsIdDmEvents
from x_python_sdk.apis.paths._2_dm_events import Model2DmEvents
from x_python_sdk.apis.paths._2_lists import Model2Lists
from x_python_sdk.apis.paths._2_lists_id import Model2ListsId
from x_python_sdk.apis.paths._2_lists_id_followers import Model2ListsIdFollowers
from x_python_sdk.apis.paths._2_lists_id_members import Model2ListsIdMembers
from x_python_sdk.apis.paths._2_lists_id_members_user_id import Model2ListsIdMembersUserId
from x_python_sdk.apis.paths._2_lists_id_tweets import Model2ListsIdTweets
from x_python_sdk.apis.paths._2_openapi_json import Model2OpenapiJson
from x_python_sdk.apis.paths._2_spaces import Model2Spaces
from x_python_sdk.apis.paths._2_spaces_by_creator_ids import Model2SpacesByCreatorIds
from x_python_sdk.apis.paths._2_spaces_search import Model2SpacesSearch
from x_python_sdk.apis.paths._2_spaces_id import Model2SpacesId
from x_python_sdk.apis.paths._2_spaces_id_buyers import Model2SpacesIdBuyers
from x_python_sdk.apis.paths._2_spaces_id_tweets import Model2SpacesIdTweets
from x_python_sdk.apis.paths._2_tweets import Model2Tweets
from x_python_sdk.apis.paths._2_tweets_compliance_stream import Model2TweetsComplianceStream
from x_python_sdk.apis.paths._2_tweets_counts_all import Model2TweetsCountsAll
from x_python_sdk.apis.paths._2_tweets_counts_recent import Model2TweetsCountsRecent
from x_python_sdk.apis.paths._2_tweets_firehose_stream import Model2TweetsFirehoseStream
from x_python_sdk.apis.paths._2_tweets_label_stream import Model2TweetsLabelStream
from x_python_sdk.apis.paths._2_tweets_sample_stream import Model2TweetsSampleStream
from x_python_sdk.apis.paths._2_tweets_sample10_stream import Model2TweetsSample10Stream
from x_python_sdk.apis.paths._2_tweets_search_all import Model2TweetsSearchAll
from x_python_sdk.apis.paths._2_tweets_search_recent import Model2TweetsSearchRecent
from x_python_sdk.apis.paths._2_tweets_search_stream import Model2TweetsSearchStream
from x_python_sdk.apis.paths._2_tweets_search_stream_rules import Model2TweetsSearchStreamRules
from x_python_sdk.apis.paths._2_tweets_id import Model2TweetsId
from x_python_sdk.apis.paths._2_tweets_id_liking_users import Model2TweetsIdLikingUsers
from x_python_sdk.apis.paths._2_tweets_id_quote_tweets import Model2TweetsIdQuoteTweets
from x_python_sdk.apis.paths._2_tweets_id_retweeted_by import Model2TweetsIdRetweetedBy
from x_python_sdk.apis.paths._2_tweets_tweet_id_hidden import Model2TweetsTweetIdHidden
from x_python_sdk.apis.paths._2_users import Model2Users
from x_python_sdk.apis.paths._2_users_by import Model2UsersBy
from x_python_sdk.apis.paths._2_users_by_username_username import Model2UsersByUsernameUsername
from x_python_sdk.apis.paths._2_users_compliance_stream import Model2UsersComplianceStream
from x_python_sdk.apis.paths._2_users_me import Model2UsersMe
from x_python_sdk.apis.paths._2_users_id import Model2UsersId
from x_python_sdk.apis.paths._2_users_id_blocking import Model2UsersIdBlocking
from x_python_sdk.apis.paths._2_users_id_bookmarks import Model2UsersIdBookmarks
from x_python_sdk.apis.paths._2_users_id_bookmarks_tweet_id import Model2UsersIdBookmarksTweetId
from x_python_sdk.apis.paths._2_users_id_followed_lists import Model2UsersIdFollowedLists
from x_python_sdk.apis.paths._2_users_id_followed_lists_list_id import Model2UsersIdFollowedListsListId
from x_python_sdk.apis.paths._2_users_id_followers import Model2UsersIdFollowers
from x_python_sdk.apis.paths._2_users_id_following import Model2UsersIdFollowing
from x_python_sdk.apis.paths._2_users_id_liked_tweets import Model2UsersIdLikedTweets
from x_python_sdk.apis.paths._2_users_id_likes import Model2UsersIdLikes
from x_python_sdk.apis.paths._2_users_id_likes_tweet_id import Model2UsersIdLikesTweetId
from x_python_sdk.apis.paths._2_users_id_list_memberships import Model2UsersIdListMemberships
from x_python_sdk.apis.paths._2_users_id_mentions import Model2UsersIdMentions
from x_python_sdk.apis.paths._2_users_id_muting import Model2UsersIdMuting
from x_python_sdk.apis.paths._2_users_id_owned_lists import Model2UsersIdOwnedLists
from x_python_sdk.apis.paths._2_users_id_pinned_lists import Model2UsersIdPinnedLists
from x_python_sdk.apis.paths._2_users_id_pinned_lists_list_id import Model2UsersIdPinnedListsListId
from x_python_sdk.apis.paths._2_users_id_retweets import Model2UsersIdRetweets
from x_python_sdk.apis.paths._2_users_id_retweets_source_tweet_id import Model2UsersIdRetweetsSourceTweetId
from x_python_sdk.apis.paths._2_users_id_timelines_reverse_chronological import Model2UsersIdTimelinesReverseChronological
from x_python_sdk.apis.paths._2_users_id_tweets import Model2UsersIdTweets
from x_python_sdk.apis.paths._2_users_source_user_id_blocking_target_user_id import Model2UsersSourceUserIdBlockingTargetUserId
from x_python_sdk.apis.paths._2_users_source_user_id_following_target_user_id import Model2UsersSourceUserIdFollowingTargetUserId
from x_python_sdk.apis.paths._2_users_source_user_id_muting_target_user_id import Model2UsersSourceUserIdMutingTargetUserId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues._2_COMPLIANCE_JOBS: Model2ComplianceJobs,
        PathValues._2_COMPLIANCE_JOBS_ID: Model2ComplianceJobsId,
        PathValues._2_DM_CONVERSATIONS: Model2DmConversations,
        PathValues._2_DM_CONVERSATIONS_WITH_PARTICIPANT_ID_DM_EVENTS: Model2DmConversationsWithParticipantIdDmEvents,
        PathValues._2_DM_CONVERSATIONS_WITH_PARTICIPANT_ID_MESSAGES: Model2DmConversationsWithParticipantIdMessages,
        PathValues._2_DM_CONVERSATIONS_DM_CONVERSATION_ID_MESSAGES: Model2DmConversationsDmConversationIdMessages,
        PathValues._2_DM_CONVERSATIONS_ID_DM_EVENTS: Model2DmConversationsIdDmEvents,
        PathValues._2_DM_EVENTS: Model2DmEvents,
        PathValues._2_LISTS: Model2Lists,
        PathValues._2_LISTS_ID: Model2ListsId,
        PathValues._2_LISTS_ID_FOLLOWERS: Model2ListsIdFollowers,
        PathValues._2_LISTS_ID_MEMBERS: Model2ListsIdMembers,
        PathValues._2_LISTS_ID_MEMBERS_USER_ID: Model2ListsIdMembersUserId,
        PathValues._2_LISTS_ID_TWEETS: Model2ListsIdTweets,
        PathValues._2_OPENAPI_JSON: Model2OpenapiJson,
        PathValues._2_SPACES: Model2Spaces,
        PathValues._2_SPACES_BY_CREATOR_IDS: Model2SpacesByCreatorIds,
        PathValues._2_SPACES_SEARCH: Model2SpacesSearch,
        PathValues._2_SPACES_ID: Model2SpacesId,
        PathValues._2_SPACES_ID_BUYERS: Model2SpacesIdBuyers,
        PathValues._2_SPACES_ID_TWEETS: Model2SpacesIdTweets,
        PathValues._2_TWEETS: Model2Tweets,
        PathValues._2_TWEETS_COMPLIANCE_STREAM: Model2TweetsComplianceStream,
        PathValues._2_TWEETS_COUNTS_ALL: Model2TweetsCountsAll,
        PathValues._2_TWEETS_COUNTS_RECENT: Model2TweetsCountsRecent,
        PathValues._2_TWEETS_FIREHOSE_STREAM: Model2TweetsFirehoseStream,
        PathValues._2_TWEETS_LABEL_STREAM: Model2TweetsLabelStream,
        PathValues._2_TWEETS_SAMPLE_STREAM: Model2TweetsSampleStream,
        PathValues._2_TWEETS_SAMPLE10_STREAM: Model2TweetsSample10Stream,
        PathValues._2_TWEETS_SEARCH_ALL: Model2TweetsSearchAll,
        PathValues._2_TWEETS_SEARCH_RECENT: Model2TweetsSearchRecent,
        PathValues._2_TWEETS_SEARCH_STREAM: Model2TweetsSearchStream,
        PathValues._2_TWEETS_SEARCH_STREAM_RULES: Model2TweetsSearchStreamRules,
        PathValues._2_TWEETS_ID: Model2TweetsId,
        PathValues._2_TWEETS_ID_LIKING_USERS: Model2TweetsIdLikingUsers,
        PathValues._2_TWEETS_ID_QUOTE_TWEETS: Model2TweetsIdQuoteTweets,
        PathValues._2_TWEETS_ID_RETWEETED_BY: Model2TweetsIdRetweetedBy,
        PathValues._2_TWEETS_TWEET_ID_HIDDEN: Model2TweetsTweetIdHidden,
        PathValues._2_USERS: Model2Users,
        PathValues._2_USERS_BY: Model2UsersBy,
        PathValues._2_USERS_BY_USERNAME_USERNAME: Model2UsersByUsernameUsername,
        PathValues._2_USERS_COMPLIANCE_STREAM: Model2UsersComplianceStream,
        PathValues._2_USERS_ME: Model2UsersMe,
        PathValues._2_USERS_ID: Model2UsersId,
        PathValues._2_USERS_ID_BLOCKING: Model2UsersIdBlocking,
        PathValues._2_USERS_ID_BOOKMARKS: Model2UsersIdBookmarks,
        PathValues._2_USERS_ID_BOOKMARKS_TWEET_ID: Model2UsersIdBookmarksTweetId,
        PathValues._2_USERS_ID_FOLLOWED_LISTS: Model2UsersIdFollowedLists,
        PathValues._2_USERS_ID_FOLLOWED_LISTS_LIST_ID: Model2UsersIdFollowedListsListId,
        PathValues._2_USERS_ID_FOLLOWERS: Model2UsersIdFollowers,
        PathValues._2_USERS_ID_FOLLOWING: Model2UsersIdFollowing,
        PathValues._2_USERS_ID_LIKED_TWEETS: Model2UsersIdLikedTweets,
        PathValues._2_USERS_ID_LIKES: Model2UsersIdLikes,
        PathValues._2_USERS_ID_LIKES_TWEET_ID: Model2UsersIdLikesTweetId,
        PathValues._2_USERS_ID_LIST_MEMBERSHIPS: Model2UsersIdListMemberships,
        PathValues._2_USERS_ID_MENTIONS: Model2UsersIdMentions,
        PathValues._2_USERS_ID_MUTING: Model2UsersIdMuting,
        PathValues._2_USERS_ID_OWNED_LISTS: Model2UsersIdOwnedLists,
        PathValues._2_USERS_ID_PINNED_LISTS: Model2UsersIdPinnedLists,
        PathValues._2_USERS_ID_PINNED_LISTS_LIST_ID: Model2UsersIdPinnedListsListId,
        PathValues._2_USERS_ID_RETWEETS: Model2UsersIdRetweets,
        PathValues._2_USERS_ID_RETWEETS_SOURCE_TWEET_ID: Model2UsersIdRetweetsSourceTweetId,
        PathValues._2_USERS_ID_TIMELINES_REVERSE_CHRONOLOGICAL: Model2UsersIdTimelinesReverseChronological,
        PathValues._2_USERS_ID_TWEETS: Model2UsersIdTweets,
        PathValues._2_USERS_SOURCE_USER_ID_BLOCKING_TARGET_USER_ID: Model2UsersSourceUserIdBlockingTargetUserId,
        PathValues._2_USERS_SOURCE_USER_ID_FOLLOWING_TARGET_USER_ID: Model2UsersSourceUserIdFollowingTargetUserId,
        PathValues._2_USERS_SOURCE_USER_ID_MUTING_TARGET_USER_ID: Model2UsersSourceUserIdMutingTargetUserId,
    }
)

path_to_api = PathToApi(
    {
        PathValues._2_COMPLIANCE_JOBS: Model2ComplianceJobs,
        PathValues._2_COMPLIANCE_JOBS_ID: Model2ComplianceJobsId,
        PathValues._2_DM_CONVERSATIONS: Model2DmConversations,
        PathValues._2_DM_CONVERSATIONS_WITH_PARTICIPANT_ID_DM_EVENTS: Model2DmConversationsWithParticipantIdDmEvents,
        PathValues._2_DM_CONVERSATIONS_WITH_PARTICIPANT_ID_MESSAGES: Model2DmConversationsWithParticipantIdMessages,
        PathValues._2_DM_CONVERSATIONS_DM_CONVERSATION_ID_MESSAGES: Model2DmConversationsDmConversationIdMessages,
        PathValues._2_DM_CONVERSATIONS_ID_DM_EVENTS: Model2DmConversationsIdDmEvents,
        PathValues._2_DM_EVENTS: Model2DmEvents,
        PathValues._2_LISTS: Model2Lists,
        PathValues._2_LISTS_ID: Model2ListsId,
        PathValues._2_LISTS_ID_FOLLOWERS: Model2ListsIdFollowers,
        PathValues._2_LISTS_ID_MEMBERS: Model2ListsIdMembers,
        PathValues._2_LISTS_ID_MEMBERS_USER_ID: Model2ListsIdMembersUserId,
        PathValues._2_LISTS_ID_TWEETS: Model2ListsIdTweets,
        PathValues._2_OPENAPI_JSON: Model2OpenapiJson,
        PathValues._2_SPACES: Model2Spaces,
        PathValues._2_SPACES_BY_CREATOR_IDS: Model2SpacesByCreatorIds,
        PathValues._2_SPACES_SEARCH: Model2SpacesSearch,
        PathValues._2_SPACES_ID: Model2SpacesId,
        PathValues._2_SPACES_ID_BUYERS: Model2SpacesIdBuyers,
        PathValues._2_SPACES_ID_TWEETS: Model2SpacesIdTweets,
        PathValues._2_TWEETS: Model2Tweets,
        PathValues._2_TWEETS_COMPLIANCE_STREAM: Model2TweetsComplianceStream,
        PathValues._2_TWEETS_COUNTS_ALL: Model2TweetsCountsAll,
        PathValues._2_TWEETS_COUNTS_RECENT: Model2TweetsCountsRecent,
        PathValues._2_TWEETS_FIREHOSE_STREAM: Model2TweetsFirehoseStream,
        PathValues._2_TWEETS_LABEL_STREAM: Model2TweetsLabelStream,
        PathValues._2_TWEETS_SAMPLE_STREAM: Model2TweetsSampleStream,
        PathValues._2_TWEETS_SAMPLE10_STREAM: Model2TweetsSample10Stream,
        PathValues._2_TWEETS_SEARCH_ALL: Model2TweetsSearchAll,
        PathValues._2_TWEETS_SEARCH_RECENT: Model2TweetsSearchRecent,
        PathValues._2_TWEETS_SEARCH_STREAM: Model2TweetsSearchStream,
        PathValues._2_TWEETS_SEARCH_STREAM_RULES: Model2TweetsSearchStreamRules,
        PathValues._2_TWEETS_ID: Model2TweetsId,
        PathValues._2_TWEETS_ID_LIKING_USERS: Model2TweetsIdLikingUsers,
        PathValues._2_TWEETS_ID_QUOTE_TWEETS: Model2TweetsIdQuoteTweets,
        PathValues._2_TWEETS_ID_RETWEETED_BY: Model2TweetsIdRetweetedBy,
        PathValues._2_TWEETS_TWEET_ID_HIDDEN: Model2TweetsTweetIdHidden,
        PathValues._2_USERS: Model2Users,
        PathValues._2_USERS_BY: Model2UsersBy,
        PathValues._2_USERS_BY_USERNAME_USERNAME: Model2UsersByUsernameUsername,
        PathValues._2_USERS_COMPLIANCE_STREAM: Model2UsersComplianceStream,
        PathValues._2_USERS_ME: Model2UsersMe,
        PathValues._2_USERS_ID: Model2UsersId,
        PathValues._2_USERS_ID_BLOCKING: Model2UsersIdBlocking,
        PathValues._2_USERS_ID_BOOKMARKS: Model2UsersIdBookmarks,
        PathValues._2_USERS_ID_BOOKMARKS_TWEET_ID: Model2UsersIdBookmarksTweetId,
        PathValues._2_USERS_ID_FOLLOWED_LISTS: Model2UsersIdFollowedLists,
        PathValues._2_USERS_ID_FOLLOWED_LISTS_LIST_ID: Model2UsersIdFollowedListsListId,
        PathValues._2_USERS_ID_FOLLOWERS: Model2UsersIdFollowers,
        PathValues._2_USERS_ID_FOLLOWING: Model2UsersIdFollowing,
        PathValues._2_USERS_ID_LIKED_TWEETS: Model2UsersIdLikedTweets,
        PathValues._2_USERS_ID_LIKES: Model2UsersIdLikes,
        PathValues._2_USERS_ID_LIKES_TWEET_ID: Model2UsersIdLikesTweetId,
        PathValues._2_USERS_ID_LIST_MEMBERSHIPS: Model2UsersIdListMemberships,
        PathValues._2_USERS_ID_MENTIONS: Model2UsersIdMentions,
        PathValues._2_USERS_ID_MUTING: Model2UsersIdMuting,
        PathValues._2_USERS_ID_OWNED_LISTS: Model2UsersIdOwnedLists,
        PathValues._2_USERS_ID_PINNED_LISTS: Model2UsersIdPinnedLists,
        PathValues._2_USERS_ID_PINNED_LISTS_LIST_ID: Model2UsersIdPinnedListsListId,
        PathValues._2_USERS_ID_RETWEETS: Model2UsersIdRetweets,
        PathValues._2_USERS_ID_RETWEETS_SOURCE_TWEET_ID: Model2UsersIdRetweetsSourceTweetId,
        PathValues._2_USERS_ID_TIMELINES_REVERSE_CHRONOLOGICAL: Model2UsersIdTimelinesReverseChronological,
        PathValues._2_USERS_ID_TWEETS: Model2UsersIdTweets,
        PathValues._2_USERS_SOURCE_USER_ID_BLOCKING_TARGET_USER_ID: Model2UsersSourceUserIdBlockingTargetUserId,
        PathValues._2_USERS_SOURCE_USER_ID_FOLLOWING_TARGET_USER_ID: Model2UsersSourceUserIdFollowingTargetUserId,
        PathValues._2_USERS_SOURCE_USER_ID_MUTING_TARGET_USER_ID: Model2UsersSourceUserIdMutingTargetUserId,
    }
)
