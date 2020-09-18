# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

full_ip = argv[1]
full_ip1 = full_ip.split('/')
ip = full_ip1[0]
mask = int( full_ip1[-1])
ip_splited = ip.split('.')

ip1= int(ip_splited[0])
ip2= int(ip_splited[1])
ip3= int(ip_splited[2])
ip4= 0

mask_binary = (mask*'1' + ((32-mask)*'0'))
print(mask_binary)
mask1 = int( mask_binary[0:8],2)
mask2 = int(mask_binary[8:16],2)
mask3 = int(mask_binary[16:24],2)
mask4 = int(mask_binary[24:32],2)

print(mask_binary)
print(mask)
print(mask1)
print(f'''
Network:
{ip1:<8} {ip2:<8} {ip3:<8} {ip4:<8}
{ip1:08b} {ip2:08b} {ip3:08b} {ip4:08b}

Mask:
{mask1:<8} {mask2:<8} {mask3:<8} {mask4:<8}
{mask1:08b} {mask2:08b} {mask3:08b} {mask4:08b}
''')
