# Copyright (c) 2022 Nikhil Akki
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import pickledb
from src.hash import generate_url_hash

db = pickledb.load(os.getenv("PICKLE_DB_URI", "test.db"), False)
app = FastAPI()


class GenerateShortURL(BaseModel):
    url: str


@app.get("/")
def health_check():
    return {"response": "Health check success"}


@app.post("/shortened-url")
def shortended_url(generateShortURL: GenerateShortURL):
    url = generateShortURL.url
    short_url = generate_url_hash()
    db.set(short_url, url)
    db.dump()
    return {"response": dict(url=url, short_url=short_url)}


@app.get("/all")
def all_records():
    return {item: db.get(item) for item in db.getall()}


@app.get("/{shortUrl}")
def short_to_big_url(shortUrl: str):
    record = db.get(shortUrl)
    return RedirectResponse(record)
