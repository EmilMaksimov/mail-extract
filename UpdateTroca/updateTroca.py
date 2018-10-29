import re


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def writeOutFile(customer, hostname, username, password, IP, OS):
    with open("out.txt", "a") as o:
        o.write(
            "\"" + customer + "\"" + "," + "\"" + hostname.upper() + "\"" + "," + "\"" + username + "\"" + "," + "\"" + password + "\"" + "," + "\"" + IP + "\"" + "," + "\"" + OS + "\"""\n")

f = open("out.txt", "w")
f.close()
t = open("temp.txt", "w")
t.close()

with open('temp.txt', 'r') as temp:
    for line in temp:
        password2 = line.split(',')[3].strip('\"')
        if "No-cmdb" in line:
            hostname = line.split(',')[1].strip('\"')
            username = line.split(',')[2].strip('\"')
            password = line.split(',')[3].strip('\"')
            flag = False
            with open('/home/emil/Downloads/query_sys0.csv') as cmdb:
                for cmdb_line in cmdb:
                    if "." not in hostname:
                        if findWholeWord(hostname)(cmdb_line.upper().split(',')[2]) is not None:
                            IP = cmdb_line.split(',')[3]
                            customer = cmdb_line.split(',')[7]
                            OS = cmdb_line.split(',')[9]
                            #print("\"" + customer + "\"" + "," + "\"" + hostname.upper() + "\"" + "," + "\"" + username + "\"" + "," + "\"" + password + "\"" + "," + "\"" + IP + "\"" + "," + "\"" + OS + "\"")
                            writeOutFile(customer, hostname, username, password, IP, OS)
                            flag = True
                            break
                    elif "." in hostname:
                        if findWholeWord(hostname.split('.')[0])(cmdb_line.upper().split(',')[2]) is not None:
                            IP = cmdb_line.split(',')[3]
                            customer = cmdb_line.split(',')[7]
                            OS = cmdb_line.split(',')[9]
                            #print("\"" + customer + "\"" + "," + "\"" + hostname.upper() + "\"" + "," + "\"" + username + "\"" + "," + "\"" + password + "\"" + "," + "\"" + IP + "\"" + "," + "\"" + OS + "\"")
                            writeOutFile(customer, hostname, username, password, IP, OS)
                            flag = True
                            break
            if flag == False:
                customer, IP, OS = ['No-cmdb'] * 3
                writeOutFile(customer, hostname, username, password2, IP, OS)
                #print("\"" + customer + "\"" + "," + "\"" + hostname.upper() + "\"" + "," + "\"" + username + "\"" + "," + "\"" + password2 + "\"" + "," + "\"" + IP + "\"" + "," + "\"" + OS + "\"")
        else:
            with open('out.txt', 'a') as infile:
                infile.write(line)
            #print(line.strip())

