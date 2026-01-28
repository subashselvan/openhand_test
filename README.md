# Starlette Application

A simple web application built with Starlette and managed with uv.

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Run the development server:
   ```bash
   uv run python server.py
   ```
   Or:
   ```bash
   uv run start
   ```

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `GET /users/{user_id}` - Get user by ID

## Development

The application runs on `http://localhost:8000` with auto-reload enabled.