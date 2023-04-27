from pynput.keyboard import Key, Controller
from autobahn import wamp

keyboard = Controller()


class Keys:

    @wamp.register('com.left.key')
    def left_key_press(self):
        keyboard.press(Key.left)
        keyboard.release(Key.left)

    @wamp.register('com.right.key')
    def right_key_press(self):
        keyboard.press(Key.right)
        keyboard.release(Key.right)
