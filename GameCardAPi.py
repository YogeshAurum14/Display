from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/")
async def main():
    return FileResponse(r"C:\Users\Yogesh.Tiwari\PycharmProjects\hello_pic.jpg")
