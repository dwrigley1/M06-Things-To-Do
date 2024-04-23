# Dakota Wrigley
# 15.1 'Things To Do'

''' Use multiprocessing to create three separate processes. 
Make each one wait a random number of seconds between zero 
and one, print the current time, and then exit.'''

import multiprocessing
from datetime import datetime
import time
import random as rand

def wait_time():
    cycle = rand.random()
    time.sleep(cycle)
    timestamp = datetime.now().strftime('%H:%M:%S')
    print(timestamp)

if __name__ == "__main__":
    for num in range(3):
        single_process = multiprocessing.Process(target = wait_time)
        single_process.start()
