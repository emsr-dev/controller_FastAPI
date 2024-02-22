import os
from dotenv import load_dotenv
import socket
import requests

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

# TODO: fix ConnectionResetError or catch it
if __name__ == '__main__':
    try:
        requests.post(URL, json={'ip': IPAddr})
        print(f"IP sent to {URL}")
    except Exception as e:
        print(e)

    uvicorn.run(
        "src:app",
        host=IPAddr,
        port=int(PORT),
        reload=False,
        ssl_keyfile='key.pem',
        ssl_certfile='cert.pem'
    )
