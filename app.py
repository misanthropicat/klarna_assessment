import uvicorn
from fastapi import FastAPI
import endpoints

app = FastAPI()
app.include_router(endpoints.router)

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8080, root_path='/', reload=True)
