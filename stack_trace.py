file_location =  r"C:\Users\Swapnil\projects\Python_demo\app_log.txt"
# file_loc = r"/Users/Yash/Desktop/app_log.txt"

app_log_files = file_location

f = open(app_log_files, 'r')

data = f.read()

splat = data.split("\n\n")
for numbers, paragraph in enumerate(splat, 1):
	list_of_stack = []
	list_of_stack.append(paragraph)
	print(list_of_stack)
	# list_list_stack = [list_of_stack]
	# # print(list_list_stack)
			
	
			

			