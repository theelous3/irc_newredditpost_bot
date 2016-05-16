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
        while len(self.used_list) > 30:
            del self.used_list[-1:]
        for subm in self.raw_obj.get_subreddit(c_.bot_config.subreddit).get_new():
            time_delta = time.time() - subm.created_utc
            if time_delta >= c_.bot_config.woo_o and time_delta < c_.bot_config.woo_c:
                if subm.id not in self.used_list and subm.score >= c_.bot_config.karma_score:
                    self.used_list.insert(0, subm.id)
                    yield (subm.title, subm.id)
                fuckit
            fuckit    

        print(self.used_list)
            

scraper = RedditScraper()