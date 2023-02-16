import os

ENV = os.getenv("ENV", "local")
HOST = os.getenv("LOCALSTACK_HOSTNAME", "localhost")
PORT = os.getenv("EDGE_PORT", "4566")
CALENDAR_API_URL = os.getenv("CALENDAR_API_URL", "https://brasilapi.com.br/api/feriados/v1/")

PROPERTIES: dict = {
    "ENV": ENV,
    "HOST": HOST,
    "PORT": PORT,
    "CALENDAR_API_URL": CALENDAR_API_URL,
}
