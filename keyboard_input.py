import keyboard
import time

SLEEP_TIME = 0.01


def wait_until_key_pressed(key):
    keyboard.wait(key)
