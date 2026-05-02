import os, threading, multiprocessing
shared = {"count": 0}
def thread_job():
    shared["count"] += 1
    print("thread", threading.current_thread().name, shared)
def process_job():
    local = {"count": 0}
    local["count"] += 1
    print("process pid=", os.getpid(), local)
if __name__ == "__main__":
    t1 = threading.Thread(target=thread_job, name="T1")
    t2 = threading.Thread(target=thread_job, name="T2")
    t1.start(); t2.start()
    t1.join(); t2.join()
    print("main sees", shared) # threads changed shared memory
    p1 = multiprocessing.Process(target=process_job)
    p2 = multiprocessing.Process(target=process_job)
    p1.start(); p2.start()
    p1.join(); p2.join()
    print("main still sees", shared)