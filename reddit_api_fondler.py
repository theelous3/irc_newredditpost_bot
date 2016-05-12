import praw
import time
import config as c_
from collections import OrderedDict


class RedditScraper:

    def __init__(self):
        self.raw_obj = praw.Reddit(user_agent='#{} helper by {}'.format(c_.bot_config.subreddit, 
                                                                        c_.bot_config.reddit_usrnm))
        self.used_list = []

    def get_new_subs(self):
        while len(self.used_list) > 25:
            del self.used_list[-1:]
        for subm in self.raw_obj.get_subreddit(c_.bot_config.subreddit).get_new():
            time_delta = time.time() - subm.created_utc
            if time_delta >= 300 and time_delta < 3200:
                if subm.id not in self.used_list:
                    if subm.score >= 1:
                        self.used_list.insert(0, subm.id)
                        print((subm.title, subm.id))
                        yield (subm.title, subm.id) 
                else:
                    pass
            

scraper = RedditScraper()