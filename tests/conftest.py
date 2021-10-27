import pytest
import fastwsgi
import time
from multiprocessing import Process


HOST = "127.0.0.1"
PORT = 8080


class ServerProcess:
    def __init__(self, application, host=HOST, port=PORT) -> None:
        self.process = Process(target=fastwsgi.run, args=(application, host, port))
        self.endpoint = f"http://{host}:{port}"

    def __enter__(self):
        self.process.start()
        time.sleep(1)  # Allow server to start
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if self.process.is_alive():
            self.process.terminate()


@pytest.fixture(autouse=True, scope="session")
def server_process():
    return ServerProcess