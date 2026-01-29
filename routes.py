"""Route handlers for the Starlette application."""

from starlette.responses import JSONResponse


async def homepage(request):
    """Handle homepage requests."""
    return JSONResponse({"message": "Welcome to Starlette Application!"})
