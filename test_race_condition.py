# import threading

# JOHN_TOTAL = 0

# def add(num):
#     global JOHN_TOTAL
#     for _ in range(100000):
#         JOHN_TOTAL += num


# while JOHN_TOTAL == 0:
#     john = threading.Thread(target=add, args=(1, ))
#     alice = threading.Thread(target=add, args=(-1, ))

#     threads = (john, alice, )
#     for thread in threads:
#         thread.start()
#     for thread in threads:
#         thread.join()

#     print(f"John's total: {JOHN_TOTAL}")
import threading


JOHN_TOTAL = 0
LOCK = threading.Lock()

def add(lock, num):
    lock.acquire()
    global JOHN_TOTAL
    for _ in range(100000):
        JOHN_TOTAL += num
    lock.release()

RETRY_COUNT = 0
while JOHN_TOTAL == 0 and RETRY_COUNT < 10:
    john = threading.Thread(target=add, args=(LOCK, 1, ))
    alice = threading.Thread(target=add, args=(LOCK, -1, ))

    threads = (john, alice, )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    print(f"John's total: {JOHN_TOTAL}")
    RETRY_COUNT += 1