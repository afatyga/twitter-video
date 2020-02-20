from multiprocessing import cpu_count, Pool
from twitterHW2 import startUp
import time 
import os

PROCESSES = cpu_count() - 1

def info(username):
    print("Process: " + str(username) + "process id: " + str(os.getpid()))
#    print('parent process:', os.getppid())
#    print('process id:', os.getpid())

def tempTemp (usersWCount):
	info(usersWCount[0])
	startUp(usersWCount[0], usersWCount[1])

# def add_tasks(task_queue, users):
#     for user in users:
#         task_queue.put(user)
#     return task_queue

def run(userList):
    # empty_task_queue = Queue(maxsize = 20)
    # full_task_queue = add_tasks(empty_task_queue, userList)
    print(f'Running with {PROCESSES} processes!')
#    processes = []
    startTime = time.time()
    usersWCount = []
    for user in userList:
    	userCount = []
    	userCount.append(user)
    	userCount.append(userList.index(user))
    	usersWCount.append(userCount)

#    print(usersWCount)
    pool = Pool(PROCESSES)
    pool.map(tempTemp, usersWCount)
    pool.close()
    pool.join()
#    print(full_task_queue)
#    processes = []


#     while not full_task_queue.empty():
#     	for n in range(PROCESSES):
#     		if (full_task_queue.empty()): break

# 	    	username = full_task_queue.get()
#     		info('main line', username)
# 	    	p = Process(target = tempTemp, args=(username, count,))
# 	    	processes.append(p)
#     		p.start()
#     		count = count + 1

# #      completing process
# 	    	for p in processes:
#     			p.join()

    print(f'Time taken = {time.time() - startTime:.10f}')

if __name__ == '__main__':
	users = ['johnmulaneybot', 'budiningservice',  'budogpound', 'OnlyHipHopFacts', 'jennafischer', 'bodegacats_', 'bu_tweets', 'tobyhater', 'factsofschool', 'thegoldenratio4', 'wendys', 'hogwartsmystery', 'wizardingworld', 'hpotterquotes', 'arianagrande', 'xxl']

	run(users)



	   #  print(f'Running with {PROCESSES} processes!')

    # while not full_task_queue.empty():
    # 	for n in range(PROCESSES):
    # 		if full_task_queue.empty():
    # 			break
    # 		username = full_task_queue.get()
    # 		p = Process(target = tempTemp, args=(username, count,))
    # 		processes.append(p)
    # 		p.start()
    # 		count = count + 1

    # 	for p in processes:
    # 		p.join()
    # 		print("Process DONE")

    # 	processes = []