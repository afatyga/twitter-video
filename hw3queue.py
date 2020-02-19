import time

from multiprocessing import Process, Queue, Pool
from twitterHW2 import getMsgs
import multiprocessing
import os
import time

#PROCESSES = multiprocessing.cpu_count() - 1

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=getMsgs, args=('johnmulaneybot',))
#     p.start()
#     p.join()

users = ['johnmulaneybot', 'tobyhater',  'barackobama', 'rihanna', 'katyperry', 'taylorswift13']

queue = Queue()
for user in users: #adds them to the queue
	queue.put(user)


def processItUp():
	startTime = time.time()
	number_of_processes = 7
	number_of_tasks = len(users)
	processes = []


	for w in range(number_of_processes):
		p = Process(target=getMsgs, args=(queue.get(),) )
		processes.append(p)
		p.start()

    # completing process
	for p in processes:
		p.join()


	print(f'Time taken = {time.time() - startTime:.10f}')


if __name__ == '__main__':
    processItUp()