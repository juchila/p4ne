import time

file_src = "C://tmp//CDR.txt"
file_dst = "C://tmp//report.txt"
ff = open(file_dst, 'w')
j = 0
tt1 = time.mktime(time.strptime("18 May 2018 16:00:00", "%d %b %Y %H:%M:%S"))
tt2 = time.mktime(time.strptime("19 May 2018 13:00:0", "%d %b %Y %H:%M:%S"))

# print(str(tt1) + " " + str(tt2))

with open(file_src) as f:
    for i in f:
        cdr = i.split(",")
        if j == 0:
            j += 1
            index = [cdr.index("dateTimeOrigination"), cdr.index("callingPartyNumber"), cdr.index("originalCalledPartyNumber"), cdr.index("finalCalledPartyNumber"), cdr.index("duration")]
            for x in index:
                ff.write(cdr[x] + " \t")
            ff.write("\n")

            # print(index)
        # if i.find("b0022464021001") != -1:
            # ccc = cdr.index("b0022464021001")
            # print(str(ccc) + " " + str(j))

        if cdr[index[4]] == "0" and len(cdr[index[1]]) == 11 and tt1 <= int(cdr[index[0]]) <= tt2:
            cdr[index[0]] = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(int(cdr[index[0]])))
            for x in index:
                ff.write(cdr[x] + " \t")
            ff.write("\n")
        # j += 1
ff.close()
