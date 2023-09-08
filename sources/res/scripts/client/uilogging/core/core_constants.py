from enum import Enum

class HttpHeaders(str, Enum):
    AUTH_TOKEN = 'X-TOKEN'
    USER_ID = 'X-SPA-ID'
    CONTENT_TYPE = 'Content-Type'


HTTP_OK_STATUS = 200
HTTP_SESSION_EXPIRED = 498
HTTP_DEFAULT_TIMEOUT = 30
FINAL_FLUSH_TIMEOUT = 3
DEFAULT_COMPRESSION_LEVEL = 5
LOGS_SEND_PERIOD = 5.0
LOGS_FORCE_SEND_PERIOD = 600.0
LOGS_MAX_QUEUE_SIZE = 5000
LOGS_MAX_COUNT_PER_SEND = 50
LOG_RECORD_MAX_PROPERTIES_COUNT = 1000
REQUEST_SESSION_TIMEOUT = 45
ENSURE_SESSION_TICK = 5.0
MAX_SESSION_GET_RETRIES = 3
MIN_SESSION_LIFE_TIME = LOGS_SEND_PERIOD * 2