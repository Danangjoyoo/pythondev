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