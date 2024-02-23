import threading
import random
import time

N = 10  # number of guests
available = True # sign is available at the start
lock = threading.Lock()


def enterRoom(guestIndex):
    global available, lock
    # not locked as any thread should be able to see the sign if it's available
    while not available:
        # if not available the guest can enjoy the party
        print(
            f'Guest #{guestIndex} saw that the room is not available so he went to party')
        time.sleep(random.uniform(0.10, 2))
    # changing the sign we have to use lock to ensure mutual exclusion 
    with lock:
        available = False
        print(f'Guest #{guestIndex} has entered the room')
    time.sleep(random.uniform(0.1, 2))  # pass time in the room
    # changing the sign use lock
    with lock:
        print(f'Guest #{guestIndex} has left the room')
        available = True


def main():
    threads = []
    for i in range(N):
        thread = threading.Thread(target=enterRoom, args=(i, ))
        threads.append(thread)

    for thread in threads:
        # pass time to simulate guests coming at random times
        time.sleep(random.uniform(0.1, 2)) 
        thread.start()
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
