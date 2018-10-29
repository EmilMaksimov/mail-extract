import os
import subprocess

'''removing old file'''
if os.path.isfile('temp.txt'):
    os.remove('temp.txt')
if os.path.isfile('pwd.gpg'):
    os.remove('pwd.gpg')

'''Decrypt the credentials file into plain text '''
subprocess.call(['gpg2','-o','temp.txt','-d','/home/emil/Documents/conecta-config/pwd.gpg'])

'''READ generated file and append to unencrypted file'''
with open('out.txt', 'r') as out:
    for line in out:
        with open('temp.txt','a') as infile:
            infile.write(line)

'''Encrypt the credentials file back '''

subprocess.call(['gpg2','-o','pwd.gpg','-e','-r','emil','temp.txt'])