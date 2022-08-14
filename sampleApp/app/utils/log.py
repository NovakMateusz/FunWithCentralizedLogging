from datetime import datetime
import logging

import json_logging
from json_logging.util import iso_time_format, RequestUtil
from json_logging.framework.sanic import RequestAdapter, ResponseAdapter
import ujson
import sanic


__all__ = ['setup_logging']


class CustomBaseJSONFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._request_util = RequestUtil(request_adapter_class=RequestAdapter, response_adapter_class=ResponseAdapter)

    def format(self, record):
        log_object = self._format_log_object(record, request_util=self._request_util)
        return ujson.dumps(log_object, ensure_ascii=False)

    def _format_log_object(self, record, request_util: RequestUtil):
        utcnow = datetime.utcnow()
        base_object = {
            'time': iso_time_format(utcnow),
            "level": record.levelname

        }
        return base_object


class CustomJSONRequestLogFormatter(CustomBaseJSONFormatter):
    def _format_log_object(self, record, request_util: RequestUtil):
        request = record.request_info.request
        request_adapter = request_util.request_adapter

        json_log_object = super()._format_log_object(record, request_util)

        json_log_object.update(
            {
                'type': 'request',
                'message': f'Requests to {request_adapter.get_path(request)}'
            }
        )
        return json_log_object


class CustomJSONLogFormatter(CustomBaseJSONFormatter):
    def _format_log_object(self, record, request_util: RequestUtil):

        json_log_object = super()._format_log_object(record, request_util)
        json_log_object.update(
            {
                'type': 'log',
                'message': self._sanitize_log_message(record)
            }
        )
        return json_log_object

    @staticmethod
    def _sanitize_log_message(record):
        return record.getMessage().replace('\n', '_').replace('\r', '_').replace('\t', '_')


def setup_logging(app: sanic.Sanic) -> None:
    json_logging.init_sanic(custom_formatter=CustomJSONLogFormatter, enable_json=True)
    json_logging.init_request_instrument(app, custom_formatter=CustomJSONRequestLogFormatter)
