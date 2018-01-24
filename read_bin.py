
file_name = "DvCTrace-170616-114442-0.BIN" 


def read_bin_file(file_name, chunks = 4, format = 'I', skip_bytes = 0, offset = 0):
	import math
	import struct
	with open(file_name, "rb") as binary_file:
		data = binary_file.read()
		var_list = []
		data = [data[chunks*i : chunks*i + chunks] for i in range(0,int(math.ceil(len(data))/chunks))]
		for val in data[::skip_bytes]:
			var_list.append(hex(struct.unpack('I',val)[0]))
		return var_list


file_name = "DvCTrace-170616-114442-0.BIN"
def validate_bin(file_name, input_list, chunks = 0, format = 'I', skip_bytes = 0, offset = 0):
	# for format please refere https://docs.python.org/2/library/struct.html
	# I = unsigned int, 
	data_list = read_bin_file(file_name[0], chunks = 4, format = 'I', skip_bytes = 2  )
	print data_list 
	
	
validate_bin("DvCTrace-170616-114442-0.BIN" , [], chunks = 4, format = 'I', skip_bytes = 2  )
