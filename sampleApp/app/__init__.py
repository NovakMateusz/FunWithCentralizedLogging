from re import I
import sanic

from .utils.middlewares import generate_correlation_id, inject_timer, calculate_request_time


def register_all_blueprints(app: sanic.Sanic) -> None:
    from .blueprints import main_blueprint

    app.blueprint(main_blueprint)


def register_middlewares(app: sanic.Sanic) -> None:

    app.register_middleware(generate_correlation_id, "request")
    app.register_middleware(inject_timer, "request")
    app.register_middleware(calculate_request_time, "response")


def create_app() -> sanic.Sanic:
    app = sanic.Sanic(name="main-app")
    register_all_blueprints(app)
    register_middlewares(app)
    

    return app
