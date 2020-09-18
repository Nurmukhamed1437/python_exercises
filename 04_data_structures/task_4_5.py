#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2 (пересечение).

Результатом должен быть такой список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
list1 = command1.split( )
list2 = command2.split( )
vlans1 = list1[-1].split(',')
vlans2 = list2[-1].split(',')
command3 = sorted(list(set(vlans1) & set(vlans2)))
print(vlans1,vlans2)
print(command3)
