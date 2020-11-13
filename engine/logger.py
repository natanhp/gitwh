from datetime import datetime
from pprint import pformat


def log(message):
    time = str(datetime.utcnow().strftime("%y%m%d %H%M%S.%f"))[:-4:]
    message = pformat(f"[{time}] - {message}")
