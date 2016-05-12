import praw
import time
import config as c_
from collections import OrderedDict


class RedditScraper:

    def __init__(self):
        self.raw_obj = praw.Reddit(user_agent='#{} helper by {}'.format(c_.bot_config.subreddit, 
                                                                        c_.bot_config.reddit_usrnm))
        self.last_id = ''

    def get_new_subs(self):
        raylway = 1
        for subm in self.raw_obj.get_subreddit(c_.bot_config.subreddit).get_new():
            if subm.id == self.last_id:
                break
            time_delta = time.time() - subm.created_utc
            if time_delta >= 300 and time_delta < 6000:
                if subm.score >= 1:
                    if raylway > 0:
                        self.last_id = subm.id
                        raylway -= 1
                        yield subm.url
                    else:
                        yield subm.url
        
            

scraper = RedditScraper()

