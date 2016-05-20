import connection as cnect
import reddit_api_fondler as r_a_f
import config as c_ 



class Botty:


    def __init__(self):
        self.choc_digest = []


    def connect(self):
        cnect.connection.establish_connection()

    def hey_listen(self):
        while True:
            for line in cnect.connection.recv():
                print(line)
                if line.split()[0] == 'PING':
                    self.ping(line.split()[1])
                try:
                    if line.split(':',2)[2].startswith(c_.bot_config.nick):
                        if c_.bot_config.phrase in line.lower():
                            self.you_pass_butter()
                        elif 'help' in line.lower():
                            self.send_help()
                        elif 'source' in line.lower():
                            self.send_source()
                    else:
                        if c_.bot_config.nick in line.split(':',2)[1] and 'VERSION' in line.split(':',2)[2]:
                            self.send_version(line.split(':',2)[1].split('!')[0])



                except IndexError:
                    continue
                
    def ping(self, response):
        cnect.connection.send('PONG ' + response)

    def send_help(self):
        cnect.connection.send('PRIVMSG {} :'.format(c_.bot_config.channel) + 'Type "{} {}" and I\'ll get the latest posts from {} :D'.format(c_.bot_config.nick,
                                                                                c_.bot_config.phrase,
                                                                                c_.bot_config.subreddit))
    def send_source(self):
        cnect.connection.send('PRIVMSG {} :'.format(c_.bot_config.channel) + 'My guts: https://github.com/theelous3/irc_newredditpost_bot')

    def send_version(self, nick):
        cnect.connection.send('NOTICE {} :'.format(nick) + 'irc_newredditpost_bot 2.1.0')

    def you_pass_butter(self):
    #   https://youtu.be/ekP0LQEsUh0?t=52
        for item_tuple in r_a_f.scraper.get_new_subs():
            if len(item_tuple[0]) > 53:
                tuple_replace = list(item_tuple[0])
                tuple_replace = ((''.join(tuple_replace[:48]) + '[...]'), item_tuple[1])
                self.choc_digest.append(tuple_replace)
            else:
                self.choc_digest.append(item_tuple)
        if self.choc_digest:
            for item_tuple in self.choc_digest:
                cnect.connection.send('PRIVMSG {}'.format(c_.bot_config.channel), 
                                    ' :\x01ACTION "' + item_tuple[0] + '"', 
                                    'http://redd.it/' + item_tuple[1] + ' \x01')
                self.choc_digest = []
        else:
            cnect.connection.send('PRIVMSG {} :'.format(c_.bot_config.channel) + 'Nothing new. Thanks for checking!')



if __name__ == "__main__":
    botty = Botty()
    botty.connect()
    botty.hey_listen()