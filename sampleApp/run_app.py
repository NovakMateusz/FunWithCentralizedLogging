import sanic

from app import create_app


if __name__ == "__main__":
    app: sanic.Sanic = create_app()
    app.run(host="0.0.0.0", port=8000, access_log=False)
