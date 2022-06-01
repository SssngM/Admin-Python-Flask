from flask import Flask, requests, redirect, render_template, jsonify
from models import db, connect_db, Users, jsonipy, json

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_info'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)


#토큰 예시
token = "dgfat12gf45%&ag" 


@app.route("/header" , methods=['GET', 'POST'])
def create_token():
# local_token = token.json()
    # requests.get.header(token)
    header_token = {'Authorization': 'token {}'.format(token)}
    response = requests.get(headers=header_token) 
    if response.stauts_code == 401:
        return 401
    elif header_token == token:
        return 200, response.json(header_token)


file_path = "./users.json"

def non_token():
    header_token = {}
    with open('users.json','r') as f:
        data = json.load(f)
        response = requests.get(headers=data) 
    if header_token == token:
        return 200, response.json(header_token)


# def create_token():

#     response = requests.post(token)
#     if response.stauts_code == 401:
#         return 401
#     else header_token == token:
#         return 200, response.json(header_token)