import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping for {seconds} ...')
    time.sleep(seconds)
    return f'Done Sleeping ...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:

    secs = [5,4,3,2,1]

    # threadPool = [executor.submit(do_something, sec) for sec in secs]
    # # results = [executor.submit(do_something,1) for _ in range(10)]

    # for f in concurrent.futures.as_completed(threadPool):
    #     print(f.result())
    results = executor.map(do_something, secs)

    for res in results:
        print(res)

end = time.perf_counter()

print(f'Finished in {round(end - start,2)} sec ...')