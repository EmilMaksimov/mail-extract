import re


def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def writeOutFile(customer, i, username, password, IP, OS):
    with open("/tmp/temp.txt", "a") as o:
        o.write("\"" + customer + "\"" + "," + "\"" + i.upper() + "\"" + "," + "\"" + username + "\"" + "," + "\"" + password + "\"" + "," + "\"" + IP + "\"" + "," + "\"" + OS + "\"""\n")


mail_extract = input('Enter your mail extract file path: ')
hostname = None
unique_hostnames = []
f = open("/tmp/temp.txt", "w")
f.close()

with open(mail_extract) as m:
    for m_line in m:
        if "System" in m_line and "Abstract" not in m_line:
            hostname = m_line.strip().split(':')[1].split(' ')[0]
        if hostname not in unique_hostnames and hostname != None:
            unique_hostnames.append(hostname)
for i in unique_hostnames:
    with open(mail_extract) as u:
        for u_line in u:
            if i in u_line and "Password:" in u_line and "Abstract" not in u_line:
                password = u_line.strip().split(':')[2]
    with open(mail_extract) as uu:
        for uu_line in uu:
            if i in uu_line and "User" in uu_line and "Abstract" not in uu_line:
                username = uu_line.strip().split(':')[2]
    flag = False
    with open('../query_sys0.csv') as cmdb:
        for cmdb_line in cmdb:
            if "." not in i:
                if findWholeWord(i)(cmdb_line.upper().split(',')[2]) != None:
                    IP = cmdb_line.split(',')[3]
                    customer = cmdb_line.split(',')[7]
                    OS = cmdb_line.split(',')[9]
                    writeOutFile(customer, i, username, password, IP, OS)
                    flag = True
                    break
            elif "." in i:
                if findWholeWord(i.split('.')[0])(cmdb_line.upper().split(',')[2]) != None:
                    IP = cmdb_line.split(',')[3]
                    customer = cmdb_line.split(',')[7]
                    OS = cmdb_line.split(',')[9]
                    writeOutFile(customer, i.split('.')[0], username, password, IP, OS)
                    flag = True
                    break
    if flag == False:
        customer, IP, OS = ['No-cmdb'] * 3
        writeOutFile(customer, i, username, password, IP, OS)
