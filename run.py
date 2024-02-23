import os
from dotenv import load_dotenv
import socket
import requests
import asyncio

import uvicorn

load_dotenv()
PORT = os.environ.get('PORT')
URL = os.environ.get('URL')

IPAddr: str


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip


IPAddr = get_ip()


if __name__ == '__main__':
    try:
        requests.post(URL, json={
            'ip': IPAddr,
            'port': PORT
        })
        print(f"\33[32mINFO\33[0m:     IP and PORT were sent to \33[1m{URL}\33[0m")
    except Exception as e:
        print(f"\33[31mERROR\33[0m:    request was not accepted by \33[1m{URL}\33[0m")

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    uvicorn.run(
        "src:app",
        host=IPAddr,
        port=int(PORT),
        reload=False,
        ssl_keyfile='key.pem',
        ssl_certfile='cert.pem'
    )

    input('\33[5mPress ENTER to exit\33[0m')
