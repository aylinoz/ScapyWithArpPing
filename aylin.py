#!/usr/bin/env python
# -*- encoding: utf-8 -*-


__license__   = 'GPL v3'
__copyright__ = '2017, Aylin Öztürk <aylin_ozturk@live.com>'
__docformat__ = 'restructuredtext en'

from sys import argv, exit
from os import path
from scapy.all import *

def yaz(dosya):
    
    f1 = open(dosya,'a')
    f2 = open('gecici2.txt','r')

    sorgu = raw_input("Degisiklikler dosyaya kaydedilsin mi?(y veya n): ")
    if sorgu == 'y':
        for line in f2:
            print("for girdi")
            f1.write(line)
        print("Degisiklikler Kaydedildi.")
    if sorgu == 'n':
        print('Degisiklikler kaydedilmedi.')
    
    f1.close()
    f2.close()

def arp_ping(host,ad):
    f3 = open("gecici2.txt", 'w')
    f3.close
    a = 0
    '''ARP Ping'''
    try:
        f1 = open(ad,'r')
    except:
        f1 = open(ad,'w')
        f1.close()
        f1 = open(ad,'r')
    f2 = open("gecici.txt",'w')
    f3 = open("gecici2.txt",'a')

    # The fastest way to discover hosts on a local ethernet network is to use the ARP Ping method:
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=host), timeout=2)

    # Answers can be reviewed with the following command:
    ans.summary(lambda (s, r): f2.write(r.sprintf("%Ether.src% %ARP.psrc% \n")))

    f2.close()
    f2 = open("gecici.txt",'r')

    for l2 in f2:
        f1 = open(ad,'r')
        for l1 in f1:
            if l1 == l2:
                a=a+1
        f1.close()
        if a==0:
            f3.write(l2)
        else:
            a=0

    f1.close()
    f3.close()
    f2.close()
    f3 = open("gecici2.txt",'r')
    toplam = sum(1 for line in f3)
    f3.close()

    if toplam>0:
	yaz(ad)

    toplam=0

if __name__ == '__main__':
    # own variant
    arp_ping('192.168.0-20.*','cikis.txt')
