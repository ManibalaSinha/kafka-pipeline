import time

def retry(func, attempts=3, delay=2):
    for i in range(attempts):
        try:
            return func()
        except Exception as e:
            print(f"Retry {i+1} failed: {e}")
            time.sleep(delay)
    raise Exception("Max retries exceeded")