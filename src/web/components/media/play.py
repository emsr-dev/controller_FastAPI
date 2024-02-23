from fastapi import APIRouter
from src.controllers.media.play import *

play_router = APIRouter(prefix='/media')


@play_router.get('/play')
def get():
    return {'success': True}


@play_router.post('/play')
def post():
    message = play_pause()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/pause')
def get():
    return {'success': True}


@play_router.post('/pause')
def post():
    message = play_pause()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/next')
def get():
    return {'success': True}


@play_router.post('/next')
def post():
    message = next_track()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/prev')
def get():
    return {'success': True}


@play_router.post('/prev')
def post():
    message = prev_track()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/left')
def get():
    return {'success': True}


@play_router.post('/left')
def post():
    message = left()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/right')
def get():
    return {'success': True}


@play_router.post('/right')
def post():
    message = right()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/up')
def get():
    return {'success': True}


@play_router.post('/up')
def post():
    message = up()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/down')
def get():
    return {'success': True}


@play_router.post('/down')
def post():
    message = down()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/enter')
def get():
    return {'success': True}


@play_router.post('/enter')
def post():
    message = enter()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/esc')
def get():
    return {'success': True}


@play_router.post('/esc')
def post():
    message = esc()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/full')
def get():
    return {'success': True}


@play_router.post('/full')
def post():
    message = f11()
    return {
        'message': message,
        'success': True
    }


@play_router.get('/mute')
def get():
    return {'success': True}


@play_router.post('/mute')
def post():
    message = mute()
    return {
        'message': message,
        'success': True
    }
