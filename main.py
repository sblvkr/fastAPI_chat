from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/static', app=StaticFiles(directory='static'))

html = ""
with open('index.html', 'r') as f:
    html = f.read()


@app.get("/")
async def main():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    count = 0
    while True:
        data = await websocket.receive_json()
        text = data['data']
        if text != "":
            count += 1
            result = {"count": count, "text": text}
            await websocket.send_json(result)
        continue
