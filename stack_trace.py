file_location =  r"C:\Users\Swapnil\projects\Python_demo\app_log.txt"
# file_loc = r"/Users/Yash/Desktop/app_log.txt"

app_log_files = file_location

##Open file
with open(app_log_files) as f:
	##readlines
	f = f.readlines()

	##Find by year
	date = '2020'

	count = 1
	list_of_stack = []
	for logs in f:
		if date in logs:
			count += 1
			list_of_stack.append(logs)
	##Give total lines with 2020		
	print('Count',count)
	##Each line is stored in a list seperated by comma.
	sorted_list = [x for xs in list_of_stack for x in xs.split(",")]
	print(sorted_list)
