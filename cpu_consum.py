from multiprocessing import Process
import psutil
import logging
process_list = []
def A(n):
    print("in A")
    for i in range(n):
        abc = i * 1030*1024*1024*1024*1024*2030**11111
        print("consume cpu{0}".format(psutil.cpu_percent(interval=1, percpu=True)))
        #print(abc)
    
    
def B(n):
    print("in B")
    for i in range(n):
        abc = i * 1030*1024*1024*1024*1024*2030**11111
        print("consume cpu{0}".format(psutil.cpu_percent(interval=1, percpu=True)))
        #print(abc)
    
def C(n):
    print("in C")
    for i in range(n):
        abc = i * 1030*1024*1024*1024*1024*2030**11111
        print("consume cpu{0}".format(psutil.cpu_percent(interval=1, percpu=True)))
        #print(abc)
    
    
def D(n):
    print("in D")
    for i in range(n):
        abc = i * 1030*1024*1024*1024*1024*2030**111111
        print("consume cpu{0}".format(psutil.cpu_percent(interval=1, percpu=True)))
        #print(abc)
    
    
def E(n):
    print("in E")
    for i in range(n):
        abc = i * 1030*1024*1024*1024*1024*2030**1111111111
        print("consume cpu{0}".format(psutil.cpu_percent(interval=1, percpu=True)))
        #print(abc)
    
    
def D(n):
    print("in F")
    for i in range(n):
        abc = i * 1030*1024*1024*1024*1024*2030**11111111
        #print(abc)
    
    
def G(n):
    print("in G")
    for i in range(n):
        abc = i * 1030*1024*1024*1024*1024*2030**111111
        #print(abc)
    
    
def H(n):
    print("in H")
    for i in range(n):
        abc = i * 1030*1024*1024*1024*1024*2030**111111
        #print(abc)
    
    
def I(n):
    print("in I")
    for i in range(n):
        abc = i * 1030*1024*1024*1024*1024*2030**111111
        #print(abc)
    
    

if '__main__' == __name__:
    import psutil
    import pdb;pdb.set_trace()
    print("Count before{0}".format(psutil.cpu_count()))
    for i in range(5):
        while True:

            for proc in process_list:
                if not proc.is_alive():
                    process_list.remove(proc)

            if len(process_list) < 5:
                break
    
        pr_A = Process(target=A, args=(20,))
        pr_A.start()
        process_list.append(pr_A)

        pr_B = Process(target=B, args=(20,))
        pr_B.start()
        process_list.append(pr_B)


        pr_C = Process(target=C, args=(20,))
        pr_C.start()
        process_list.append(pr_C)


        pr_D = Process(target=D, args=(20,))
        pr_D.start()
        process_list.append(pr_D)

        for proc in process_list:
            proc.join()
    print("Count last{0}".format(psutil.cpu_count()))
