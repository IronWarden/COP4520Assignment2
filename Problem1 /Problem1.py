import threading
import random
import time

N = 100 # number of Guests 
cupcakeAvailable = True
lock = threading.Lock()
count = 0
visited = [False] * N # bool array to keep track of visited guests 
guestIndex = 0 # keep track of guest
threads = []

def eatCupcake():
    return random.choice([True, False])

def enterLabyrinth(guestIndex):
    global cupcakeAvailable, count, lock
    # ensure mutual exclusion
    with lock:
        if not visited[guestIndex]:
            visited[guestIndex] = True
            count += 1
            print(f"Guest {guestIndex} enters the labyrinth.")
            # if there is a cupcake, guests can choose to eat it or not
            if cupcakeAvailable:
                if eatCupcake():
                    cupcakeAvailable = False
            else:
                # guest choice to get an cupcake or not 
                choice = random.choice(["Request", "Not Request"])
                if choice == "Request":
                    # guest choice to eat requested cupcake 
                    if eatCupcake():
                        cupcakeAvailable = False
                    else:
                        cupcakeAvailable = True
                else:
                    cupcakeAvailable = False

def main():
    global cupcakeAvailable, count, N, visted, threads

    for i in range(N):
        thread = threading.Thread(target=enterLabyrinth, args=(i,))
        threads.append(thread)

    while count < N:
        with lock:
            # Minotaur can pick the same guest over and over
            guestIndex = random.randint(0, N - 1)
            # the guests general strategy is to only enter once
            if not visited[guestIndex] and not threads[guestIndex].is_alive():
                threads[guestIndex].start()

    for thread in threads:
        thread.join()
    print(f"All {count} of us visited the labyrinth!")

if __name__ == "__main__":
    main()