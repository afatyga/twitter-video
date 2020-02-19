import time
from multiprocessing import Process, Queue, cpu_count
from twitterHW2 import start
#import os
#import time

PROCESSES = cpu_count() - 1
NUMBER_OF_TASKS = 10

users = ['johnmulaneybot', 'tobyhater',  'barackobama', 'rihanna', 'katyperry', 'taylorswift13']


def process_tasks(task_queue):
    while not task_queue.empty():
        username = task_queue.get()
        start(username)
    return True


def add_tasks(task_queue):
    for user in users:
        task_queue.put(user)
    return task_queue


def run():
    empty_task_queue = Queue()
    full_task_queue = add_tasks(empty_task_queue)
    processes = []
    print(f'Running with {PROCESSES} processes!')
    start = time.time()
    for n in range(PROCESSES):
        p = Process(
            target=process_tasks, args=(full_task_queue,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
    print(f'Time taken = {time.time() - start:.10f}')



# users = ['johnmulaneybot', 'tobyhater',  'barackobama', 'rihanna', 'katyperry', 'taylorswift13']

# queue = Queue()
# for user in users: #adds them to the queue
# 	queue.put(user)


# def processItUp():
# 	startTime = time.time()
# 	number_of_processes = 7
# 	number_of_tasks = len(users)
# 	processes = []

# 	for w in range(number_of_processes):
# 		if (not queue.Empty):
# 			p = Process(target=getMsgs, args=(queue.get(),) )
# 			processes.append(p)
# 			p.start()

#     # completing process
# 	for p in processes:
# 		p.join()


# 	print(f'Time taken = {time.time() - startTime:.10f}')


if __name__ == '__main__':
	run()
#    processItUp()