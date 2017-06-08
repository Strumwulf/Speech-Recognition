import subprocess as sp

with open ('record.sh', 'rb') as file:
    script = file.read()
rc = sp.call(script, shell=True)
