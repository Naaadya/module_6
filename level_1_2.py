import time
from threading import Thread

def get_thread(thread_name):
    time.sleep(1)
    print('\n'f'thread_name {thread_name}')


threads = [Thread(target = get_thread, args = (i + 1,)) for i in range(5)]
start_time = time.time()
for t in threads:
    t.start()
    t.join()

print(f"time_pos: {time.time() - start_time} sec")

thre = [Thread(target = get_thread, args = (i + 1,)) for i in range(5)]
start_time = time.time()
for y in thre:
    y.start()
    
for y in thre:
    y.join()
print(f"time_par: {time.time() - start_time} sec")