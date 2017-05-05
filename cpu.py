

import psutil
print(psutil.cpu_count())

p = psutil.Process()
print(p.cpu_affinity())  # get

p.cpu_affinity([0])  # set; from now on, process will run on CPU #0 only
print p.cpu_affinity()

# reset affinity against all CPUs
all_cpus = list(range(psutil.cpu_count()))
p.cpu_affinity(all_cpus)


psutil.disk_io_counters()

psutil.disk_io_counters(perdisk=True)

#Get cpu wise utilization
for i in range(20):
    print(psutil.cpu_percent(interval=1, percpu=True))
    print("------------------------------")

