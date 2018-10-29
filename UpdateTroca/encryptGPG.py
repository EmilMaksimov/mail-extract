import os
import subprocess

'''removing old file'''
if os.path.isfile('pwd.gpg'):
    os.remove('pwd.gpg')

'''Decrypt the credentials file into plain text '''
subprocess.call(['gpg2','-o','pwd.gpg','-e','-r','emil','out.txt'])