import connection as cnect
import reddit_api_fondler as r_a_f
import config as c_ 
import threading
import time
import queue


class Botty:

    def __init__(self):
        self.q_in = queue.Queue()
        self.q_out = queue.Queue()
        self.choc_digest = []
        self.dump_time = time.time()


    def connect(self):
        cnect.connection.establish_connection()

    def you_pass_butter(self):
        while True:
            time.sleep(30)
            for item_tuple in r_a_f.scraper.get_new_subs():
                list(item_tuple)
                if len(item_tuple[0]) > 53:
                    tuple_replace = list(item_tuple[0])
                    tuple_replace = ((''.join(tuple_replace[:48]) + '[...]'), item_tuple[1])
                    self.choc_digest.append(tuple_replace)
                else:
                    self.choc_digest.append(item_tuple)
                print(item_tuple)
            if time.time() - self.dump_time > 1800:
                self.dump_time = time.time()
                for item_tuple in self.choc_digest:
                    cnect.connection.send('PRIVMSG {}'.format(c_.bot_config.channel), 
                                        ' :\x01ACTION "' + item_tuple[0] + '"', 
                                        'http://redd.it/' + item_tuple[1] + ' \x01')
                    self.choc_digest = []
            


if __name__ == "__main__":
    botty = Botty()
    botty.connect()
    t1 = threading.Thread(target=cnect.connection.ping_broda)
    t1.start()
    time.sleep(20)
    t2 = threading.Thread(target=botty.you_pass_butter)
    t2.start()