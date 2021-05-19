from typing import List, Optional, Set
from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl
import tts
app = FastAPI()

class Item(BaseModel):
    text: Optional[str]
@app.post("/gen_speech")
async def gen_speech(obj: Item):
    speech = tts.main(obj.text)
    return {
        "speech" : speech
    }