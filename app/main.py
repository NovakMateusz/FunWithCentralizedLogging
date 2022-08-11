import logging
import sys
import uuid

import sanic


async def generate_correlation_id(request: sanic.Request):
    if 'correlation-id' not in request.headers:
        request.headers['correlation-id'] = str(uuid.uuid4())


app = sanic.Sanic(name="main-app")

logger = logging.getLogger("sanic-app")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

app.register_middleware(generate_correlation_id, "request")

@app.route("/")
async def home(request: sanic.Request):
    logger.info(f"Incomming requests {request.headers['correlation-id']}")
    return sanic.response.text("hello world")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
