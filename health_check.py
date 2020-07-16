#!/usr/bin/env python3
import shutil
import psutil
import emails


def check_disk_full(disk, min_percent):
    """Returns True if there is enough free disk space, false otherwise"""
    du = shutil.disk_usage(disk)
    #calculate percentage of free space
    percent_free = 100*du.free/du.total
    #calculate how many free gigabytes
    # gigabytes_free = du.free/2**30
    print(du,percent_free)
    if percent_free<min_percent:
        return True
    return False

def cpu_check(min_percent):
	per = psutil.cpu_percent(interval=1) 
	if per>min_percent:
		return True
	return False

def memory_check(amt):
	mem = psutil.virtual_memory().available/2**30
	amt = amt/1000
	print(mem)
	if mem<amt:
		return True
	return False

if __name__ == "__main__":
	if cpu_check(80):
		message = emails.generate_error_report('automation@example.com','student-02-ed69dc9ae9d8@example.com','Error - CPU usage is over 80%','Please check your system and resolve the issue as soon as possible.')
		emails.send_email(message)
	if memory_check(500):
		message = emails.generate_error_report('automation@example.com','student-02-ed69dc9ae9d8@example.com','Error - Available memory is less than 500MB','Please check your system and resolve the issue as soon as possible.')
		emails.send_email(message)
	if check_disk_full("/",20):
		message = emails.generate_error_report('automation@example.com','student-02-ed69dc9ae9d8@example.com','Error - Available disk space is less than 20%','Please check your system and resolve the issue as soon as possible.')
		emails.send_email(message)

