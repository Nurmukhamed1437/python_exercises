# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""


interface = input("Введите режим работы интерфейса (access/trunk): ")
type_number = input("Введите тип и номер интерфейса: ")

vopros ={'access': 'Введите номер VLAN:',
         'trunk' : 'Введите разрешенные VLAN:'

}

q = str(input(vopros[interface]))
print(q)
access_template = [
    "switchport mode access" ,
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

dictionary = {'access': access_template,
              'trunk': trunk_template
}

print("interface:" + interface)
a = str(dictionary[interface])
c = a.replace("'",'')
d = c.replace("[",'')
d = d.replace("]",'')
e = d.replace(",","\n")
z = e.replace("{}", q)
print(z)
