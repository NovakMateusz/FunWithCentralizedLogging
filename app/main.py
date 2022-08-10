import logging
import logging.handlers


import json_logging
import sanic
from sanic.log import logger

app = sanic.Sanic(name="main-app")

json_logging.init_sanic(enable_json=True)
json_logging.init_request_instrument(app)

# init the logger as usual
logger = logging.getLogger("main-app-logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.basicConfig(filename="./logs/test.log"))


@app.route("/")
async def home(request):
    # this will be faster
    correlation_id = json_logging.get_correlation_id(request=request)

    return sanic.response.text("hello world")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, access_log=True)