from fastapi import APIRouter
from src.controllers.media.play import *

play_router = APIRouter(prefix='/media')


@play_router.get('/play')
def play_get():
    return {'success': True}


@play_router.post('/play')
def play_post():
    message = play_pause()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/pause')
def pause_get():
    return {'success': True}


@play_router.post('/pause')
def pause_post():
    message = play_pause()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/next')
def next_get():
    return {'success': True}


@play_router.post('/next')
def next_post():
    message = next_track()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/prev')
def prev_get():
    return {'success': True}


@play_router.post('/prev')
def prev_post():
    message = prev_track()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/left')
def left_get():
    return {'success': True}


@play_router.post('/left')
def left_post():
    message = left()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/right')
def right_get():
    return {'success': True}


@play_router.post('/right')
def right_post():
    message = right()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/up')
def up_get():
    return {'success': True}


@play_router.post('/up')
def up_post():
    message = up()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/down')
def down_get():
    return {'success': True}


@play_router.post('/down')
def down_post():
    message = down()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/enter')
def enter_get():
    return {'success': True}


@play_router.post('/enter')
def enter_post():
    message = enter()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/esc')
def esc_get():
    return {'success': True}


@play_router.post('/esc')
def esc_post():
    message = esc()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/full')
def full_get():
    return {'success': True}


@play_router.post('/full')
def full_post():
    message = f11()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/mute')
def mute_get():
    return {'success': True}


@play_router.post('/mute')
def mute_post():
    message = mute()
    return {
        'message': message,
        'success': True
    }
