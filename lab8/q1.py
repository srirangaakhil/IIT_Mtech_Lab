import os

if __name__ == '__main__':
	work_dir = 'working_ip_address.txt'
	non_work_dir = 'non_working_ip_address.txt'
	ip = '10.130.154.'
	host_index = 1

	work_ptr = open(work_dir, "w")
	non_work_ptr = open(non_work_dir, "w")

	while host_index <= 132:
		response = os.system("ping -c 1 " + ip + str(host_index) + " >> /dev/null")
		if response == 0:
			work_ptr.write(ip + str(host_index) + '\n')
		else:
			non_work_ptr.write(ip + str(host_index) + '\n')
		host_index += 1

	work_ptr.close()
	non_work_ptr.close()