from prometheus_client import start_http_server, Summary
import random
import time
port = "4545"
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request(t):
    time.sleep(t)

if __name__ == '__main__':
    start_http_server(port)
    while True:
        process_request(random.random())