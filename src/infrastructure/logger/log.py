import json
import logging

logger = logging.getLogger("holidays-importer")
logger.setLevel(logging.INFO)
logger.propagate = False

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

global_uuid = None


def set_global_uuid(value: str) -> None:
    global global_uuid
    global_uuid = value


class RequestFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        record.funcName = record.funcName if record.funcName != "<module>" else "N/A"
        record.requestId = global_uuid
        record.msg = json.dumps(record.msg, ensure_ascii=False)
        return super().format(record)


requestType = "Message"
formatter = RequestFormatter('{"severityText": "%(levelname)s", '
                             f'"requestId": "%(requestId)s", '
                             f'"requestType": "{requestType}", '
                             '"timestamp": "%(asctime)s", '
                             '"file": "%(filename)s", '
                             '"function": "%(funcName)s", '
                             '"line": "%(lineno)s", '
                             '"msg": %(message)s} ')

ch.setFormatter(formatter)
logger.addHandler(ch)
