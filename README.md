# Getting Started
## Start Server
- clone repository
```commandline
git clone https://github.com/KyrenRE/controler_FastAPI.git
```
- update pip and install requirements
```commandline
pip install --upgrade pip
pip install -r requirements.txt
```
- create the ssl certificate and key in bash
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
