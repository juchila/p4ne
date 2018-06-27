import time

file_src = ["C://tmp//phone.csv", "C://tmp//deviceprofile.csv"]
file_dst = "C://tmp//report.txt"
ff = open(file_dst, 'w')
# tt1 = time.mktime(time.strptime("18 May 2018 16:00:00", "%d %b %Y %H:%M:%S"))
# tt2 = time.mktime(time.strptime("19 May 2018 13:00:0", "%d %b %Y %H:%M:%S"))

# print(str(tt1) + " " + str(tt2))

for fn in file_src:
    print(fn)
    with open(fn, 'r', encoding='utf-8') as f:
        j = 0
        for i in f:
            device = i.split(",")
            # print(device)
            if j == 0:
                j += 1
                index = [device.index("Directory Number 1"), device.index("Line CSS 1"),
                         device.index("Alerting Name 1"),
                         device.index("ASCII Alerting Name 1"),
                         device.index("Line Description 1"),
                         device.index("External Phone Number Mask 1"),
                         device.index("Directory Number 2"), device.index("Line CSS 2"),
                         device.index("Alerting Name 2"),
                         device.index("ASCII Alerting Name 2"),
                         device.index("Line Description 2"),
                         device.index("External Phone Number Mask 2")]
            # j += 1
            # ff.write(str(j) + "\n")
            for x in index:
                # print(device[x])
                if device[x] != '': ff.write(device[x] + " \t")
            ff.write("\n")
ff.close()
