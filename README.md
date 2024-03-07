<div align="center">

[![Visit X](./header.png)](https://developer.x.com)

# X<a id="x"></a>

Twitter API v2 available endpoints


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`x.bookmarks.add_tweet`](#xbookmarksadd_tweet)
  * [`x.bookmarks.get_user_bookmarks`](#xbookmarksget_user_bookmarks)
  * [`x.bookmarks.remove_tweet`](#xbookmarksremove_tweet)
  * [`x.compliance.create_job`](#xcompliancecreate_job)
  * [`x.compliance.get_job_by_id`](#xcomplianceget_job_by_id)
  * [`x.compliance.list_jobs`](#xcompliancelist_jobs)
  * [`x.compliance.stream_data`](#xcompliancestream_data)
  * [`x.compliance.stream_tweets_label_events`](#xcompliancestream_tweets_label_events)
  * [`x.compliance.stream_users_data`](#xcompliancestream_users_data)
  * [`x.direct_messages.create_new_dm_conversation`](#xdirect_messagescreate_new_dm_conversation)
  * [`x.direct_messages.get_dm_events`](#xdirect_messagesget_dm_events)
  * [`x.direct_messages.get_dm_events_0`](#xdirect_messagesget_dm_events_0)
  * [`x.direct_messages.get_recent_dm_events`](#xdirect_messagesget_recent_dm_events)
  * [`x.direct_messages.send_new_message_to_dm_conversation`](#xdirect_messagessend_new_message_to_dm_conversation)
  * [`x.direct_messages.send_new_message_to_user`](#xdirect_messagessend_new_message_to_user)
  * [`x.general.get_open_api_spec`](#xgeneralget_open_api_spec)
  * [`x.lists.add_member`](#xlistsadd_member)
  * [`x.lists.create_new_list`](#xlistscreate_new_list)
  * [`x.lists.delete_owned_list`](#xlistsdelete_owned_list)
  * [`x.lists.follow_list`](#xlistsfollow_list)
  * [`x.lists.get_followed`](#xlistsget_followed)
  * [`x.lists.get_user_memberships`](#xlistsget_user_memberships)
  * [`x.lists.get_user_owned_lists`](#xlistsget_user_owned_lists)
  * [`x.lists.get_user_pinned_lists`](#xlistsget_user_pinned_lists)
  * [`x.lists.lookup_by_list_id`](#xlistslookup_by_list_id)
  * [`x.lists.pin_list`](#xlistspin_list)
  * [`x.lists.remove_member`](#xlistsremove_member)
  * [`x.lists.unfollow_list`](#xlistsunfollow_list)
  * [`x.lists.unpin_list`](#xlistsunpin_list)
  * [`x.lists.update_owned_list`](#xlistsupdate_owned_list)
  * [`x.spaces.find_matching_spaces`](#xspacesfind_matching_spaces)
  * [`x.spaces.get_buyers_list`](#xspacesget_buyers_list)
  * [`x.spaces.get_tweets`](#xspacesget_tweets)
  * [`x.spaces.lookup_by_creator_ids`](#xspaceslookup_by_creator_ids)
  * [`x.spaces.lookup_space_by_id`](#xspaceslookup_space_by_id)
  * [`x.spaces.lookup_space_ids`](#xspaceslookup_space_ids)
  * [`x.tweets.add_or_delete_rules`](#xtweetsadd_or_delete_rules)
  * [`x.tweets.create_tweet`](#xtweetscreate_tweet)
  * [`x.tweets.delete_by_id`](#xtweetsdelete_by_id)
  * [`x.tweets.get_buyers_list`](#xtweetsget_buyers_list)
  * [`x.tweets.get_filtered_stream`](#xtweetsget_filtered_stream)
  * [`x.tweets.get_firehose_stream`](#xtweetsget_firehose_stream)
  * [`x.tweets.get_liked_tweets`](#xtweetsget_liked_tweets)
  * [`x.tweets.get_mentions_by_id`](#xtweetsget_mentions_by_id)
  * [`x.tweets.get_quote_tweets`](#xtweetsget_quote_tweets)
  * [`x.tweets.get_recent_tweet_counts`](#xtweetsget_recent_tweet_counts)
  * [`x.tweets.get_recent_tweets`](#xtweetsget_recent_tweets)
  * [`x.tweets.get_tweet_counts`](#xtweetsget_tweet_counts)
  * [`x.tweets.get_tweets`](#xtweetsget_tweets)
  * [`x.tweets.get_user_home_timeline`](#xtweetsget_user_home_timeline)
  * [`x.tweets.hide_reply`](#xtweetshide_reply)
  * [`x.tweets.like_tweet`](#xtweetslike_tweet)
  * [`x.tweets.list_by_list_id`](#xtweetslist_by_list_id)
  * [`x.tweets.list_by_user_id`](#xtweetslist_by_user_id)
  * [`x.tweets.lookup_by_id`](#xtweetslookup_by_id)
  * [`x.tweets.lookup_by_tweet_ids`](#xtweetslookup_by_tweet_ids)
  * [`x.tweets.retweet_tweet_by_id`](#xtweetsretweet_tweet_by_id)
  * [`x.tweets.search_all`](#xtweetssearch_all)
  * [`x.tweets.search_stream_rules`](#xtweetssearch_stream_rules)
  * [`x.tweets.stream_sample`](#xtweetsstream_sample)
  * [`x.tweets.stream_sample10`](#xtweetsstream_sample10)
  * [`x.tweets.unlike_tweet_by_id`](#xtweetsunlike_tweet_by_id)
  * [`x.tweets.unretweet_by_id`](#xtweetsunretweet_by_id)
  * [`x.users.block_user_by_id`](#xusersblock_user_by_id)
  * [`x.users.follow_user`](#xusersfollow_user)
  * [`x.users.get_blocked_users`](#xusersget_blocked_users)
  * [`x.users.get_followers_by_id`](#xusersget_followers_by_id)
  * [`x.users.get_followers_by_list_id`](#xusersget_followers_by_list_id)
  * [`x.users.get_following_users`](#xusersget_following_users)
  * [`x.users.get_members_by_list_id`](#xusersget_members_by_list_id)
  * [`x.users.get_muted_users_by_id`](#xusersget_muted_users_by_id)
  * [`x.users.get_retweeted_by_tweet_id_users`](#xusersget_retweeted_by_tweet_id_users)
  * [`x.users.list_liking_users`](#xuserslist_liking_users)
  * [`x.users.lookup_by_id`](#xuserslookup_by_id)
  * [`x.users.lookup_by_ids`](#xuserslookup_by_ids)
  * [`x.users.lookup_by_username`](#xuserslookup_by_username)
  * [`x.users.lookup_by_usernames`](#xuserslookup_by_usernames)
  * [`x.users.lookup_me`](#xuserslookup_me)
  * [`x.users.mute_user_by_id`](#xusersmute_user_by_id)
  * [`x.users.unblock_user_by_id`](#xusersunblock_user_by_id)
  * [`x.users.unfollow_user`](#xusersunfollow_user)
  * [`x.users.unmute_by_user_id`](#xusersunmute_by_user_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=X&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from x_python_sdk import X, ApiException

x = X(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Add Tweet to Bookmarks
    add_tweet_response = x.bookmarks.add_tweet(
        tweet_id="1346889436626259968",
        id="2244994945",
    )
    print(add_tweet_response)
except ApiException as e:
    print("Exception when calling BookmarksApi.add_tweet: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from x_python_sdk import X, ApiException

x = X(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)


async def main():
    try:
        # Add Tweet to Bookmarks
        add_tweet_response = await x.bookmarks.aadd_tweet(
            tweet_id="1346889436626259968",
            id="2244994945",
        )
        print(add_tweet_response)
    except ApiException as e:
        print("Exception when calling BookmarksApi.add_tweet: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from x_python_sdk import X, ApiException

x = X(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

try:
    # Add Tweet to Bookmarks
    add_tweet_response = x.bookmarks.raw.add_tweet(
        tweet_id="1346889436626259968",
        id="2244994945",
    )
    pprint(add_tweet_response.body)
    pprint(add_tweet_response.body["data"])
    pprint(add_tweet_response.body["errors"])
    pprint(add_tweet_response.headers)
    pprint(add_tweet_response.status)
    pprint(add_tweet_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BookmarksApi.add_tweet: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `x.bookmarks.add_tweet`<a id="xbookmarksadd_tweet"></a>

Adds a Tweet (ID in the body) to the requesting User's (in the path) bookmarks

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_tweet_response = x.bookmarks.add_tweet(
    tweet_id="1346889436626259968",
    id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tweet_id: [`TweetId`](./x_python_sdk/type/tweet_id.py)<a id="tweet_id-tweetidx_python_sdktypetweet_idpy"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User for whom to add bookmarks.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BookmarkAddRequest`](./x_python_sdk/type/bookmark_add_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BookmarkMutationResponse`](./x_python_sdk/pydantic/bookmark_mutation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/bookmarks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.bookmarks.get_user_bookmarks`<a id="xbookmarksget_user_bookmarks"></a>

Returns Tweet objects that have been bookmarked by the requesting User

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_bookmarks_response = x.bookmarks.get_user_bookmarks(
    id="2244994945",
    max_results=1,
    pagination_token="a",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User for whom to return results.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdBookmarksResponse`](./x_python_sdk/pydantic/get2_users_id_bookmarks_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/bookmarks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.bookmarks.remove_tweet`<a id="xbookmarksremove_tweet"></a>

Removes a Tweet from the requesting User's bookmarked Tweets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_tweet_response = x.bookmarks.remove_tweet(
    id="2244994945",
    tweet_id="1346889436626259968",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User whose bookmark is to be removed.

##### tweet_id: [`TweetId`](./x_python_sdk/type/.py)<a id="tweet_id-tweetidx_python_sdktypepy"></a>

The ID of the Tweet that the source User is removing from bookmarks.

#### 🔄 Return<a id="🔄-return"></a>

[`BookmarkMutationResponse`](./x_python_sdk/pydantic/bookmark_mutation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/bookmarks/{tweet_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.compliance.create_job`<a id="xcompliancecreate_job"></a>

Creates a compliance for the given job type

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_job_response = x.compliance.create_job(
    type="tweets",
    name="my-job",
    resumable=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of compliance job to list.

##### name: [`ComplianceJobName`](./x_python_sdk/type/compliance_job_name.py)<a id="name-compliancejobnamex_python_sdktypecompliance_job_namepy"></a>

##### resumable: `bool`<a id="resumable-bool"></a>

If true, this endpoint will return a pre-signed URL with resumable uploads enabled.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateComplianceJobRequest`](./x_python_sdk/type/create_compliance_job_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateComplianceJobResponse`](./x_python_sdk/pydantic/create_compliance_job_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/compliance/jobs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.compliance.get_job_by_id`<a id="xcomplianceget_job_by_id"></a>

Returns a single Compliance Job by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_job_by_id_response = x.compliance.get_job_by_id(
    id="1372966999991541762",
    compliance_job_fields=[
        "created_at",
        "download_expires_at",
        "download_url",
        "id",
        "name",
        "resumable",
        "status",
        "type",
        "upload_expires_at",
        "upload_url",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`JobId`](./x_python_sdk/type/.py)<a id="id-jobidx_python_sdktypepy"></a>

The ID of the Compliance Job to retrieve.

##### compliance_job_fields: List[`str`]<a id="compliance_job_fields-liststr"></a>

A comma separated list of ComplianceJob fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2ComplianceJobsIdResponse`](./x_python_sdk/pydantic/get2_compliance_jobs_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/compliance/jobs/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.compliance.list_jobs`<a id="xcompliancelist_jobs"></a>

Returns recent Compliance Jobs for a given job type and optional job status

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_jobs_response = x.compliance.list_jobs(
    type="tweets",
    status="created",
    compliance_job_fields=[
        "created_at",
        "download_expires_at",
        "download_url",
        "id",
        "name",
        "resumable",
        "status",
        "type",
        "upload_expires_at",
        "upload_url",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

Type of Compliance Job to list.

##### status: `str`<a id="status-str"></a>

Status of Compliance Job to list.

##### compliance_job_fields: List[`str`]<a id="compliance_job_fields-liststr"></a>

A comma separated list of ComplianceJob fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2ComplianceJobsResponse`](./x_python_sdk/pydantic/get2_compliance_jobs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/compliance/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.compliance.stream_data`<a id="xcompliancestream_data"></a>

Streams 100% of compliance data for Tweets

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
stream_data_response = x.compliance.stream_data(
    partition=1,
    backfill_minutes=0,
    start_time="2021-02-01T18:40:40.000Z",
    end_time="2021-02-14T18:40:40.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partition: `int`<a id="partition-int"></a>

The partition number.

##### backfill_minutes: `int`<a id="backfill_minutes-int"></a>

The number of minutes of backfill requested.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweet Compliance events will be provided.

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweet Compliance events will be provided.

#### 🔄 Return<a id="🔄-return"></a>

[`TweetComplianceStreamResponse`](./x_python_sdk/pydantic/tweet_compliance_stream_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/compliance/stream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.compliance.stream_tweets_label_events`<a id="xcompliancestream_tweets_label_events"></a>

Streams 100% of labeling events applied to Tweets

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
stream_tweets_label_events_response = x.compliance.stream_tweets_label_events(
    backfill_minutes=0,
    start_time="2021-02-01T18:40:40.000Z",
    end_time="2021-02-01T18:40:40.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### backfill_minutes: `int`<a id="backfill_minutes-int"></a>

The number of minutes of backfill requested.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweet labels will be provided.

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the Tweet labels will be provided.

#### 🔄 Return<a id="🔄-return"></a>

[`TweetLabelStreamResponse`](./x_python_sdk/pydantic/tweet_label_stream_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/label/stream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.compliance.stream_users_data`<a id="xcompliancestream_users_data"></a>

Streams 100% of compliance data for Users

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
stream_users_data_response = x.compliance.stream_users_data(
    partition=1,
    backfill_minutes=0,
    start_time="2021-02-01T18:40:40.000Z",
    end_time="2021-02-01T18:40:40.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partition: `int`<a id="partition-int"></a>

The partition number.

##### backfill_minutes: `int`<a id="backfill_minutes-int"></a>

The number of minutes of backfill requested.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the User Compliance events will be provided.

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp from which the User Compliance events will be provided.

#### 🔄 Return<a id="🔄-return"></a>

[`UserComplianceStreamResponse`](./x_python_sdk/pydantic/user_compliance_stream_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/compliance/stream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.direct_messages.create_new_dm_conversation`<a id="xdirect_messagescreate_new_dm_conversation"></a>

Creates a new DM Conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_dm_conversation_response = x.direct_messages.create_new_dm_conversation(
    conversation_type="Group",
    message={
        "text": "text_example",
    },
    participant_ids=["4807288800152802"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### conversation_type: `str`<a id="conversation_type-str"></a>

The conversation type that is being created.

##### message: `CreateMessageRequest`<a id="message-createmessagerequest"></a>

##### participant_ids: [`DmParticipants`](./x_python_sdk/type/dm_participants.py)<a id="participant_ids-dmparticipantsx_python_sdktypedm_participantspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateDmConversationRequest`](./x_python_sdk/type/create_dm_conversation_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateDmEventResponse`](./x_python_sdk/pydantic/create_dm_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/dm_conversations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.direct_messages.get_dm_events`<a id="xdirect_messagesget_dm_events"></a>

Returns DM Events for a DM Conversation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_dm_events_response = x.direct_messages.get_dm_events(
    participant_id="2244994945",
    max_results=100,
    pagination_token="aaaaaaaaaaaaaaaa",
    event_types=["MessageCreate", "ParticipantsLeave"],
    dm_event_fields=[
        "attachments",
        "created_at",
        "dm_conversation_id",
        "event_type",
        "id",
        "participant_ids",
        "referenced_tweets",
        "sender_id",
        "text",
    ],
    expansions=[
        "attachments.media_keys",
        "participant_ids",
        "referenced_tweets.id",
        "sender_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### participant_id: [`UserId`](./x_python_sdk/type/.py)<a id="participant_id-useridx_python_sdktypepy"></a>

The ID of the participant user for the One to One DM conversation.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken32`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken32x_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### event_types: List[`str`]<a id="event_types-liststr"></a>

The set of event_types to include in the results.

##### dm_event_fields: List[`str`]<a id="dm_event_fields-liststr"></a>

A comma separated list of DmEvent fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2DmConversationsWithParticipantIdDmEventsResponse`](./x_python_sdk/pydantic/get2_dm_conversations_with_participant_id_dm_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/dm_conversations/with/{participant_id}/dm_events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.direct_messages.get_dm_events_0`<a id="xdirect_messagesget_dm_events_0"></a>

Returns DM Events for a DM Conversation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_dm_events_0_response = x.direct_messages.get_dm_events_0(
    id="123123123-456456456",
    max_results=100,
    pagination_token="aaaaaaaaaaaaaaaa",
    event_types=["MessageCreate", "ParticipantsLeave"],
    dm_event_fields=[
        "attachments",
        "created_at",
        "dm_conversation_id",
        "event_type",
        "id",
        "participant_ids",
        "referenced_tweets",
        "sender_id",
        "text",
    ],
    expansions=[
        "attachments.media_keys",
        "participant_ids",
        "referenced_tweets.id",
        "sender_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`DmConversationId`](./x_python_sdk/type/.py)<a id="id-dmconversationidx_python_sdktypepy"></a>

The DM Conversation ID.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken32`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken32x_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### event_types: List[`str`]<a id="event_types-liststr"></a>

The set of event_types to include in the results.

##### dm_event_fields: List[`str`]<a id="dm_event_fields-liststr"></a>

A comma separated list of DmEvent fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2DmConversationsIdDmEventsResponse`](./x_python_sdk/pydantic/get2_dm_conversations_id_dm_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/dm_conversations/{id}/dm_events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.direct_messages.get_recent_dm_events`<a id="xdirect_messagesget_recent_dm_events"></a>

Returns recent DM Events across DM conversations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_dm_events_response = x.direct_messages.get_recent_dm_events(
    max_results=100,
    pagination_token="aaaaaaaaaaaaaaaa",
    event_types=["MessageCreate", "ParticipantsLeave"],
    dm_event_fields=[
        "attachments",
        "created_at",
        "dm_conversation_id",
        "event_type",
        "id",
        "participant_ids",
        "referenced_tweets",
        "sender_id",
        "text",
    ],
    expansions=[
        "attachments.media_keys",
        "participant_ids",
        "referenced_tweets.id",
        "sender_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken32`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken32x_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### event_types: List[`str`]<a id="event_types-liststr"></a>

The set of event_types to include in the results.

##### dm_event_fields: List[`str`]<a id="dm_event_fields-liststr"></a>

A comma separated list of DmEvent fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2DmEventsResponse`](./x_python_sdk/pydantic/get2_dm_events_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/dm_events` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.direct_messages.send_new_message_to_dm_conversation`<a id="xdirect_messagessend_new_message_to_dm_conversation"></a>

Creates a new message for a DM Conversation specified by DM Conversation ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_new_message_to_dm_conversation_response = (
    x.direct_messages.send_new_message_to_dm_conversation(
        body={
            "text": "text_example",
        },
        dm_conversation_id="dm_conversation_id_example",
        attachments=[
            {
                "media_id": "1146654567674912769",
            }
        ],
        text="a",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dm_conversation_id: `str`<a id="dm_conversation_id-str"></a>

The DM Conversation ID.

##### attachments: [`DmAttachments`](./x_python_sdk/type/dm_attachments.py)<a id="attachments-dmattachmentsx_python_sdktypedm_attachmentspy"></a>

##### text: `str`<a id="text-str"></a>

Text of the message.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateMessageRequest`](./x_python_sdk/type/create_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateDmEventResponse`](./x_python_sdk/pydantic/create_dm_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/dm_conversations/{dm_conversation_id}/messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.direct_messages.send_new_message_to_user`<a id="xdirect_messagessend_new_message_to_user"></a>

Creates a new message for a DM Conversation with a participant user by ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_new_message_to_user_response = x.direct_messages.send_new_message_to_user(
    body={
        "text": "text_example",
    },
    participant_id="2244994945",
    attachments=[
        {
            "media_id": "1146654567674912769",
        }
    ],
    text="a",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### participant_id: [`UserId`](./x_python_sdk/type/.py)<a id="participant_id-useridx_python_sdktypepy"></a>

The ID of the recipient user that will receive the DM.

##### attachments: [`DmAttachments`](./x_python_sdk/type/dm_attachments.py)<a id="attachments-dmattachmentsx_python_sdktypedm_attachmentspy"></a>

##### text: `str`<a id="text-str"></a>

Text of the message.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateMessageRequest`](./x_python_sdk/type/create_message_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CreateDmEventResponse`](./x_python_sdk/pydantic/create_dm_event_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/dm_conversations/with/{participant_id}/messages` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.general.get_open_api_spec`<a id="xgeneralget_open_api_spec"></a>

Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_open_api_spec_response = x.general.get_open_api_spec()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/openapi.json` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.add_member`<a id="xlistsadd_member"></a>

Causes a User to become a member of a List.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_member_response = x.lists.add_member(
    user_id="2244994945",
    id="1146654567674912769",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: [`UserId`](./x_python_sdk/type/user_id.py)<a id="user_id-useridx_python_sdktypeuser_idpy"></a>

##### id: [`ListId`](./x_python_sdk/type/.py)<a id="id-listidx_python_sdktypepy"></a>

The ID of the List for which to add a member.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListAddUserRequest`](./x_python_sdk/type/list_add_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ListMutateResponse`](./x_python_sdk/pydantic/list_mutate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/lists/{id}/members` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.create_new_list`<a id="xlistscreate_new_list"></a>

Creates a new List.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_list_response = x.lists.create_new_list(
    name="a",
    description="",
    private=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### description: `str`<a id="description-str"></a>

##### private: `bool`<a id="private-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListCreateRequest`](./x_python_sdk/type/list_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ListCreateResponse`](./x_python_sdk/pydantic/list_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/lists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.delete_owned_list`<a id="xlistsdelete_owned_list"></a>

Delete a List that you own.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_owned_list_response = x.lists.delete_owned_list(
    id="1146654567674912769",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`ListId`](./x_python_sdk/type/.py)<a id="id-listidx_python_sdktypepy"></a>

The ID of the List to delete.

#### 🔄 Return<a id="🔄-return"></a>

[`ListDeleteResponse`](./x_python_sdk/pydantic/list_delete_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/lists/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.follow_list`<a id="xlistsfollow_list"></a>

Causes a User to follow a List.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
follow_list_response = x.lists.follow_list(
    list_id="1146654567674912769",
    id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: [`ListId`](./x_python_sdk/type/list_id.py)<a id="list_id-listidx_python_sdktypelist_idpy"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that will follow the List.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListFollowedRequest`](./x_python_sdk/type/list_followed_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ListFollowedResponse`](./x_python_sdk/pydantic/list_followed_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/followed_lists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.get_followed`<a id="xlistsget_followed"></a>

Returns a User's followed Lists.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followed_response = x.lists.get_followed(
    id="2244994945",
    max_results=100,
    pagination_token="a",
    list_fields=[
        "created_at",
        "description",
        "follower_count",
        "id",
        "member_count",
        "name",
        "owner_id",
        "private",
    ],
    expansions=["owner_id"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`UserId`](./x_python_sdk/type/.py)<a id="id-useridx_python_sdktypepy"></a>

The ID of the User to lookup.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationTokenLong`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtokenlongx_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### list_fields: List[`str`]<a id="list_fields-liststr"></a>

A comma separated list of List fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdFollowedListsResponse`](./x_python_sdk/pydantic/get2_users_id_followed_lists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/followed_lists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.get_user_memberships`<a id="xlistsget_user_memberships"></a>

Get a User's List Memberships.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_memberships_response = x.lists.get_user_memberships(
    id="2244994945",
    max_results=100,
    pagination_token="a",
    list_fields=[
        "created_at",
        "description",
        "follower_count",
        "id",
        "member_count",
        "name",
        "owner_id",
        "private",
    ],
    expansions=["owner_id"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`UserId`](./x_python_sdk/type/.py)<a id="id-useridx_python_sdktypepy"></a>

The ID of the User to lookup.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationTokenLong`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtokenlongx_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### list_fields: List[`str`]<a id="list_fields-liststr"></a>

A comma separated list of List fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdListMembershipsResponse`](./x_python_sdk/pydantic/get2_users_id_list_memberships_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/list_memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.get_user_owned_lists`<a id="xlistsget_user_owned_lists"></a>

Get a User's Owned Lists.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_owned_lists_response = x.lists.get_user_owned_lists(
    id="2244994945",
    max_results=100,
    pagination_token="a",
    list_fields=[
        "created_at",
        "description",
        "follower_count",
        "id",
        "member_count",
        "name",
        "owner_id",
        "private",
    ],
    expansions=["owner_id"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`UserId`](./x_python_sdk/type/.py)<a id="id-useridx_python_sdktypepy"></a>

The ID of the User to lookup.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationTokenLong`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtokenlongx_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### list_fields: List[`str`]<a id="list_fields-liststr"></a>

A comma separated list of List fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdOwnedListsResponse`](./x_python_sdk/pydantic/get2_users_id_owned_lists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/owned_lists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.get_user_pinned_lists`<a id="xlistsget_user_pinned_lists"></a>

Get a User's Pinned Lists.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_pinned_lists_response = x.lists.get_user_pinned_lists(
    id="2244994945",
    list_fields=[
        "created_at",
        "description",
        "follower_count",
        "id",
        "member_count",
        "name",
        "owner_id",
        "private",
    ],
    expansions=["owner_id"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User for whom to return results.

##### list_fields: List[`str`]<a id="list_fields-liststr"></a>

A comma separated list of List fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdPinnedListsResponse`](./x_python_sdk/pydantic/get2_users_id_pinned_lists_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/pinned_lists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.lookup_by_list_id`<a id="xlistslookup_by_list_id"></a>

Returns a List.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_by_list_id_response = x.lists.lookup_by_list_id(
    id="1146654567674912769",
    list_fields=[
        "created_at",
        "description",
        "follower_count",
        "id",
        "member_count",
        "name",
        "owner_id",
        "private",
    ],
    expansions=["owner_id"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`ListId`](./x_python_sdk/type/.py)<a id="id-listidx_python_sdktypepy"></a>

The ID of the List.

##### list_fields: List[`str`]<a id="list_fields-liststr"></a>

A comma separated list of List fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2ListsIdResponse`](./x_python_sdk/pydantic/get2_lists_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/lists/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.pin_list`<a id="xlistspin_list"></a>

Causes a User to pin a List.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
pin_list_response = x.lists.pin_list(
    list_id="1146654567674912769",
    id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### list_id: [`ListId`](./x_python_sdk/type/list_id.py)<a id="list_id-listidx_python_sdktypelist_idpy"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that will pin the List.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListPinnedRequest`](./x_python_sdk/type/list_pinned_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ListPinnedResponse`](./x_python_sdk/pydantic/list_pinned_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/pinned_lists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.remove_member`<a id="xlistsremove_member"></a>

Causes a User to be removed from the members of a List.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_member_response = x.lists.remove_member(
    id="1146654567674912769",
    user_id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`ListId`](./x_python_sdk/type/.py)<a id="id-listidx_python_sdktypepy"></a>

The ID of the List to remove a member.

##### user_id: [`UserId`](./x_python_sdk/type/.py)<a id="user_id-useridx_python_sdktypepy"></a>

The ID of User that will be removed from the List.

#### 🔄 Return<a id="🔄-return"></a>

[`ListMutateResponse`](./x_python_sdk/pydantic/list_mutate_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/lists/{id}/members/{user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.unfollow_list`<a id="xlistsunfollow_list"></a>

Causes a User to unfollow a List.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unfollow_list_response = x.lists.unfollow_list(
    id="2244994945",
    list_id="1146654567674912769",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that will unfollow the List.

##### list_id: [`ListId`](./x_python_sdk/type/.py)<a id="list_id-listidx_python_sdktypepy"></a>

The ID of the List to unfollow.

#### 🔄 Return<a id="🔄-return"></a>

[`ListFollowedResponse`](./x_python_sdk/pydantic/list_followed_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/followed_lists/{list_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.unpin_list`<a id="xlistsunpin_list"></a>

Causes a User to remove a pinned List.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unpin_list_response = x.lists.unpin_list(
    id="2244994945",
    list_id="1146654567674912769",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User for whom to return results.

##### list_id: [`ListId`](./x_python_sdk/type/.py)<a id="list_id-listidx_python_sdktypepy"></a>

The ID of the List to unpin.

#### 🔄 Return<a id="🔄-return"></a>

[`ListUnpinResponse`](./x_python_sdk/pydantic/list_unpin_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/pinned_lists/{list_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.lists.update_owned_list`<a id="xlistsupdate_owned_list"></a>

Update a List that you own.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_owned_list_response = x.lists.update_owned_list(
    id="1146654567674912769",
    description="",
    name="a",
    private=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`ListId`](./x_python_sdk/type/.py)<a id="id-listidx_python_sdktypepy"></a>

The ID of the List to modify.

##### description: `str`<a id="description-str"></a>

##### name: `str`<a id="name-str"></a>

##### private: `bool`<a id="private-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListUpdateRequest`](./x_python_sdk/type/list_update_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ListUpdateResponse`](./x_python_sdk/pydantic/list_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/lists/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.spaces.find_matching_spaces`<a id="xspacesfind_matching_spaces"></a>

Returns Spaces that match the provided query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
find_matching_spaces_response = x.spaces.find_matching_spaces(
    query="crypto",
    state="all",
    max_results=100,
    space_fields=[
        "created_at",
        "creator_id",
        "ended_at",
        "host_ids",
        "id",
        "invited_user_ids",
        "is_ticketed",
        "lang",
        "participant_count",
        "scheduled_start",
        "speaker_ids",
        "started_at",
        "state",
        "subscriber_count",
        "title",
        "topic_ids",
        "updated_at",
    ],
    expansions=[
        "creator_id",
        "host_ids",
        "invited_user_ids",
        "speaker_ids",
        "topic_ids",
    ],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    topic_fields=["description", "id", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

The search query.

##### state: `str`<a id="state-str"></a>

The state of Spaces to search for.

##### max_results: `int`<a id="max_results-int"></a>

The number of results to return.

##### space_fields: List[`str`]<a id="space_fields-liststr"></a>

A comma separated list of Space fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### topic_fields: List[`str`]<a id="topic_fields-liststr"></a>

A comma separated list of Topic fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2SpacesSearchResponse`](./x_python_sdk/pydantic/get2_spaces_search_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/spaces/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.spaces.get_buyers_list`<a id="xspacesget_buyers_list"></a>

Retrieves the list of Users who purchased a ticket to the given space

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_buyers_list_response = x.spaces.get_buyers_list(
    id="1YqKDqWqdPLsV",
    pagination_token="aaaaaaaaaaaaaaaa",
    max_results=100,
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Space to be retrieved.

##### pagination_token: [`PaginationToken32`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken32x_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2SpacesIdBuyersResponse`](./x_python_sdk/pydantic/get2_spaces_id_buyers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/spaces/{id}/buyers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.spaces.get_tweets`<a id="xspacesget_tweets"></a>

Retrieves Tweets shared in the specified Space.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tweets_response = x.spaces.get_tweets(
    id="1YqKDqWqdPLsV",
    max_results=25,
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Space to be retrieved.

##### max_results: `int`<a id="max_results-int"></a>

The number of Tweets to fetch from the provided space. If not provided, the value will default to the maximum of 100.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2SpacesIdTweetsResponse`](./x_python_sdk/pydantic/get2_spaces_id_tweets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/spaces/{id}/tweets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.spaces.lookup_by_creator_ids`<a id="xspaceslookup_by_creator_ids"></a>

Returns a variety of information about the Spaces created by the provided User IDs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_by_creator_ids_response = x.spaces.lookup_by_creator_ids(
    user_ids=["2244994945"],
    space_fields=[
        "created_at",
        "creator_id",
        "ended_at",
        "host_ids",
        "id",
        "invited_user_ids",
        "is_ticketed",
        "lang",
        "participant_count",
        "scheduled_start",
        "speaker_ids",
        "started_at",
        "state",
        "subscriber_count",
        "title",
        "topic_ids",
        "updated_at",
    ],
    expansions=[
        "creator_id",
        "host_ids",
        "invited_user_ids",
        "speaker_ids",
        "topic_ids",
    ],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    topic_fields=["description", "id", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_ids: List[`UserId`]<a id="user_ids-listuserid"></a>

The IDs of Users to search through.

##### space_fields: List[`str`]<a id="space_fields-liststr"></a>

A comma separated list of Space fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### topic_fields: List[`str`]<a id="topic_fields-liststr"></a>

A comma separated list of Topic fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2SpacesByCreatorIdsResponse`](./x_python_sdk/pydantic/get2_spaces_by_creator_ids_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/spaces/by/creator_ids` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.spaces.lookup_space_by_id`<a id="xspaceslookup_space_by_id"></a>

Returns a variety of information about the Space specified by the requested ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_space_by_id_response = x.spaces.lookup_space_by_id(
    id="1YqKDqWqdPLsV",
    space_fields=[
        "created_at",
        "creator_id",
        "ended_at",
        "host_ids",
        "id",
        "invited_user_ids",
        "is_ticketed",
        "lang",
        "participant_count",
        "scheduled_start",
        "speaker_ids",
        "started_at",
        "state",
        "subscriber_count",
        "title",
        "topic_ids",
        "updated_at",
    ],
    expansions=[
        "creator_id",
        "host_ids",
        "invited_user_ids",
        "speaker_ids",
        "topic_ids",
    ],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    topic_fields=["description", "id", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Space to be retrieved.

##### space_fields: List[`str`]<a id="space_fields-liststr"></a>

A comma separated list of Space fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### topic_fields: List[`str`]<a id="topic_fields-liststr"></a>

A comma separated list of Topic fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2SpacesIdResponse`](./x_python_sdk/pydantic/get2_spaces_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/spaces/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.spaces.lookup_space_ids`<a id="xspaceslookup_space_ids"></a>

Returns a variety of information about the Spaces specified by the requested IDs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_space_ids_response = x.spaces.lookup_space_ids(
    ids=["1SLjjRYNejbKM"],
    space_fields=[
        "created_at",
        "creator_id",
        "ended_at",
        "host_ids",
        "id",
        "invited_user_ids",
        "is_ticketed",
        "lang",
        "participant_count",
        "scheduled_start",
        "speaker_ids",
        "started_at",
        "state",
        "subscriber_count",
        "title",
        "topic_ids",
        "updated_at",
    ],
    expansions=[
        "creator_id",
        "host_ids",
        "invited_user_ids",
        "speaker_ids",
        "topic_ids",
    ],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    topic_fields=["description", "id", "name"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: List[`str`]<a id="ids-liststr"></a>

The list of Space IDs to return.

##### space_fields: List[`str`]<a id="space_fields-liststr"></a>

A comma separated list of Space fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### topic_fields: List[`str`]<a id="topic_fields-liststr"></a>

A comma separated list of Topic fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2SpacesResponse`](./x_python_sdk/pydantic/get2_spaces_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/spaces` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.add_or_delete_rules`<a id="xtweetsadd_or_delete_rules"></a>

Add or delete rules from a User's active rule set. Users can provide unique, optionally tagged rules to add. Users can delete their entire rule set or a subset specified by rule ids or values.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_or_delete_rules_response = x.tweets.add_or_delete_rules(
    body=None,
    add=[
        {
            "tag": "Non-retweeted coffee Tweets",
            "value": "coffee -is:retweet",
        }
    ],
    delete={},
    dry_run=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### add: List[`RuleNoId`]<a id="add-listrulenoid"></a>

##### delete: [`DeleteRulesRequestDelete`](./x_python_sdk/type/delete_rules_request_delete.py)<a id="delete-deleterulesrequestdeletex_python_sdktypedelete_rules_request_deletepy"></a>


##### dry_run: `bool`<a id="dry_run-bool"></a>

Dry Run can be used with both the add and delete action, with the expected result given, but without actually taking any action in the system (meaning the end state will always be as it was when the request was submitted). This is particularly useful to validate rule changes.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddOrDeleteRulesRequest`](./x_python_sdk/type/add_or_delete_rules_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AddOrDeleteRulesResponse`](./x_python_sdk/pydantic/add_or_delete_rules_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/search/stream/rules` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.create_tweet`<a id="xtweetscreate_tweet"></a>

Causes the User to create a Tweet under the authorized account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_tweet_response = x.tweets.create_tweet(
    card_uri="string_example",
    direct_message_deep_link="string_example",
    for_super_followers_only=False,
    geo={},
    media={
        "media_ids": ["1146654567674912769"],
    },
    nullcast=False,
    poll={
        "duration_minutes": 5,
        "options": ["options_example"],
        "reply_settings": "following",
    },
    quote_tweet_id="1346889436626259968",
    reply={
        "in_reply_to_tweet_id": "1346889436626259968",
    },
    reply_settings="following",
    text="Learn how to use the user Tweet timeline and user mention timeline endpoints in the Twitter API v2 to explore Tweet\\u2026 https:\\/\\/t.co\\/56a0vZUx7i",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### card_uri: `str`<a id="card_uri-str"></a>

Card Uri Parameter. This is mutually exclusive from Quote Tweet Id, Poll, Media, and Direct Message Deep Link.

##### direct_message_deep_link: `str`<a id="direct_message_deep_link-str"></a>

Link to take the conversation from the public timeline to a private Direct Message.

##### for_super_followers_only: `bool`<a id="for_super_followers_only-bool"></a>

Exclusive Tweet for super followers.

##### geo: [`TweetCreateRequestGeo`](./x_python_sdk/type/tweet_create_request_geo.py)<a id="geo-tweetcreaterequestgeox_python_sdktypetweet_create_request_geopy"></a>


##### media: [`TweetCreateRequestMedia`](./x_python_sdk/type/tweet_create_request_media.py)<a id="media-tweetcreaterequestmediax_python_sdktypetweet_create_request_mediapy"></a>


##### nullcast: `bool`<a id="nullcast-bool"></a>

Nullcasted (promoted-only) Tweets do not appear in the public timeline and are not served to followers.

##### poll: [`TweetCreateRequestPoll`](./x_python_sdk/type/tweet_create_request_poll.py)<a id="poll-tweetcreaterequestpollx_python_sdktypetweet_create_request_pollpy"></a>


##### quote_tweet_id: [`TweetId`](./x_python_sdk/type/tweet_id.py)<a id="quote_tweet_id-tweetidx_python_sdktypetweet_idpy"></a>

##### reply: [`TweetCreateRequestReply`](./x_python_sdk/type/tweet_create_request_reply.py)<a id="reply-tweetcreaterequestreplyx_python_sdktypetweet_create_request_replypy"></a>


##### reply_settings: `str`<a id="reply_settings-str"></a>

Settings to indicate who can reply to the Tweet.

##### text: `str`<a id="text-str"></a>

The content of the Tweet.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TweetCreateRequest`](./x_python_sdk/type/tweet_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TweetCreateResponse`](./x_python_sdk/pydantic/tweet_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.delete_by_id`<a id="xtweetsdelete_by_id"></a>

Delete specified Tweet (in the path) by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = x.tweets.delete_by_id(
    id="1346889436626259968",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`TweetId`](./x_python_sdk/type/.py)<a id="id-tweetidx_python_sdktypepy"></a>

The ID of the Tweet to be deleted.

#### 🔄 Return<a id="🔄-return"></a>

[`TweetDeleteResponse`](./x_python_sdk/pydantic/tweet_delete_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_buyers_list`<a id="xtweetsget_buyers_list"></a>

Retrieves the list of Users who purchased a ticket to the given space

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_buyers_list_response = x.tweets.get_buyers_list(
    id="1YqKDqWqdPLsV",
    pagination_token="aaaaaaaaaaaaaaaa",
    max_results=100,
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Space to be retrieved.

##### pagination_token: [`PaginationToken32`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken32x_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2SpacesIdBuyersResponse`](./x_python_sdk/pydantic/get2_spaces_id_buyers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/spaces/{id}/buyers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_filtered_stream`<a id="xtweetsget_filtered_stream"></a>

Streams Tweets matching the stream's active rule set.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_filtered_stream_response = x.tweets.get_filtered_stream(
    backfill_minutes=0,
    start_time="2021-02-01T18:40:40.000Z",
    end_time="2021-02-14T18:40:40.000Z",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### backfill_minutes: `int`<a id="backfill_minutes-int"></a>

The number of minutes of backfill requested.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided.

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`FilteredStreamingTweetResponse`](./x_python_sdk/pydantic/filtered_streaming_tweet_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/search/stream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_firehose_stream`<a id="xtweetsget_firehose_stream"></a>

Streams 100% of public Tweets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_firehose_stream_response = x.tweets.get_firehose_stream(
    partition=1,
    backfill_minutes=0,
    start_time="2021-02-14T18:40:40.000Z",
    end_time="2021-02-14T18:40:40.000Z",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partition: `int`<a id="partition-int"></a>

The partition number.

##### backfill_minutes: `int`<a id="backfill_minutes-int"></a>

The number of minutes of backfill requested.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided.

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`StreamingTweetResponse`](./x_python_sdk/pydantic/streaming_tweet_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/firehose/stream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_liked_tweets`<a id="xtweetsget_liked_tweets"></a>

Returns a list of Tweets liked by the provided User ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_liked_tweets_response = x.tweets.get_liked_tweets(
    id="2244994945",
    max_results=5,
    pagination_token="a",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`UserId`](./x_python_sdk/type/.py)<a id="id-useridx_python_sdktypepy"></a>

The ID of the User to lookup.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdLikedTweetsResponse`](./x_python_sdk/pydantic/get2_users_id_liked_tweets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/liked_tweets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_mentions_by_id`<a id="xtweetsget_mentions_by_id"></a>

Returns Tweet objects that mention username associated to the provided User ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_mentions_by_id_response = x.tweets.get_mentions_by_id(
    id="2244994945",
    since_id="1346889436626259968",
    until_id="1346889436626259968",
    max_results=5,
    pagination_token="a",
    start_time="2021-02-01T18:40:40.000Z",
    end_time="2021-02-14T18:40:40.000Z",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`UserId`](./x_python_sdk/type/.py)<a id="id-useridx_python_sdktypepy"></a>

The ID of the User to lookup.

##### since_id: [`TweetId`](./x_python_sdk/type/.py)<a id="since_id-tweetidx_python_sdktypepy"></a>

The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.

##### until_id: [`TweetId`](./x_python_sdk/type/.py)<a id="until_id-tweetidx_python_sdktypepy"></a>

The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdMentionsResponse`](./x_python_sdk/pydantic/get2_users_id_mentions_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/mentions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_quote_tweets`<a id="xtweetsget_quote_tweets"></a>

Returns a variety of information about each Tweet that quotes the Tweet specified by the requested ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_quote_tweets_response = x.tweets.get_quote_tweets(
    id="1346889436626259968",
    max_results=10,
    pagination_token="a",
    exclude=["replies", "retweets"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`TweetId`](./x_python_sdk/type/.py)<a id="id-tweetidx_python_sdktypepy"></a>

A single Tweet ID.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results to be returned.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### exclude: List[`str`]<a id="exclude-liststr"></a>

The set of entities to exclude (e.g. 'replies' or 'retweets').

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsIdQuoteTweetsResponse`](./x_python_sdk/pydantic/get2_tweets_id_quote_tweets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/{id}/quote_tweets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_recent_tweet_counts`<a id="xtweetsget_recent_tweet_counts"></a>

Returns Tweet Counts from the last 7 days that match a search query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_tweet_counts_response = x.tweets.get_recent_tweet_counts(
    query="(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet",
    start_time="1970-01-01T00:00:00.00Z",
    end_time="1970-01-01T00:00:00.00Z",
    since_id="1346889436626259968",
    until_id="1346889436626259968",
    next_token="a",
    pagination_token="a",
    granularity="hour",
    search_count_fields=["end", "start", "tweet_count"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).

##### since_id: [`TweetId`](./x_python_sdk/type/.py)<a id="since_id-tweetidx_python_sdktypepy"></a>

Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.

##### until_id: [`TweetId`](./x_python_sdk/type/.py)<a id="until_id-tweetidx_python_sdktypepy"></a>

Returns results with a Tweet ID less than (that is, older than) the specified ID.

##### next_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="next_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

##### granularity: `str`<a id="granularity-str"></a>

The granularity for the search counts results.

##### search_count_fields: List[`str`]<a id="search_count_fields-liststr"></a>

A comma separated list of SearchCount fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsCountsRecentResponse`](./x_python_sdk/pydantic/get2_tweets_counts_recent_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/counts/recent` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_recent_tweets`<a id="xtweetsget_recent_tweets"></a>

Returns Tweets from the last 7 days that match a search query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_recent_tweets_response = x.tweets.get_recent_tweets(
    query="(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet",
    start_time="1970-01-01T00:00:00.00Z",
    end_time="1970-01-01T00:00:00.00Z",
    since_id="1346889436626259968",
    until_id="1346889436626259968",
    max_results=10,
    next_token="a",
    pagination_token="a",
    sort_order="recency",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).

##### since_id: [`TweetId`](./x_python_sdk/type/.py)<a id="since_id-tweetidx_python_sdktypepy"></a>

Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.

##### until_id: [`TweetId`](./x_python_sdk/type/.py)<a id="until_id-tweetidx_python_sdktypepy"></a>

Returns results with a Tweet ID less than (that is, older than) the specified ID.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of search results to be returned by a request.

##### next_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="next_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

##### sort_order: `str`<a id="sort_order-str"></a>

This order in which to return results.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsSearchRecentResponse`](./x_python_sdk/pydantic/get2_tweets_search_recent_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/search/recent` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_tweet_counts`<a id="xtweetsget_tweet_counts"></a>

Returns Tweet Counts that match a search query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tweet_counts_response = x.tweets.get_tweet_counts(
    query="(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet",
    start_time="1970-01-01T00:00:00.00Z",
    end_time="1970-01-01T00:00:00.00Z",
    since_id="1346889436626259968",
    until_id="1346889436626259968",
    next_token="a",
    pagination_token="a",
    granularity="hour",
    search_count_fields=["end", "start", "tweet_count"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp (from most recent 7 days) from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).

##### since_id: [`TweetId`](./x_python_sdk/type/.py)<a id="since_id-tweetidx_python_sdktypepy"></a>

Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.

##### until_id: [`TweetId`](./x_python_sdk/type/.py)<a id="until_id-tweetidx_python_sdktypepy"></a>

Returns results with a Tweet ID less than (that is, older than) the specified ID.

##### next_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="next_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

##### granularity: `str`<a id="granularity-str"></a>

The granularity for the search counts results.

##### search_count_fields: List[`str`]<a id="search_count_fields-liststr"></a>

A comma separated list of SearchCount fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsCountsAllResponse`](./x_python_sdk/pydantic/get2_tweets_counts_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/counts/all` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_tweets`<a id="xtweetsget_tweets"></a>

Retrieves Tweets shared in the specified Space.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tweets_response = x.tweets.get_tweets(
    id="1YqKDqWqdPLsV",
    max_results=25,
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the Space to be retrieved.

##### max_results: `int`<a id="max_results-int"></a>

The number of Tweets to fetch from the provided space. If not provided, the value will default to the maximum of 100.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2SpacesIdTweetsResponse`](./x_python_sdk/pydantic/get2_spaces_id_tweets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/spaces/{id}/tweets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.get_user_home_timeline`<a id="xtweetsget_user_home_timeline"></a>

Returns Tweet objects that appears in the provided User ID's home timeline

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_home_timeline_response = x.tweets.get_user_home_timeline(
    id="2244994945",
    since_id="791775337160081409",
    until_id="1346889436626259968",
    max_results=1,
    pagination_token="a",
    exclude=["replies", "retweets"],
    start_time="2021-02-01T18:40:40.000Z",
    end_time="2021-02-14T18:40:40.000Z",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User to list Reverse Chronological Timeline Tweets of.

##### since_id: [`TweetId`](./x_python_sdk/type/.py)<a id="since_id-tweetidx_python_sdktypepy"></a>

The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.

##### until_id: [`TweetId`](./x_python_sdk/type/.py)<a id="until_id-tweetidx_python_sdktypepy"></a>

The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results.

##### exclude: List[`str`]<a id="exclude-liststr"></a>

The set of entities to exclude (e.g. 'replies' or 'retweets').

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdTimelinesReverseChronologicalResponse`](./x_python_sdk/pydantic/get2_users_id_timelines_reverse_chronological_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/timelines/reverse_chronological` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.hide_reply`<a id="xtweetshide_reply"></a>

Hides or unhides a reply to an owned conversation.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
hide_reply_response = x.tweets.hide_reply(
    hidden=True,
    tweet_id="1346889436626259968",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### hidden: `bool`<a id="hidden-bool"></a>

##### tweet_id: [`TweetId`](./x_python_sdk/type/.py)<a id="tweet_id-tweetidx_python_sdktypepy"></a>

The ID of the reply that you want to hide or unhide.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TweetHideRequest`](./x_python_sdk/type/tweet_hide_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TweetHideResponse`](./x_python_sdk/pydantic/tweet_hide_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/{tweet_id}/hidden` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.like_tweet`<a id="xtweetslike_tweet"></a>

Causes the User (in the path) to like the specified Tweet. The User in the path must match the User context authorizing the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
like_tweet_response = x.tweets.like_tweet(
    tweet_id="1346889436626259968",
    id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tweet_id: [`TweetId`](./x_python_sdk/type/tweet_id.py)<a id="tweet_id-tweetidx_python_sdktypetweet_idpy"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that is requesting to like the Tweet.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersLikesCreateRequest`](./x_python_sdk/type/users_likes_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersLikesCreateResponse`](./x_python_sdk/pydantic/users_likes_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/likes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.list_by_list_id`<a id="xtweetslist_by_list_id"></a>

Returns a list of Tweets associated with the provided List ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_list_id_response = x.tweets.list_by_list_id(
    id="1146654567674912769",
    max_results=100,
    pagination_token="a",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`ListId`](./x_python_sdk/type/.py)<a id="id-listidx_python_sdktypepy"></a>

The ID of the List.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2ListsIdTweetsResponse`](./x_python_sdk/pydantic/get2_lists_id_tweets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/lists/{id}/tweets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.list_by_user_id`<a id="xtweetslist_by_user_id"></a>

Returns a list of Tweets authored by the provided User ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_by_user_id_response = x.tweets.list_by_user_id(
    id="2244994945",
    since_id="791775337160081409",
    until_id="1346889436626259968",
    max_results=5,
    pagination_token="a",
    exclude=["replies", "retweets"],
    start_time="2021-02-01T18:40:40.000Z",
    end_time="2021-02-14T18:40:40.000Z",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`UserId`](./x_python_sdk/type/.py)<a id="id-useridx_python_sdktypepy"></a>

The ID of the User to lookup.

##### since_id: [`TweetId`](./x_python_sdk/type/.py)<a id="since_id-tweetidx_python_sdktypepy"></a>

The minimum Tweet ID to be included in the result set. This parameter takes precedence over start_time if both are specified.

##### until_id: [`TweetId`](./x_python_sdk/type/.py)<a id="until_id-tweetidx_python_sdktypepy"></a>

The maximum Tweet ID to be included in the result set. This parameter takes precedence over end_time if both are specified.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results.

##### exclude: List[`str`]<a id="exclude-liststr"></a>

The set of entities to exclude (e.g. 'replies' or 'retweets').

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp from which the Tweets will be provided. The since_id parameter takes precedence if it is also specified.

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided. The until_id parameter takes precedence if it is also specified.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdTweetsResponse`](./x_python_sdk/pydantic/get2_users_id_tweets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/tweets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.lookup_by_id`<a id="xtweetslookup_by_id"></a>

Returns a variety of information about the Tweet specified by the requested ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_by_id_response = x.tweets.lookup_by_id(
    id="1346889436626259968",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`TweetId`](./x_python_sdk/type/.py)<a id="id-tweetidx_python_sdktypepy"></a>

A single Tweet ID.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsIdResponse`](./x_python_sdk/pydantic/get2_tweets_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.lookup_by_tweet_ids`<a id="xtweetslookup_by_tweet_ids"></a>

Returns a variety of information about the Tweet specified by the requested ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_by_tweet_ids_response = x.tweets.lookup_by_tweet_ids(
    ids=["1346889436626259968"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: List[`TweetId`]<a id="ids-listtweetid"></a>

A comma separated list of Tweet IDs. Up to 100 are allowed in a single request.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsResponse`](./x_python_sdk/pydantic/get2_tweets_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.retweet_tweet_by_id`<a id="xtweetsretweet_tweet_by_id"></a>

Causes the User (in the path) to retweet the specified Tweet. The User in the path must match the User context authorizing the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
retweet_tweet_by_id_response = x.tweets.retweet_tweet_by_id(
    tweet_id="1346889436626259968",
    id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tweet_id: [`TweetId`](./x_python_sdk/type/tweet_id.py)<a id="tweet_id-tweetidx_python_sdktypetweet_idpy"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that is requesting to retweet the Tweet.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersRetweetsCreateRequest`](./x_python_sdk/type/users_retweets_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersRetweetsCreateResponse`](./x_python_sdk/pydantic/users_retweets_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/retweets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.search_all`<a id="xtweetssearch_all"></a>

Returns Tweets that match a search query.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_all_response = x.tweets.search_all(
    query="(from:TwitterDev OR from:TwitterAPI) has:media -is:retweet",
    start_time="1970-01-01T00:00:00.00Z",
    end_time="1970-01-01T00:00:00.00Z",
    since_id="1346889436626259968",
    until_id="1346889436626259968",
    max_results=10,
    next_token="a",
    pagination_token="a",
    sort_order="recency",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

One query/rule/filter for matching Tweets. Refer to https://t.co/rulelength to identify the max query length.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The oldest UTC timestamp from which the Tweets will be provided. Timestamp is in second granularity and is inclusive (i.e. 12:00:01 includes the first second of the minute).

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The newest, most recent UTC timestamp to which the Tweets will be provided. Timestamp is in second granularity and is exclusive (i.e. 12:00:01 excludes the first second of the minute).

##### since_id: [`TweetId`](./x_python_sdk/type/.py)<a id="since_id-tweetidx_python_sdktypepy"></a>

Returns results with a Tweet ID greater than (that is, more recent than) the specified ID.

##### until_id: [`TweetId`](./x_python_sdk/type/.py)<a id="until_id-tweetidx_python_sdktypepy"></a>

Returns results with a Tweet ID less than (that is, older than) the specified ID.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of search results to be returned by a request.

##### next_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="next_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results. The value used with the parameter is pulled directly from the response provided by the API, and should not be modified.

##### sort_order: `str`<a id="sort_order-str"></a>

This order in which to return results.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsSearchAllResponse`](./x_python_sdk/pydantic/get2_tweets_search_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/search/all` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.search_stream_rules`<a id="xtweetssearch_stream_rules"></a>

Returns rules from a User's active rule set. Users can fetch all of their rules or a subset, specified by the provided rule ids.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_stream_rules_response = x.tweets.search_stream_rules(
    ids=["4807288800152802"],
    max_results=1000,
    pagination_token="aaaaaaaaaaaaaaaa",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: List[`RuleId`]<a id="ids-listruleid"></a>

A comma-separated list of Rule IDs.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: `str`<a id="pagination_token-str"></a>

This value is populated by passing the 'next_token' returned in a request to paginate through results.

#### 🔄 Return<a id="🔄-return"></a>

[`RulesLookupResponse`](./x_python_sdk/pydantic/rules_lookup_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/search/stream/rules` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.stream_sample`<a id="xtweetsstream_sample"></a>

Streams a deterministic 1% of public Tweets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
stream_sample_response = x.tweets.stream_sample(
    backfill_minutes=0,
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### backfill_minutes: `int`<a id="backfill_minutes-int"></a>

The number of minutes of backfill requested.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`StreamingTweetResponse`](./x_python_sdk/pydantic/streaming_tweet_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/sample/stream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.stream_sample10`<a id="xtweetsstream_sample10"></a>

Streams a deterministic 10% of public Tweets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
stream_sample10_response = x.tweets.stream_sample10(
    partition=1,
    backfill_minutes=0,
    start_time="2021-02-14T18:40:40.000Z",
    end_time="2021-02-14T18:40:40.000Z",
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
    expansions=[
        "attachments.media_keys",
        "attachments.poll_ids",
        "author_id",
        "edit_history_tweet_ids",
        "entities.mentions.username",
        "geo.place_id",
        "in_reply_to_user_id",
        "referenced_tweets.id",
        "referenced_tweets.id.author_id",
    ],
    media_fields=[
        "alt_text",
        "duration_ms",
        "height",
        "media_key",
        "non_public_metrics",
        "organic_metrics",
        "preview_image_url",
        "promoted_metrics",
        "public_metrics",
        "type",
        "url",
        "variants",
        "width",
    ],
    poll_fields=["duration_minutes", "end_datetime", "id", "options", "voting_status"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    place_fields=[
        "contained_within",
        "country",
        "country_code",
        "full_name",
        "geo",
        "id",
        "name",
        "place_type",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### partition: `int`<a id="partition-int"></a>

The partition number.

##### backfill_minutes: `int`<a id="backfill_minutes-int"></a>

The number of minutes of backfill requested.

##### start_time: `datetime`<a id="start_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The earliest UTC timestamp to which the Tweets will be provided.

##### end_time: `datetime`<a id="end_time-datetime"></a>

YYYY-MM-DDTHH:mm:ssZ. The latest UTC timestamp to which the Tweets will be provided.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### media_fields: List[`str`]<a id="media_fields-liststr"></a>

A comma separated list of Media fields to display.

##### poll_fields: List[`str`]<a id="poll_fields-liststr"></a>

A comma separated list of Poll fields to display.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### place_fields: List[`str`]<a id="place_fields-liststr"></a>

A comma separated list of Place fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsSample10StreamResponse`](./x_python_sdk/pydantic/get2_tweets_sample10_stream_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/sample10/stream` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.unlike_tweet_by_id`<a id="xtweetsunlike_tweet_by_id"></a>

Causes the User (in the path) to unlike the specified Tweet. The User must match the User context authorizing the request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unlike_tweet_by_id_response = x.tweets.unlike_tweet_by_id(
    id="2244994945",
    tweet_id="1346889436626259968",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that is requesting to unlike the Tweet.

##### tweet_id: [`TweetId`](./x_python_sdk/type/.py)<a id="tweet_id-tweetidx_python_sdktypepy"></a>

The ID of the Tweet that the User is requesting to unlike.

#### 🔄 Return<a id="🔄-return"></a>

[`UsersLikesDeleteResponse`](./x_python_sdk/pydantic/users_likes_delete_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/likes/{tweet_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.tweets.unretweet_by_id`<a id="xtweetsunretweet_by_id"></a>

Causes the User (in the path) to unretweet the specified Tweet. The User must match the User context authorizing the request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unretweet_by_id_response = x.tweets.unretweet_by_id(
    id="2244994945",
    source_tweet_id="1346889436626259968",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that is requesting to retweet the Tweet.

##### source_tweet_id: [`TweetId`](./x_python_sdk/type/.py)<a id="source_tweet_id-tweetidx_python_sdktypepy"></a>

The ID of the Tweet that the User is requesting to unretweet.

#### 🔄 Return<a id="🔄-return"></a>

[`UsersRetweetsDeleteResponse`](./x_python_sdk/pydantic/users_retweets_delete_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/retweets/{source_tweet_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.block_user_by_id`<a id="xusersblock_user_by_id"></a>

Causes the User (in the path) to block the target User. The User (in the path) must match the User context authorizing the request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
block_user_by_id_response = x.users.block_user_by_id(
    target_user_id="2244994945",
    id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### target_user_id: [`UserId`](./x_python_sdk/type/user_id.py)<a id="target_user_id-useridx_python_sdktypeuser_idpy"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that is requesting to block the target User.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BlockUserRequest`](./x_python_sdk/type/block_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BlockUserMutationResponse`](./x_python_sdk/pydantic/block_user_mutation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/blocking` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.follow_user`<a id="xusersfollow_user"></a>

Causes the User(in the path) to follow, or “request to follow” for protected Users, the target User. The User(in the path) must match the User context authorizing the request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
follow_user_response = x.users.follow_user(
    target_user_id="2244994945",
    id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### target_user_id: [`UserId`](./x_python_sdk/type/user_id.py)<a id="target_user_id-useridx_python_sdktypeuser_idpy"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that is requesting to follow the target User.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersFollowingCreateRequest`](./x_python_sdk/type/users_following_create_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UsersFollowingCreateResponse`](./x_python_sdk/pydantic/users_following_create_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/following` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.get_blocked_users`<a id="xusersget_blocked_users"></a>

Returns a list of Users that are blocked by the provided User ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_blocked_users_response = x.users.get_blocked_users(
    id="2244994945",
    max_results=1,
    pagination_token="aaaaaaaaaaaaaaaa",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User for whom to return results.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken32`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken32x_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdBlockingResponse`](./x_python_sdk/pydantic/get2_users_id_blocking_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/blocking` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.get_followers_by_id`<a id="xusersget_followers_by_id"></a>

Returns a list of Users who are followers of the specified User ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followers_by_id_response = x.users.get_followers_by_id(
    id="2244994945",
    max_results=1,
    pagination_token="aaaaaaaaaaaaaaaa",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`UserId`](./x_python_sdk/type/.py)<a id="id-useridx_python_sdktypepy"></a>

The ID of the User to lookup.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken32`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken32x_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdFollowersResponse`](./x_python_sdk/pydantic/get2_users_id_followers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/followers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.get_followers_by_list_id`<a id="xusersget_followers_by_list_id"></a>

Returns a list of Users that follow a List by the provided List ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_followers_by_list_id_response = x.users.get_followers_by_list_id(
    id="1146654567674912769",
    max_results=100,
    pagination_token="a",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`ListId`](./x_python_sdk/type/.py)<a id="id-listidx_python_sdktypepy"></a>

The ID of the List.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationTokenLong`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtokenlongx_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2ListsIdFollowersResponse`](./x_python_sdk/pydantic/get2_lists_id_followers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/lists/{id}/followers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.get_following_users`<a id="xusersget_following_users"></a>

Returns a list of Users that are being followed by the provided User ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_following_users_response = x.users.get_following_users(
    id="2244994945",
    max_results=1,
    pagination_token="aaaaaaaaaaaaaaaa",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`UserId`](./x_python_sdk/type/.py)<a id="id-useridx_python_sdktypepy"></a>

The ID of the User to lookup.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken32`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken32x_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdFollowingResponse`](./x_python_sdk/pydantic/get2_users_id_following_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/following` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.get_members_by_list_id`<a id="xusersget_members_by_list_id"></a>

Returns a list of Users that are members of a List by the provided List ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_members_by_list_id_response = x.users.get_members_by_list_id(
    id="1146654567674912769",
    max_results=100,
    pagination_token="a",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`ListId`](./x_python_sdk/type/.py)<a id="id-listidx_python_sdktypepy"></a>

The ID of the List.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationTokenLong`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtokenlongx_python_sdktypepy"></a>

This parameter is used to get a specified 'page' of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2ListsIdMembersResponse`](./x_python_sdk/pydantic/get2_lists_id_members_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/lists/{id}/members` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.get_muted_users_by_id`<a id="xusersget_muted_users_by_id"></a>

Returns a list of Users that are muted by the provided User ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_muted_users_by_id_response = x.users.get_muted_users_by_id(
    id="2244994945",
    max_results=100,
    pagination_token="a",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User for whom to return results.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationTokenLong`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtokenlongx_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdMutingResponse`](./x_python_sdk/pydantic/get2_users_id_muting_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/muting` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.get_retweeted_by_tweet_id_users`<a id="xusersget_retweeted_by_tweet_id_users"></a>

Returns a list of Users that have retweeted the provided Tweet ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_retweeted_by_tweet_id_users_response = x.users.get_retweeted_by_tweet_id_users(
    id="1346889436626259968",
    max_results=100,
    pagination_token="a",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`TweetId`](./x_python_sdk/type/.py)<a id="id-tweetidx_python_sdktypepy"></a>

A single Tweet ID.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsIdRetweetedByResponse`](./x_python_sdk/pydantic/get2_tweets_id_retweeted_by_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/{id}/retweeted_by` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.list_liking_users`<a id="xuserslist_liking_users"></a>

Returns a list of Users that have liked the provided Tweet ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_liking_users_response = x.users.list_liking_users(
    id="1346889436626259968",
    max_results=100,
    pagination_token="a",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`TweetId`](./x_python_sdk/type/.py)<a id="id-tweetidx_python_sdktypepy"></a>

A single Tweet ID.

##### max_results: `int`<a id="max_results-int"></a>

The maximum number of results.

##### pagination_token: [`PaginationToken36`](./x_python_sdk/type/.py)<a id="pagination_token-paginationtoken36x_python_sdktypepy"></a>

This parameter is used to get the next 'page' of results.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2TweetsIdLikingUsersResponse`](./x_python_sdk/pydantic/get2_tweets_id_liking_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/tweets/{id}/liking_users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.lookup_by_id`<a id="xuserslookup_by_id"></a>

This endpoint returns information about a User. Specify User by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_by_id_response = x.users.lookup_by_id(
    id="2244994945",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: [`UserId`](./x_python_sdk/type/.py)<a id="id-useridx_python_sdktypepy"></a>

The ID of the User to lookup.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersIdResponse`](./x_python_sdk/pydantic/get2_users_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.lookup_by_ids`<a id="xuserslookup_by_ids"></a>

This endpoint returns information about Users. Specify Users by their ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_by_ids_response = x.users.lookup_by_ids(
    ids=["2244994945,6253282,12"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: List[`UserId`]<a id="ids-listuserid"></a>

A list of User IDs, comma-separated. You can specify up to 100 IDs.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersResponse`](./x_python_sdk/pydantic/get2_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.lookup_by_username`<a id="xuserslookup_by_username"></a>

This endpoint returns information about a User. Specify User by username.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_by_username_response = x.users.lookup_by_username(
    username="TwitterDev",
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

A username.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersByUsernameUsernameResponse`](./x_python_sdk/pydantic/get2_users_by_username_username_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/by/username/{username}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.lookup_by_usernames`<a id="xuserslookup_by_usernames"></a>

This endpoint returns information about Users. Specify Users by their username.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_by_usernames_response = x.users.lookup_by_usernames(
    usernames=["TwitterDev,TwitterAPI"],
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### usernames: List[`str`]<a id="usernames-liststr"></a>

A list of usernames, comma-separated.

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersByResponse`](./x_python_sdk/pydantic/get2_users_by_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/by` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.lookup_me`<a id="xuserslookup_me"></a>

This endpoint returns information about the requesting User.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
lookup_me_response = x.users.lookup_me(
    user_fields=[
        "created_at",
        "description",
        "entities",
        "id",
        "location",
        "name",
        "pinned_tweet_id",
        "profile_image_url",
        "protected",
        "public_metrics",
        "url",
        "username",
        "verified",
        "verified_type",
        "withheld",
    ],
    expansions=["pinned_tweet_id"],
    tweet_fields=[
        "attachments",
        "author_id",
        "context_annotations",
        "conversation_id",
        "created_at",
        "edit_controls",
        "edit_history_tweet_ids",
        "entities",
        "geo",
        "id",
        "in_reply_to_user_id",
        "lang",
        "non_public_metrics",
        "organic_metrics",
        "possibly_sensitive",
        "promoted_metrics",
        "public_metrics",
        "referenced_tweets",
        "reply_settings",
        "source",
        "text",
        "withheld",
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_fields: List[`str`]<a id="user_fields-liststr"></a>

A comma separated list of User fields to display.

##### expansions: List[`str`]<a id="expansions-liststr"></a>

A comma separated list of fields to expand.

##### tweet_fields: List[`str`]<a id="tweet_fields-liststr"></a>

A comma separated list of Tweet fields to display.

#### 🔄 Return<a id="🔄-return"></a>

[`Get2UsersMeResponse`](./x_python_sdk/pydantic/get2_users_me_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/me` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.mute_user_by_id`<a id="xusersmute_user_by_id"></a>

Causes the User (in the path) to mute the target User. The User (in the path) must match the User context authorizing the request.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
mute_user_by_id_response = x.users.mute_user_by_id(
    target_user_id="2244994945",
    id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### target_user_id: [`UserId`](./x_python_sdk/type/user_id.py)<a id="target_user_id-useridx_python_sdktypeuser_idpy"></a>

##### id: `str`<a id="id-str"></a>

The ID of the authenticated source User that is requesting to mute the target User.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MuteUserRequest`](./x_python_sdk/type/mute_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MuteUserMutationResponse`](./x_python_sdk/pydantic/mute_user_mutation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{id}/muting` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.unblock_user_by_id`<a id="xusersunblock_user_by_id"></a>

Causes the source User to unblock the target User. The source User must match the User context authorizing the request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unblock_user_by_id_response = x.users.unblock_user_by_id(
    source_user_id="2244994945",
    target_user_id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### source_user_id: `str`<a id="source_user_id-str"></a>

The ID of the authenticated source User that is requesting to unblock the target User.

##### target_user_id: [`UserId`](./x_python_sdk/type/.py)<a id="target_user_id-useridx_python_sdktypepy"></a>

The ID of the User that the source User is requesting to unblock.

#### 🔄 Return<a id="🔄-return"></a>

[`BlockUserMutationResponse`](./x_python_sdk/pydantic/block_user_mutation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{source_user_id}/blocking/{target_user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.unfollow_user`<a id="xusersunfollow_user"></a>

Causes the source User to unfollow the target User. The source User must match the User context authorizing the request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unfollow_user_response = x.users.unfollow_user(
    source_user_id="2244994945",
    target_user_id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### source_user_id: `str`<a id="source_user_id-str"></a>

The ID of the authenticated source User that is requesting to unfollow the target User.

##### target_user_id: [`UserId`](./x_python_sdk/type/.py)<a id="target_user_id-useridx_python_sdktypepy"></a>

The ID of the User that the source User is requesting to unfollow.

#### 🔄 Return<a id="🔄-return"></a>

[`UsersFollowingDeleteResponse`](./x_python_sdk/pydantic/users_following_delete_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{source_user_id}/following/{target_user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `x.users.unmute_by_user_id`<a id="xusersunmute_by_user_id"></a>

Causes the source User to unmute the target User. The source User must match the User context authorizing the request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
unmute_by_user_id_response = x.users.unmute_by_user_id(
    source_user_id="2244994945",
    target_user_id="2244994945",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### source_user_id: `str`<a id="source_user_id-str"></a>

The ID of the authenticated source User that is requesting to unmute the target User.

##### target_user_id: [`UserId`](./x_python_sdk/type/.py)<a id="target_user_id-useridx_python_sdktypepy"></a>

The ID of the User that the source User is requesting to unmute.

#### 🔄 Return<a id="🔄-return"></a>

[`MuteUserMutationResponse`](./x_python_sdk/pydantic/mute_user_mutation_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/2/users/{source_user_id}/muting/{target_user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
