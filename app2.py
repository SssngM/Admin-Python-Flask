from flask import Flask,  jsonify ,json , request, Response 
import random, json
# from models import  json , request, Response , random

app = Flask(__name__)



#토큰 예시
token = "dgfat12gf45ag" 

#random str 가져올경우
random_string = ''.join(random.choice(token) for i in range(5))

#file 경우
file_path = "./users.json"


@app.route("/header" , methods=['POST'])
def create_token():
#토큰 발행 
#   return jsonify({'token':token})

#random으로 발행 
    # random_string = ''.join(random.choice(token) for i in range(5))
    return jsonify({'token':random_string})

# file 발행
    # with open('users.json','r') as f:
    #     data = json.load(f)
    # return jsonify({'token':data})



# 토큰 확인
@app.route("/test", methods=['GET'])
def test_token():
    # header_token = request.headers.get('token')

    # 랜덤
    header_token = request.headers.get('random_string') 

    # 파일
    # header_token = request.headers.get('data')

    if header_token != token:
        return Response(json.dumps({'error msg' : ' need valid token'}), 401)

    return Response(json.dumps({'error msg': ' valid token! '}), 200)






if __name__ == '__main__':
    app.run(debug=True, port=5000)
