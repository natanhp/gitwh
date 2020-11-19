from datetime import datetime
from pprint import pformat
import sys


def log(message):
    time = str(datetime.utcnow().strftime("%y%m%d %H%M%S.%f"))[:-4:]
    message = pformat(f"[{time}] - {message}")
    print(message, file=sys.stderr)