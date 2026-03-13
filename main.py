from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hellow():
    return {'message':"hellow world"}
 
@app.get("/about")
def about():
    return {'message':'capital of india is New Delhi'}