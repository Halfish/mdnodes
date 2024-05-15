import threading
from time import sleep


def counter(pid=None, amount=None):
    for i in range(3):
        sleep(0.1)
        if amount:
            amount["amount"] += i + 1
        print(f"pid: {pid}, Counter {i}")


def test_thread():
    amount = {"amount": 0}
    threads = []
    for i in range(2):
        t = threading.Thread(target=counter, args=(i, amount))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"amount is {amount}")


if __name__ == '__main__':
    test_thread()
