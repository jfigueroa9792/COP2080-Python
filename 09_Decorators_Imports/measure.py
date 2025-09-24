from time import sleep, time

def measure(func):
    def wrapper(*args, **kwards):
        t = time() # get current time
        func(*args, **kwards) # call the received function
        print(func.__name__, "took:", time() - t)
    return wrapper

@measure
def f2(sleep_time = 0.1):
    sleep(sleep_time)

if __name__ == "__main__":
    print("Running directly")
