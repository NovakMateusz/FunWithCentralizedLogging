from re import I
import sanic

from .utils.middlewares import generate_correlation_id


def register_all_blueprints(app: sanic.Sanic) -> None:
    from .blueprints import main_blueprint

    app.blueprint(main_blueprint)


def create_app() -> sanic.Sanic:
    app = sanic.Sanic(name="main-app")
    register_all_blueprints(app)
    app.register_middleware(generate_correlation_id, "request")

    return app
