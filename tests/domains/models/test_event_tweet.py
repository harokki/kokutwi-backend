import pytest

from analysis_tweet.domains.models.event_tweet import EventTweet


def test_initialize_event_tweet():
    event_tweet = EventTweet("aaaa")

    assert event_tweet.tweet == "aaaa"