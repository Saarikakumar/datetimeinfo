import os
import datetime

DEADTIME = 175

def getime (file, dir, t_result, start_time):
    d_time = []
    for i in range(2,139):
        dirno = str(i)
        newdir = dir + dirno
        os.chdir(newdir)
        times = open(file, 'r')
        lines = times.readlines()
        for line in lines:
            if line.startswith("\tstarted"):
                x = line.split("at ")
                z = x[1].split(" -0400")
                t_result.append(z[0])
    for i in range(len(t_result)):
        date_time_str = t_result[i]
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        elapsed = (date_time_obj - start_time)
        time_seconds = elapsed.total_seconds() + DEADTIME
        d_time.append(time_seconds)
    return d_time

def write_file(time):
    os.chdir("/Users/SaarikaKumar/Desktop/")
    with open('testfile.txt','w') as file:
        file.writelines("%s\n" % item for item in time)

d1 = "/Users/SaarikaKumar/Downloads/170927/"
time = []
file = 'audita.txt'
start_time_str = '2017-09-27 14:21:23.716'
start_time_obj = datetime.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S.%f')
final_time = getime(file, d1, time, start_time_obj)
print(final_time)
write_file(final_time)

