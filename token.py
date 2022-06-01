from flask import Flask,  jsonify ,json , request, Response 
import random, json
# from models import  json , request, Response , random

app = Flask(__name__)



#토큰 예시
token = "dgfat12gf45ag" 
#file 경우
file_path = "./users.json"
#random str 가져올경우



@app.route("/header" , methods=['POST'])
def create_token():
#토큰 발행 
  # return jsonify({'token':token})

#random으로 발행 
    # random_string = [random.choice(token) for i in range(5)] 
    # return jsonify({'token':random_string})

# file 발행
    with open('users.json','r') as f:
        data = json.load(f)
    return jsonify({'token':data})



#토큰 확인
@app.routne("/test", methods=['GET'])
def test_token():
    header_token = request.headers.get('token')
    # header_token = request.headers.get('random_string')
    if header_token != token:
        return Response(json.dumps({'error msg' : ' need valid token'}), 401)

    return Response(json.dumps({'error msg': ' valid token! '}), 200)




    # with open('users.json','r') as f:
    #     data = json.load(f)
    #     response = requests.get(headers=data) 
    # if header_token == token:
    #     return 200, response.json(header_token)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
