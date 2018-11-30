# import os
# import subprocess
#
# '''removing old file'''
# if os.path.isfile('pwd.gpg'):
#     os.remove('pwd.gpg')
#
# '''Decrypt the credentials file into plain text '''
# subprocess.call(['gpg','-o','pwd.gpg','-e','-r','emil.maksimov@cz.ibm.com','out.txt'])

import os
import gnupg
from shutil import copyfile

copyfile('/Users/emaksimov/Documents/conecta-config/pwd.gpg','/Users/emaksimov/Documents/conecta-config/pwd.gpg.bak')

gpg = gnupg.GPG(gnupghome='/Users/emaksimov/.gnupg/')
#open('/tmp/pwd.txt','a').write('ANOTHER NEW LINE\n')


with open('/tmp/out.txt','rb') as f:
    status = gpg.encrypt_file(f, recipients=['emil.maksimov@cz.ibm.com'], output='/Users/emaksimov/Documents/conecta-config/pwd.gpg')

os.system('rm -f /tmp/out.txt')

print('ok: ', status.ok)
print('Status: ', status.status)
print('stderr: ', status.stderr)
