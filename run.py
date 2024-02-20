import os
from dotenv import load_dotenv
import socket
import requests
import uvicorn

load_dotenv()
PORT = os.environ.get('PORT')
URL = os.environ.get('URL')

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


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
