from multiprocessing import Process, Queue
from twitterHW2 import startUp

users = ['johnmulaneybot', 'budiningservice',  'budogpound', 'OnlyHipHopFacts', 'jennafischer', 'bodegacats_', 'bu_tweets', 'tobyhater', 'factsofschool', 'thegoldenratio4', 'wendys', 'hogwartsmystery', 'wizardingworld', 'hpotterquotes', 'arianagrande', 'xxl'] #16
#users = ['johnmulaneybot', 'budiningservice',  'budogpound', 'OnlyHipHopFacts', 'jennafischer'] #5
#users = ['johnmulaneybot', 'budiningservice',  'budogpound', 'OnlyHipHopFacts', 'jennafischer', 'bodegacats_', 'bu_tweets', 'tobyhater', 'factsofschool', 'thegoldenratio4']

def tempTemp(username, count):
	startUp(username, count)
	print("Process #" + str(count) + " username: " + username)

def add_tasks(task_queue):
    for user in users:
        task_queue.put(user)
    return task_queue

def run():
    empty_task_queue = Queue(maxsize = 20)
    full_task_queue = add_tasks(empty_task_queue)
    processes = []
    startTime = time.time()
    print(full_task_queue)
    count = 0
    processes = []


    while not full_task_queue.empty():
    	username = full_task_queue.get()
    	p = Process(target = tempTemp, args=(username, count,))
    	processes.append((p, username))
    	p.start()
    	count = count + 1

#      completing process
    for (p,username) in processes:
    	p.join()
    	print(username + " completed")

    print(f'Time taken = {time.time() - startTime:.10f}')

if __name__ == '__main__':
	run()