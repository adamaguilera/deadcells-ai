from pynput.mouse import Listener

def is_clicked(x, y, button, pressed):
    if pressed:
        print('Clicked ! ')  # in your case, you can move it to some other pos
        # return False  # to stop the thread after click


with Listener(on_click=is_clicked) as listener:
    listener.join()