﻿#Шпилёва М.А. вариант 19 Задача 10 
#Напишите программу "Генератор персонажей" для игры. Пользователю должно
#быть предоставлено 30 пунктов, которые можно распределить между четырьмя
#характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
#пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
#туда из характеристик, которым он решил присвоить другие значения.


import random 
print (
'''
		Добро пожаловать в программу "Генератор персонажей"!
	Существует 4 характиристики: Сила, Здоровье, Мудрость и Ловкость.
	Вам предоставлено 30 пунктов, которые можете распределить между ними, также Вы можете возвращать их обратно 
	и присвоить их другой характеристике.
		Приятной игры! 
		
			
''')

points=0
pointSila=0 #кол-во очков в Силе
pointZdorovie=0 #кол-во очков в Здоровье
pointMudrost=0#кол-во очков в Мудрости
pointLovkost=0 #кол-во очков в Ловкости
while points!=31:
    a=input('Введите характеристику, которую хотите изменить: ')
    if a=='сила':
        i=input('Если хотите прибавить баллы - поставьте +, иначе -: ')
        if i=='+':
         pointSila+=1
        else:
         pointSila-=1
    if a=='здоровье':
        i=input('Если хотите прибавить баллы - поставьте +, иначе -: ')
        if i=='+':
            pointZdorovie+=1
        else:
            pointZdorovie-=1
    if a=='мудрость':
        i=input('Если хотите прибавить баллы - поставьте +, иначе -: ')
        if i=='+':
         pointMudrost+=1
        else:
         pointMudrost-=1
    if a=='ловкость':
        i=input('Если хотите прибавить баллы - поставьте +, иначе -: ')
        if i=='+':
         pointLovkost=+1
        else:
         pointLovkost-=1
    points += 1
    print ('Сила:', pointSila, '\nЗдоровье: ', pointZdorovie, '\nМудрость: ', pointMudrost, '\nЛовкость: ', pointLovkost, '\nОсталось пунктов:',30-points)

if points==31:
    print('Все 30 пунктов израсходаваны. \nСпасибо за игру!')




input ('Нажмите ')





