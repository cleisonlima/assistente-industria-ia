from fastapi import FastAPI
app = FastAPI(title='Assistente IA')

@app.get('/')
def home():
    return {'status':'ok'}
