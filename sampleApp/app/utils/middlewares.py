import uuid
import sanic


async def generate_correlation_id(request: sanic.Request):
    if 'correlation-id' not in request.headers:
        request.headers['correlation-id'] = str(uuid.uuid4())
