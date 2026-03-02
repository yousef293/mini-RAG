from fastapi import FastAPI
app=FastAPI()
@app.get('/hello')
def welcome():
    return {
        "message":"hellow from the server"
    }