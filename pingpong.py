import platform
import subprocess
import argparse
import socket

#Ping function
def myping(host):
    parameter = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)

    if response == 0:
        return True
    else:
        return False

#Argparse interface
parser = argparse.ArgumentParser()
parser.add_argument('File',
                    metavar='file',
                    type=str,
                    help='name of parsed file')

args = parser.parse_args()
f = open(args.File, 'r', encoding="utf-8")


sucpingfile = open('successfullypinged.txt', 'w')
unsucpingfile = open('unsuccesfullypinged.txt', 'w')
sucping = ''
unsucping = ''


while True:
    line = f.readline()
    line = line.replace('\r', '')
    line = line.replace('\n', '')
    print(line)
    
    if myping(line) == True:
        sucping = sucping + line + '\r\n'
    else:
        try:
            ipaddres = socket.gethostbyname(line)
        except Exception:
            ipaddres = ''
            pass
        unsucping = unsucping + line + ' ' + ipaddres + '\r\n'
    
    if not line:
        sucpingfile.write(sucping)
        unsucpingfile.write(unsucping)
        f.close
        sucpingfile.close
        unsucpingfile.close
        break