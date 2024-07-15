from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from infrastructure.container import Container



def create_app() -> FastAPI:
    app = FastAPI()
    container = Container()

    app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, 
                       allow_methods=['*'], allow_headers=['*'])

    from presentation.endpoints.logs import controller as logs_controllers
    logs_controllers.configure(app)

    container.wire([logs_controllers])

    return app


api_app = create_app()

if __name__ == '__main__':
    uvicorn.run('app:api_app', host='0.0.0.0', port=8080, reload=True)
