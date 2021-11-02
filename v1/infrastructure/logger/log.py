import json
import logging

logger = logging.getLogger('my_application')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

logger.propagate = False


class RequestFormatter(logging.Formatter):
    def format(self, record, **kwargs):
        if "func" not in record.__dict__: record.func = record.funcName
        if "file" not in record.__dict__: record.file = record.filename
        if "line" not in record.__dict__: record.line = record.lineno
        record.msg = json.dumps(record.msg, ensure_ascii=False)
        return super().format(record)


formatter = RequestFormatter('{"severityText": "%(levelname)s", '
                             '"timestamp": "%(asctime)s", '
                             '"file": "%(file)s", '
                             '"line": "%(line)s", '
                             '"msg": %(message)s} ',
                             datefmt='%d/%m/%Y %H:%M:%S')

ch.setFormatter(formatter)
logger.addHandler(ch)
