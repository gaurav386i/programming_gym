import threading 


# a code two print even and odd numbers from two threads 

def print_even(n: int):
    for i in range(n):
        if i % 2 == 0:
            print(f"even thread {i}")


def print_odd(n: int):
    for i in range(n):
        if i % 2 != 0:
            print(f"odd thread {i}")

t1 = threading.Thread(target=print_even, args=(50,))
t2 = threading.Thread(target=print_odd, args=(50,))

t1.start()
t2.start()

t1.join()
t2.join()

