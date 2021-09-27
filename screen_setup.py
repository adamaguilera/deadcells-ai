import time

from pynput.mouse import Controller

import keyboard_input
from conf import Config

WAIT_PERIOD = 0.5


print('Screen setup is starting...')
mouse = Controller()
config = Config()
config.load()
print(f'Press {config.get("RECORD_KEY")} to start recording mouse coordinates...')
keyboard_input.wait_until_key_pressed(config.get('RECORD_KEY'))
print('Record key hit, starting to log coordinates...')
screen = config.get('SCREEN')
result = {}
for current in screen.keys():
    print(f'Press {config.get("SELECT_KEY")} to log mouse coordinate for {current}')
    keyboard_input.wait_until_key_pressed(config.get('SELECT_KEY'))
    print(f'Logged {mouse.position} for {current}')
    result[current] = mouse.position
    time.sleep(WAIT_PERIOD)

print('Finished recording inputs for all positions!')
print('You have logged the following information:')
for position, coordinate in result.items():
    print(f'Position {position}: {coordinate}')
read = input('Would you like to save this config? (y/n): ')
print('=-=-=-=-=-=-=-=-=-=-=-=-=')
if read.lower() == 'y':
    print('Saving config...')
    config.put('SCREEN', result)
    config.save()
else:
    print('Config was not saved.')
print('Closing application...')
exit()
