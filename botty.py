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


    def connect(self):
        cnect.connection.establish_connection()

    def you_pass_butter(self):
        while True:
            for i in r_a_f.scraper.get_new_subs():
                cnect.connection.send('PRIVMSG {}'.format(c_.bot_config.channel), i)
            time.sleep(30)


if __name__ == "__main__":
    botty = Botty()

    t1 = threading.Thread(target=cnect.connection.ping_broda)
    t2 = threading.Thread(target=botty.you_pass_butter)

    botty.connect()
    t1.start()
    t2.start()



