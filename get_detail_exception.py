import sys, traceback
def get_detail_exception():
    return str(sys.exc_info()[0]) +str(sys.exc_info()[1]) +' Line:'+str(sys.exc_info()[2].tb_lineno)+' function name:'+str(traceback.extract_tb(sys.exc_info()[-1], 1)[0][2])

