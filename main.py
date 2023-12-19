from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional


class Memo(BaseModel):
    id: Optional[str] = None
    content: Optional[str] = None
    
memos = []

app = FastAPI()

@app.post("/memos")
def create_memo(memo:Memo):
    memos.append(memo)
    return '메모 추가됨'

@app.get("/memos")
def read_memo():
    return memos

@app.put("/memos/{memo_id}")
def put_memo(req_memo:Memo):
    for memo in memos:
        if memo.id==req_memo.id:
            memo.content = req_memo.content
            return 'succeed'
    return 'fuck you'

@app.delete("/memos/{memo_id}")
def delete_memo(memo_id):
    for index,memo in enumerate(memos):
        if memo.id==memo_id:
            memos.pop(index)
            return 'succeed'
    return 'fuck you'


app.mount("/", StaticFiles(directory="static",html=True), name="static")