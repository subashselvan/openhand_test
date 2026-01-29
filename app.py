from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from routes import homepage


async def health(request):
    return JSONResponse({"status": "healthy"})


async def get_user(request):
    user_id = request.path_params["user_id"]
    return JSONResponse({"user_id": user_id, "name": f"User {user_id}"})


routes = [
    Route("/", homepage),
    Route("/health", health),
    Route("/users/{user_id}", get_user),
]

middleware = [
    Middleware(
        CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
    ),
]

app = Starlette(debug=True, routes=routes, middleware=middleware)
