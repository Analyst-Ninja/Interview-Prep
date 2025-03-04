import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'{seconds} sec Sleeping !!')
    time.sleep(seconds)
    print('Done Sleeping !!')

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t1.start()
# t2.start()

# t1.join()
# t2.join()

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

end = time.perf_counter()

print(f"Finished in {round(end - start,2)} sec.")