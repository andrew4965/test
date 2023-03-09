import psutil
import GPUtil

# fetch CPU information
cpu_percent = psutil.cpu_percent()
cpu_freq = psutil.cpu_freq().current
cpu_count = psutil.cpu_count()

# print out CPU information
print("CPU Percent: {}%".format(cpu_percent))
print("CPU Frequency: {} MHz".format(cpu_freq))
print("CPU Count: {}".format(cpu_count))

