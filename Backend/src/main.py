from fastapi import FastAPI,Form,UploadFile,File  #form to take request from ui that is path and format
import uvicorn
import multipart
import os
#import python-multipart
import uuid
from extractor import extract
app= FastAPI()

@app.post("/extract_from_doc")
def extract_from_doc(
        file_format:str = Form(...),
        file:UploadFile =File(...),
):
    contents = file.file.read()
    file_path = "../uploads/" + str(uuid.uuid4()) + ".pdf" # uuid to give some unique name to each file while coming at backend to get process further
    with open(file_path,"wb") as f:
        f.write(contents)
    try:
        data = extract(file_path,file_format)
    except Exception as e:
        data = {
            'error': str(e)
        }


    if os.path.exists(file_path):
        os.remove(file_path)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port= 8000)