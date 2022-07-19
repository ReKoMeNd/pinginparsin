import os
import sys
import platform
import subprocess
import argparse

#Searching for A DNS records
def dnsrecord(f1):
    if f1.find("IN	A")!=-1:
        return f1

#Adding name of parsed file
parser = argparse.ArgumentParser()
parser.add_argument('File',
                    metavar='file',
                    type=str,
                    help='name of parsed file')

args = parser.parse_args()

print(args.File)

f = open(args.File, 'r', encoding="utf-8")

sd = ""
f1 = open('parsedfile.txt', 'w')

while True:

    line = f.readline()
    if type(dnsrecord(line)) == str:
        ad = dnsrecord(line).replace(';', '')
        ad = ad.replace('*', '')
        if ad[0] == '.' or ad[0] == ' ':
            ad = ad[:0] + '' + ad[1:]
            
        if ad.find('	'):
            sd = sd + ad.partition('	')[0] + '.mai.ru' + '\r\n'
        else:
            sd = sd + ad.partition('		')[0] + '.mai.ru' + '\r\n'
   
    if not line:
        sd = sd.replace('\r', '')
        f1.write(sd)
        f.close
        break

print(sd)


