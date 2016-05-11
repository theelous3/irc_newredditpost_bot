import json

class BotConfig:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

bot_json = json.load(open('config.json'))
bot_config = BotConfig(**bot_json)
