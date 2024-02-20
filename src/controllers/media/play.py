import pyautogui


def play_pause():
    pyautogui.press('playpause')
    return "play/pause"


def next_track():
    pyautogui.press('nexttrack')
    return "next track"


def prev_track():
    pyautogui.press('prevtrack')
    return "previous track"


def left():
    pyautogui.press('left')
    return "arrow left"


def right():
    pyautogui.press('right')
    return "arrow right"


def up():
    pyautogui.press('up')
    return "arrow up"


def down():
    pyautogui.press('down')
    return "arrow down"


def enter():
    pyautogui.press('enter')
    return "enter"


def esc():
    pyautogui.press('esc')
    return "esc"


def f11():
    pyautogui.press('f11')
    return "f11"


def mute():
    pyautogui.press('volumemute')
    return "mute"
