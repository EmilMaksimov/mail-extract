# import os
# import subprocess
#
# '''removing old file'''
# if os.path.isfile('temp.txt'):
#     os.remove('temp.txt')
# if os.path.isfile('pwd.gpg'):
#     os.remove('pwd.gpg')
#
# '''Decrypt the credentials file into plain text '''
# subprocess.call(['gpg','-o','temp.txt','-d','/Users/emaksimov/Documents/conecta-config/pwd.gpg'])


import gnupg
import getpass

passphrase = getpass.getpass()

gpg = gnupg.GPG(gnupghome='/Users/emaksimov/.gnupg/')

with open('/Users/emaksimov/Documents/conecta-config/pwd.gpg', 'rb') as f:
    status = gpg.decrypt_file(f, passphrase=passphrase, output='/tmp/pwd.txt')

print('ok: ', status.ok)
print('Status: ', status.status)
print('stderr: ', status.stderr)