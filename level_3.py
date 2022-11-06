import requests
import time
from threading import Thread

def get_html(link):
    req = requests.get(link)
    print('ready\n')

threads = [Thread(target = get_html, args = ('https://www.python.org', )) for i in range(5)]
start_time = time.time()
for t in threads:
    t.start()
    t.join()

print(f"time_pos: {time.time() - start_time} sec")

thre = [Thread(target = get_html, args = ('https://www.python.org',)) for i in range(5)]
start_time = time.time()
for y in thre:
    y.start()
    
for y in thre:
    y.join()
print(f"time_par: {time.time() - start_time} sec")