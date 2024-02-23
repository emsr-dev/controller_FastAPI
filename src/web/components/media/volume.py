import json

from fastapi import APIRouter
from src.controllers.media.volume import *

volume_router = APIRouter(prefix='/media')


# volume
@volume_router.get('/volume')
def volume_get():
    return get_volume_json()


@volume_router.post('/volume')
def volume_post(volume: int):
    return post_volume(volume)


# volume up
@volume_router.get('/volume/up')
def get():
    return get_volume_json()


@volume_router.post('/volume/up')
def post():
    return post_volume(int(get_volume_json()['volume'])+1)


# volume down
@volume_router.get('/volume/down')
def get():
    return get_volume_json()


@volume_router.post('/volume/down')
def post():
    return post_volume(int(get_volume_json()['volume'])-1)


# change volume and json data
def post_volume(new_volume_level):
    if new_volume_level < 0:
        new_volume_level = 0
    elif new_volume_level > 100:
        new_volume_level = 100

    change_volume(new_volume_level)

    with open('data.json', 'r') as f:
        data = json.load(f)

    data['volume'] = str(new_volume_level)

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

    return get_volume_json()


def get_volume_json():
    with open('data.json', 'r') as f:
        data = json.load(f)

    return {
        'volume': data['volume'],
        'success': True
    }
