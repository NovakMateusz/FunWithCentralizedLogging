from re import I
import uuid
import time

import sanic
from sanic.log import logger

__all__ = ['generate_correlation_id', 'inject_timer', 'calculate_request_time']

async def generate_correlation_id(request: sanic.Request):
    if 'correlation_id' not in request.headers:
        request.headers['correlation_id'] = str(uuid.uuid4())


async def inject_timer(request: sanic.Request):
    if not hasattr(request.ctx, 'request_time'):
        request.ctx.request_time = time.time()

async def calculate_request_time(request: sanic.Request, _: sanic.HTTPResponse):
    if hasattr(request.ctx, 'request_time'):
        logger.info(f"Request {request.headers['correlation_id']} took {time.time() - request.ctx.request_time}s")
