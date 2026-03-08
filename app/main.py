from fastapi import FastAPI
import redis

app = FastAPI()

r = redis.Redis(host="redis", port=6379)

@app.get("/")
def read_root():
    return {"message": "DevOps Demo"}

@app.get("/counter")
def get_counter():
    value = r.get("counter") or 0
    return {"counter": int(value)}

@app.post("/counter")
def increment():
    value = r.incr("counter")
    return {"counter": value}