import sanic
from sanic.log import logger

main_blueprint = sanic.Blueprint('main_blueprint')


@main_blueprint.route("/")
async def home(request: sanic.Request):
    logger.info(f"Incomming requests {request.headers['correlation-id']}")
    return sanic.response.text("hello world")
