import os
import psutils


def send_cmd(cmd_name):
	os.system(cmd_name)



def get_proc_pid(name):
	for proc in psutil.process_iter():
		if proc.name() == name:
			return str(proc.pid)
			
			
			
			
	
if __name__ == '__main__':
	cmd_list = ['copy c:\Users\Ulaf\Desktop\dir1\mov.MP4 C:\Users\Ulaf\Desktop\dir2','mkdir newdir']
	send_cmd( [cmd_list[0] )
	print get_proc_pid(cmd_list[0])