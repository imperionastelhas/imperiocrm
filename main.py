from fastapi import FastAPI
import asyncpg
import os
DATABASE_URL = os.getenv("DATABASE_URL")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API funcionando"}

@app.get("/ping-db")
async def ping_db():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.close()
    return {"db": "ok"}