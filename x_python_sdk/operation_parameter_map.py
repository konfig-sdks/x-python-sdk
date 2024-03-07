operation_parameter_map = {
    '/2/users/{id}/bookmarks-POST': {
        'parameters': [
            {
                'name': 'tweet_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/2/users/{id}/bookmarks-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/users/{id}/bookmarks/{tweet_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'tweet_id'
            },
        ]
    },
    '/2/compliance/jobs-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'name'
            },
            {
                'name': 'resumable'
            },
        ]
    },
    '/2/compliance/jobs/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'compliance_job.fields'
            },
        ]
    },
    '/2/compliance/jobs-GET': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'status'
            },
            {
                'name': 'compliance_job.fields'
            },
        ]
    },
    '/2/tweets/compliance/stream-GET': {
        'parameters': [
            {
                'name': 'partition'
            },
            {
                'name': 'backfill_minutes'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
        ]
    },
    '/2/tweets/label/stream-GET': {
        'parameters': [
            {
                'name': 'backfill_minutes'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
        ]
    },
    '/2/users/compliance/stream-GET': {
        'parameters': [
            {
                'name': 'partition'
            },
            {
                'name': 'backfill_minutes'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
        ]
    },
    '/2/dm_conversations-POST': {
        'parameters': [
            {
                'name': 'conversation_type'
            },
            {
                'name': 'message'
            },
            {
                'name': 'participant_ids'
            },
        ]
    },
    '/2/dm_conversations/with/{participant_id}/dm_events-GET': {
        'parameters': [
            {
                'name': 'participant_id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'event_types'
            },
            {
                'name': 'dm_event.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/dm_conversations/{id}/dm_events-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'event_types'
            },
            {
                'name': 'dm_event.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/dm_events-GET': {
        'parameters': [
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'event_types'
            },
            {
                'name': 'dm_event.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/dm_conversations/{dm_conversation_id}/messages-POST': {
        'parameters': [
            {
                'name': 'dm_conversation_id'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'text'
            },
        ]
    },
    '/2/dm_conversations/with/{participant_id}/messages-POST': {
        'parameters': [
            {
                'name': 'participant_id'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'text'
            },
        ]
    },
    '/2/openapi.json-GET': {
        'parameters': [
        ]
    },
    '/2/lists/{id}/members-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/2/lists-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'private'
            },
        ]
    },
    '/2/lists/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/2/users/{id}/followed_lists-POST': {
        'parameters': [
            {
                'name': 'list_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/2/users/{id}/followed_lists-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'list.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'user.fields'
            },
        ]
    },
    '/2/users/{id}/list_memberships-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'list.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'user.fields'
            },
        ]
    },
    '/2/users/{id}/owned_lists-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'list.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'user.fields'
            },
        ]
    },
    '/2/users/{id}/pinned_lists-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'list.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'user.fields'
            },
        ]
    },
    '/2/lists/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'list.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'user.fields'
            },
        ]
    },
    '/2/users/{id}/pinned_lists-POST': {
        'parameters': [
            {
                'name': 'list_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/2/lists/{id}/members/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/2/users/{id}/followed_lists/{list_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'list_id'
            },
        ]
    },
    '/2/users/{id}/pinned_lists/{list_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'list_id'
            },
        ]
    },
    '/2/lists/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'private'
            },
        ]
    },
    '/2/spaces/search-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'state'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'space.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'topic.fields'
            },
        ]
    },
    '/2/spaces/{id}/buyers-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/spaces/{id}/tweets-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/spaces/by/creator_ids-GET': {
        'parameters': [
            {
                'name': 'user_ids'
            },
            {
                'name': 'space.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'topic.fields'
            },
        ]
    },
    '/2/spaces/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'space.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'topic.fields'
            },
        ]
    },
    '/2/spaces-GET': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'space.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'topic.fields'
            },
        ]
    },
    '/2/tweets/search/stream/rules-POST': {
        'parameters': [
            {
                'name': 'add'
            },
            {
                'name': 'delete'
            },
            {
                'name': 'dry_run'
            },
        ]
    },
    '/2/tweets-POST': {
        'parameters': [
            {
                'name': 'card_uri'
            },
            {
                'name': 'direct_message_deep_link'
            },
            {
                'name': 'for_super_followers_only'
            },
            {
                'name': 'geo'
            },
            {
                'name': 'media'
            },
            {
                'name': 'nullcast'
            },
            {
                'name': 'poll'
            },
            {
                'name': 'quote_tweet_id'
            },
            {
                'name': 'reply'
            },
            {
                'name': 'reply_settings'
            },
            {
                'name': 'text'
            },
        ]
    },
    '/2/tweets/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/2/spaces/{id}/buyers-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/tweets/search/stream-GET': {
        'parameters': [
            {
                'name': 'backfill_minutes'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/tweets/firehose/stream-GET': {
        'parameters': [
            {
                'name': 'partition'
            },
            {
                'name': 'backfill_minutes'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/users/{id}/liked_tweets-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/users/{id}/mentions-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'since_id'
            },
            {
                'name': 'until_id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/tweets/{id}/quote_tweets-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'exclude'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/tweets/counts/recent-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'since_id'
            },
            {
                'name': 'until_id'
            },
            {
                'name': 'next_token'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'granularity'
            },
            {
                'name': 'search_count.fields'
            },
        ]
    },
    '/2/tweets/search/recent-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'since_id'
            },
            {
                'name': 'until_id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'next_token'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'sort_order'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/tweets/counts/all-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'since_id'
            },
            {
                'name': 'until_id'
            },
            {
                'name': 'next_token'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'granularity'
            },
            {
                'name': 'search_count.fields'
            },
        ]
    },
    '/2/spaces/{id}/tweets-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/users/{id}/timelines/reverse_chronological-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'since_id'
            },
            {
                'name': 'until_id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'exclude'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/tweets/{tweet_id}/hidden-PUT': {
        'parameters': [
            {
                'name': 'hidden'
            },
            {
                'name': 'tweet_id'
            },
        ]
    },
    '/2/users/{id}/likes-POST': {
        'parameters': [
            {
                'name': 'tweet_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/2/lists/{id}/tweets-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/users/{id}/tweets-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'since_id'
            },
            {
                'name': 'until_id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'exclude'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/tweets/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/tweets-GET': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/users/{id}/retweets-POST': {
        'parameters': [
            {
                'name': 'tweet_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/2/tweets/search/all-GET': {
        'parameters': [
            {
                'name': 'query'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'since_id'
            },
            {
                'name': 'until_id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'next_token'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'sort_order'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/tweets/search/stream/rules-GET': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
        ]
    },
    '/2/tweets/sample/stream-GET': {
        'parameters': [
            {
                'name': 'backfill_minutes'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/tweets/sample10/stream-GET': {
        'parameters': [
            {
                'name': 'partition'
            },
            {
                'name': 'backfill_minutes'
            },
            {
                'name': 'start_time'
            },
            {
                'name': 'end_time'
            },
            {
                'name': 'tweet.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'media.fields'
            },
            {
                'name': 'poll.fields'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'place.fields'
            },
        ]
    },
    '/2/users/{id}/likes/{tweet_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'tweet_id'
            },
        ]
    },
    '/2/users/{id}/retweets/{source_tweet_id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'source_tweet_id'
            },
        ]
    },
    '/2/users/{id}/blocking-POST': {
        'parameters': [
            {
                'name': 'target_user_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/2/users/{id}/following-POST': {
        'parameters': [
            {
                'name': 'target_user_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/2/users/{id}/blocking-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/users/{id}/followers-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/lists/{id}/followers-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/users/{id}/following-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/lists/{id}/members-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/users/{id}/muting-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/tweets/{id}/retweeted_by-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/tweets/{id}/liking_users-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'max_results'
            },
            {
                'name': 'pagination_token'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/users/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/users-GET': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/users/by/username/{username}-GET': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/users/by-GET': {
        'parameters': [
            {
                'name': 'usernames'
            },
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/users/me-GET': {
        'parameters': [
            {
                'name': 'user.fields'
            },
            {
                'name': 'expansions'
            },
            {
                'name': 'tweet.fields'
            },
        ]
    },
    '/2/users/{id}/muting-POST': {
        'parameters': [
            {
                'name': 'target_user_id'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/2/users/{source_user_id}/blocking/{target_user_id}-DELETE': {
        'parameters': [
            {
                'name': 'source_user_id'
            },
            {
                'name': 'target_user_id'
            },
        ]
    },
    '/2/users/{source_user_id}/following/{target_user_id}-DELETE': {
        'parameters': [
            {
                'name': 'source_user_id'
            },
            {
                'name': 'target_user_id'
            },
        ]
    },
    '/2/users/{source_user_id}/muting/{target_user_id}-DELETE': {
        'parameters': [
            {
                'name': 'source_user_id'
            },
            {
                'name': 'target_user_id'
            },
        ]
    },
};