"""
Baby Worker to make threading more efficient and effective

How To Use?
1. Import the module:

	from BabyWorker import ThreadWorker as tw

2. use the ThreadWorker.worker as decorator (@) before you write 'def somefunction'

example:
	import time

	@tw.worker
	def somefunction():
		some_list = [1,2,3,4,5]
		for i in some_list:			
			print("Hello World", i)
			time.sleep(1)
		return some_list

2. when executing your scripts, try to add some reference

example: somefunction() will be executed while print() is running because it's a thread

	a_ref = somefunction()
	print("Hello World")

3. somefunction() will be executed in subthread, to wait for it finished use wait() method

example:
	
	a_ref = somefunction()
	a_ref.wait()
	print("Hello World")

	or..

	a_ref = somefunction()
	if a_ref.wait():
		print("Hello World")

4. to know wheter your thread is already completed or not, use finished() method to check it

example:
	
	if a_ref.finished():
		print("Its Done!")
	else:
		print("Still Running!")

5. To get the return of your function, use ret() method

example:

	a_ref = somefunction()
	a_ref.wait()
	a_ref.ret = list_from_somefunction



ENJOY!

"""

import threading
import os, time, sys

class ThreadWorker():
	allWorkers = {}
	counts = 0

	class ChildWorker():
		def __init__(self, name, func):
			self.name = name
			self.func = func
			self.__finishStat = False
			self.__ret = None

		def __execute(self):
			self.__finishStat = False
			self.__ret = self.func()
			self.__finishStat = True

		@property		
		def finished(self):
			return self.__finishStat

		def job(self):
			thread1 = threading.Thread(target=self.__execute)
			thread1.start()

		def ret(self):
			return self.__ret

		def wait(self):
			while not self.finished: pass
			self.__destroy()
			return True

		def __destroy(self):
			del ThreadWorker.allWorkers[self.name]

	@staticmethod
	def worker(func):
		def register():
			workerName = 'worker'+str(ThreadWorker.counts); ThreadWorker.counts += 1
			ThreadWorker.allWorkers[workerName] = ThreadWorker.ChildWorker(workerName, func)
			ThreadWorker.allWorkers[workerName].job()
			return ThreadWorker.allWorkers[workerName]
		return register

if __name__ == '__main__':
	print("ENJOY! This Trial!")
	try:
		os.system(f"python3 -i {__name__}.py")
	except:
		os.system(f"python -i {__name__}.py")
