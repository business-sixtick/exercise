# app.py
# pip install flask
# Installing collected packages: MarkupSafe, itsdangerous, click, blinker, Werkzeug, Jinja2, flask
from flask import Flask, render_template
import os
import socket

def is_port_in_use(port, host='127.0.0.1'):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex((host, port))
        return result == 0  # 포트가 열려 있으면 0을 반환

port = 8088
if is_port_in_use(port):
    print(f"포트 {port}는 사용 중입니다.")
else:
    print(f"포트 {port}는 비어 있습니다.")


# 현재 실행 중인 파일의 절대 경로를 얻습니다.
current_file_path = os.path.abspath(__file__)

# 파일의 디렉토리 경로를 얻습니다.
current_dir = os.path.dirname(current_file_path)

print("현재 파일의 경로:", current_file_path)
print("현재 파일의 디렉토리:", current_dir)

#Flask 객체 인스턴스 생성
app = Flask(__name__)
@app.route('/') # 접속하는 url
def index():
  content = '<h1>hello world</h1>'
  return content # 들어오네?
  return render_template('.\index.html')

if __name__=="__main__":
  app.run(host="127.0.0.1", port=port ,debug=True) # 디버그가 켜져 있으면 자동으로 리로드 한다.
  # host 등을 직접 지정하고 싶다면
  # app.run(host="127.0.0.1", port="5000", debug=True)
