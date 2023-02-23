import os

ENV = os.getenv("ENV")
HOST = os.getenv("LOCALSTACK_HOSTNAME", "localhost")
PORT = os.getenv("EDGE_PORT", "4566")
CALENDAR_API_URL = os.getenv("CALENDAR_API_URL")

PROPERTIES: dict = {
    "ENV": ENV,
    "HOST": HOST,
    "PORT": PORT,
    "CALENDAR_API_URL": CALENDAR_API_URL,
}
