# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
input1 = input("Введите IP адрес и маску: ")
full_ip = input1.split('/')
ip = full_ip[0]
mask = int( full_ip[-1])
ip_splited = ip.split('.')
ip1=int(ip_splited[0])
ip2=int(ip_splited[1])
ip3=int(ip_splited[2])
ip4=int(ip_splited[3])


mask_binary = (mask*'1' + ((32-mask)*'0'))
print(mask_binary)
mask1 = int(mask_binary[0:8], 2)
mask2 = int(mask_binary[8:16], 2)
mask3 = int(mask_binary[16:24], 2)
mask4 = int(mask_binary[24:32], 2)

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
