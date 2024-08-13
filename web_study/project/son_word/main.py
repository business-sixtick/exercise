from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import base64
import os

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

    # 이미지 데이터가 있으면 처리
    if image_data:
        # 'data:image/png;base64,' 부분 제거
        header, image_data = image_data.split(",", 1)

        # base64 데이터를 디코딩하여 파일로 저장
        image_bytes = base64.b64decode(image_data)
        with open("uploaded_image.png", "wb") as f:
            f.write(image_bytes)

        return {"message": "Image received and saved."}
    
    return {"message": "No image data received."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# uvicorn main:app --reload
