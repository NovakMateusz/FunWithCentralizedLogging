import sanic

from .blueprints import main_blueprint
from .utils.middlewares import generate_correlation_id, inject_timer, calculate_request_time
from .utils.log import setup_logging


def register_all_blueprints(app: sanic.Sanic) -> None:
    app.blueprint(main_blueprint)


def register_middlewares(app: sanic.Sanic) -> None:

    app.register_middleware(generate_correlation_id, "request")
    app.register_middleware(inject_timer, "request")
    app.register_middleware(calculate_request_time, "response")


def register_listeners(app: sanic.Sanic) -> None:
    app.register_listener(setup_logging, "after_server_start")


def create_app() -> sanic.Sanic:
    app = sanic.Sanic(name="main-app")
    register_all_blueprints(app)
    register_middlewares(app)
    setup_logging(app)

    return app
