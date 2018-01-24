"""
@author = abhijeet mote
		  abhijeet.dadax.mote@intel.com

functionality : copoies the files recursiverly present in each directory

demo to execute:
python recursiveCopy.py {source_path} {destination_path} {start_date}
python recursiveCopy.py C:\task C:\destination\destination_files "2015-07-25"
"""
import os
import sys
import shutil
import time
def get_detail_exception():
    type, value, traceback = sys.exc_info()
    return "{0} {1} Line:{2} in source_file {3}".format(type, value, traceback.tb_lineno, os.path.split(traceback.tb_frame.f_code.co_filename)[1])
     
def recursiveCopy(source_path, destination_path, start_date):
	try:
		start_epoch_time = int(time.mktime(time.strptime(start_date, "%Y-%m-%d")))
		if not os.path.isdir(destination_path):
			os.makedirs(destination_path)
			print("Directory is not present, created directory:{0}".format(destination_path))

		print("Copying below files to {0}:".format(destination_path))
		for i in  os.walk(source_path):
			dir_path = i[0]
			for j in i:
				for k in j:
					if (k.endswith("tar.gz") or k.endswith("zip")):
						complete_path = os.path.join(dir_path, os.path.basename(k))
						creation_time = os.path.getmtime(complete_path)
						if start_epoch_time < creation_time and \
							not os.path.isfile(os.path.join(destination_path,k)):
							print(complete_path)
							shutil.copy2(complete_path, destination_path)
	except Exception as e:
		print("#System_Exception : Error Occured " + get_detail_exception())

if __name__ == "__main__":
	#import pdb;pdb.set_trace()
	try:
		if sys.argv[1] and sys.argv[2] and sys.argv[3]:
			source_path = sys.argv[1]
			destination_path = sys.argv[2]
			start_date = sys.argv[3]
			recursiveCopy(source_path, destination_path, start_date)
		else:
			print("arguments are not valid...")
	except:
		print("Please provide the valid source_path, destination_path and start_date")
		sys.exit(0)
