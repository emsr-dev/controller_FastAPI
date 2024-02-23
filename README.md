# Getting Started
## Start Server
- install requirements
```commandline
pip install -r requirements.txt
```
- create the ssl certificate and key with bash
```bash
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj '/CN=issuer'
```
- create .env and change attributes accordingly
```dotenv
# port that will be opened
PORT=" "
# url where the host IP should be sent to
URL=" "
```
- run via commandline
```commandline
python run.py
```
---
## DOCS
> for documentation start the server and go to <span style="color:lightblue">**/docs**</span>
