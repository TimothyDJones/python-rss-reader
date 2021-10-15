import feedparser
from newspaper import Article
import os
import sys

DEFAULT_FEED_LIST_FILE = "feed_list.txt"



class FeedReader(object):
    def __init__():
        self.feed_list = self.get_feed_list()

    def get_feed_list(self, feed_list_file=DEFAULT_FEED_LIST_FILE):
        with open(file=feed_list_file, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
            return ([line.rstrip() for line in lines])

def main():
    fr = FeedReader()

if __name__ == "__main__":
    main()
