import json

RECORD_KEY = 'p'
STOP_KEY = 'o'
SELECT_KEY = 'l'
CONFIG_PATH = 'config/config.json'
TOP_LEFT_POS = (0, 0)
TOP_RIGHT_POS = (255, 255)
BOT_LEFT_POS = (0, 0)
BOT_RIGHT_POS = (255, 255)


class Config():
    def __init__(self):
        self.conf = None

    def save(self):
        print('Attempting to save config...')
        if not self.conf:
            print('Config was never loaded!')
        else:
            out_file = open(CONFIG_PATH, 'w')
            json.dump(self.conf, out_file, indent=4)
            print('Successfully saved config!')

    def load(self):
        print('Attempting to load config...')
        if self.conf:
            print('Config was already loaded!')
        else:
            print(f'Config path set to: {CONFIG_PATH}')
            config_json = open(CONFIG_PATH)
            self.conf = json.load(config_json)
            print(f'Successfully loaded config!')

    def put(self, key, value):
        print(f'Attempting to put key: {key}, value: {value}')
        if not self.conf:
            print('Config was not loaded...')
            self.load()
        self.conf[key] = value
        print(f'Successfully put key: {key}, value: {self.conf[key]}')

    def get(self, key):
        # print(f'Attempting to get {key} from config...')
        if not self.conf:
            print('Config was not loaded...')
            self.load()
        val = self.conf[key]
        # if val:
            # print(f'Got {val} from config')
        # else:
            # print(f'Error: No associated value found for key {key}')
        return val
