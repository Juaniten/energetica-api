import uvicorn
from server import app

if __name__ == '__main__':
    uvicorn.run("server.app:app", reload=True)
