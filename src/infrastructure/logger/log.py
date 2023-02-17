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


requestType: str = "Scheduled"
log_format: str = json.dumps({
  "severityText": "%(levelname)s",
  "requestId": "%(requestId)s",
  "requestType": requestType,
  "timestamp": "%(asctime)s",
  "file": "%(filename)s",
  "function": "%(funcName)s",
  "line": "%(lineno)s",
  "message": "%(message)s"
})

formatter = RequestFormatter(log_format)
ch.setFormatter(formatter)
logger.addHandler(ch)
