from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return {"message":"hey there"}


@app.get('/about')
def about():
    return {
        "Message":"This is a small app about fast api"
    }
