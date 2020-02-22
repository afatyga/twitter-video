from multiprocessing import cpu_count, Pool #for multi processing
from twitterHW2 import startUp # to multi process getting the tweets and creating the video
import time # to get the time
import sys

PROCESSES = cpu_count() - 1

def runProcesses(userList):

    print(f'Running with {PROCESSES} processes!')
    startTime = time.time()
    count = list(range(len(userList)))

    result = ([[u, c] for u,c in zip(userList,count)])

    pool = Pool(PROCESSES)
    pool.map_async(startUp, result)
    pool.close()
    pool.join()

    print(f'Time taken = {time.time() - startTime:.10f}')

if __name__ == '__main__':
	users = []
	sys.argv.pop(0)
	for user in sys.argv:
		users.append(user)
	print(str(len(users) + 1) + " tasks about to start running!") 
	if not (users == []):
		runProcesses(users)