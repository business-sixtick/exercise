from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import base64
import os

import struct

def parse_png(png_data):
    # PNG 파일의 시작 바이트를 확인
    if png_data[:8] != b'\x89PNG\r\n\x1a\n':
        raise ValueError("Invalid PNG file")

    offset = 8  # 시작 바이트를 건너뜀

    while offset < len(png_data):
        # 청크의 길이 (4바이트)
        length = struct.unpack('>I', png_data[offset:offset + 4])[0]
        offset += 4
        
        # 청크의 타입 (4바이트)
        chunk_type = png_data[offset:offset + 4]
        offset += 4
        
        # 청크의 데이터
        data = png_data[offset:offset + length]
        offset += length
        print(data)
        # 청크의 CRC (4바이트)
        crc = png_data[offset:offset + 4]
        offset += 4

        # IHDR 청크를 찾고 너비와 높이 출력
        if chunk_type == b'IHDR':
            width, height = struct.unpack('>II', data[:8])
            print(f"Width: {width}, Height: {height}")

# # 주어진 PNG 바이너리 데이터
# png_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x1c\x00\x00\x00\x1c\x08\x06\x00\x00\x00r\r\xdf\x94\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x01-IDATHK\xed\x95Aj\xc2@\x18\x85\xbf\xb4\xde\xa0\'\xa8t\xe9\xa2]\nB\x8f!Hw\xf5\x02=@)z\x81^\xc0.\xa5=\x86\xe0\xc6\xa5\xe2\xbaP\xba\xec\xcauA\xaa?$\x12B2\xff\x9b\xa4d\xe5l\x02\xc9\xcf\xfb\xde{\xccL\x12Z^I\xcb<\xce\xc0\x7fo<\xa6\xd2?\x87\xde\x07V\x9eC\x15h\xb0\x11\xf0\x1e\x10\xcc\x0c\x055\x15\xe07\xf0\x0b\xdcx\xee\x01\x836\x06\xba"\x82\x91\xd3\x88\x92P\xaa*Ut\xcd)@\xd3\x9a\x02\xcf\xa9\xe8\x1a\xb8+\xa4\xcaL\xd9\xf3"\x94X\x05\xe65f\xc0cA\xf4\x0b\xb8V\xaa\xad\x034\xdd,\xd1-\xb0\x01>\x80a\nl\xbci\x8a\xc6\r6\x07\x1eJ\x12\xd9\xb7=\xd0\xa9J\x1b\x93\xb0\x07l\xbdm\xef\x1d\r\x15\xd8\x05>\x05XVw\xa5\xae\nt\xb7{\xae\xc2W`w47)\xabU\x01\xde\x03\x0b1\x9d1^RPm`L:cYB[Ou\x13\xc6\x02\x83\xf3J\xa5\xad\x03\x7f\x80+\xe0R\xb8I\xcc\\\xf0\xbf\xa8$\xcc\xdf,o\xc0\xb8\xe2\xc0\xdbkW\xcf\x1d(\x88/\x81A\tP\xd6\x91\x07\x85:\xa5\x913P\xaa)f\xe8\x00\xcf3.\x1d\x9ap\x05\xde\x00\x00\x00\x00IEND\xaeB`\x82'

# parse_png(png_data)

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import Adam
from keras.datasets import mnist
from keras import utils
from PIL import Image

# MNIST 데이터셋 로드
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 데이터 전처리
x_train = x_train.reshape(60000, 784).astype('float32') / 255
x_test = x_test.reshape(10000, 784).astype('float32') / 255
y_train = utils.to_categorical(y_train, 10)
y_test = utils.to_categorical(y_test, 10)

# 모델 구축
model = Sequential()
model.add(Dense(512, input_shape=(784,)))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(Dense(10))
model.add(Activation('softmax'))

# 모델 컴파일
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# 모델 학습
hist = model.fit(x_train, y_train, epochs=5, verbose=1) # 5번
# hist = model.fit(x_train, y_train, verbose=1)

# 테스트 데이터 평가
score = model.evaluate(x_test, y_test, verbose=1)
print('loss = ', score[0])
print('accuracy = ', score[1])

# 실제 이미지 파일로 예측하기
def load_and_preprocess_image(image_path):
    # 이미지 로드
    # img = Image.open(image_path).convert('L')  # 흑백으로 변환
    # img = img.resize((28, 28))  # 크기를 28x28로 조정
    img = Image.open(image_path)
    img_array = np.array(img)  # numpy 배열로 변환 # img_array[:,:,3].reshape(1, 784) / 255
    img_array = img_array[:,:,3].astype('float32') / 255  # 정규화
    img_array = img_array.reshape(1, 784)  # 모델에 맞게 reshape
    return img_array

def predict_image(image_path):
    img_array = load_and_preprocess_image(image_path)
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)  # 가장 높은 확률을 가진 클래스
    print(f'Predicted class: {predicted_class}')
    return f'Predicted class: {predicted_class}'
    return predicted_class

# 예측할 이미지 파일 경로
# image_path = 'uploaded_image.png'  # 여기에 실제 이미지 파일 경로 입력
# predicted_class = predict_image(image_path)


app = FastAPI()

# 정적 파일(예: JavaScript, CSS 등)을 제공하는 경로 설정
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML 페이지 제공
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

# 이미지 데이터를 처리하는 POST 엔드포인트
@app.post("/upload/")
async def upload_image(request: Request):
    data = await request.json()
    image_data = data.get("image")
    # print(image_data)
    # 이미지 데이터가 있으면 처리
    if image_data:
        # 'data:image/png;base64,' 부분 제거
        header, image_data = image_data.split(",", 1)

        # base64 데이터를 디코딩하여 파일로 저장
        image_bytes = base64.b64decode(image_data)
        with open("uploaded_image.png", "wb") as f:
            f.write(image_bytes)
        # print(image_data)   
        # print(image_bytes) 
        # parse_png(image_bytes)
        ret = predict_image("uploaded_image.png")
        return {"message": ret}
    
    return {"message": "No image data received."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# uvicorn main:app --reload
# Uvicorn은 Python으로 작성된 고성능 ASGI(Asynchronous Server Gateway Interface) 서버입니다. 

#네트워크의 한계: 네트워크를 통한 데이터 전송은 대역폭과 지연(latency)에 의해 제한됩니다. 예를 들어, 대용량 파일을 전송할 때 네트워크 속도가 느리다면, 아무리 다중 프로세스를 사용해도 파일 전송이 빨라지지 않습니다. 이 경우 병목현상은 네트워크 속도 자체입니다.
# 소프트웨어로 구현된 로드 밸런서로, Nginx, HAProxy, Traefik 등이 예입니다. 클라우드 환경에서 자주 사용됩니다.
# 요청 분배 알고리즘 : 라운드 로빈(Round Robin) 최소 연결(Minimum Connections) IP 해시(IP Hash) 가중치 기반 분배(Weighted Round Robin)