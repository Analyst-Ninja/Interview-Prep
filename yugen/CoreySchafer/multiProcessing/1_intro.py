import concurrent.futures
import time
import multiprocessing
import concurrent

start = time. perf_counter()

def do_something(sec):
    print(f"{sec} sec, I am sleeping ...")
    time.sleep(sec)
    # print(f"Done sleeping")
    return f"Done sleeping ... Took {sec} seconds"

# processes = []

# for _ in range(10):
#     p = multiprocessing.Process(target=do_something, args=[1])
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()

with concurrent.futures.ProcessPoolExecutor() as executor:
    # f1 = executor.submit(do_something,1)
    # f2 = executor.submit(do_something,1)

    # print(f1.result())
    # print(f2.result())

    secs = [5,4,3,2,1]
    # processPool = [executor.submit(do_something, 1) for _ in range(10)]
    # processPool = [executor.submit(do_something, sec) for sec in secs]


    # for f in concurrent.futures.as_completed(processPool):
    #     print(f.result())

    processPoolResult = executor.map(do_something,secs)

    for res in processPoolResult:
        print(res)

end = time.perf_counter()

print(f'Finished in {round(end - start,2)}')


