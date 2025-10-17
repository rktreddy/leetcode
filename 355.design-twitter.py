#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
# class Twitter:

#     def __init__(self):
        

#     def postTweet(self, userId: int, tweetId: int) -> None:
        

#     def getNewsFeed(self, userId: int) -> List[int]:
        

#     def follow(self, followerId: int, followeeId: int) -> None:
        

#     def unfollow(self, followerId: int, followeeId: int) -> None:

from collections import defaultdict
from heapq import nlargest
from typing import List

class Twitter:
    def __init__(self):
        """
        Initialize your data structures here.
        """
        self.user_tweets = defaultdict(list)  # Maps user ids to their tweets (respecting the chronological order)
        self.user_following = defaultdict(set) # Maps user ids to the set of user ids they follow
        self.tweets = {}  # Maps tweet ids to timestamps
        self.timer = 0  # A timestamp to order tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose and post a new tweet.
        """
        self.timer += 1  # Increment the timer to record the time of the tweet
        self.user_tweets[userId].append(tweetId)  # Append the new tweet to the user's tweets
        self.tweets[tweetId] = self.timer  # Record the timestamp for the new tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users whom the user follows or by the user themselves.
        Tweets must be ordered from most recent to least recent.
        """
        following = self.user_following[userId]  # Get the set of user ids the current user follows
        users = following.union({userId})  # Combine with the current user to get all potential sources of tweets
        # Collect up to the 10 most recent tweets from each user
        tweets = [self.user_tweets[u][-10:][::-1] for u in users]  # Retrieve, reverse, and limit to 10 tweets
        all_tweets = sum(tweets, [])  # Flatten the list of tweets
        # Get the 10 most recent tweets among all the tweets collected, based on timestamps
        return nlargest(10, all_tweets, key=lambda tweet: self.tweets[tweet])

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_following[followerId].add(followeeId)  # Add the followee to the follower's following set

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid (e.g., not following), it should be a no-op.
        """
        if followeeId in self.user_following[followerId]:  # If the follower is actually following the followee
            self.user_following[followerId].remove(followeeId)  # Remove the followee from the set


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

