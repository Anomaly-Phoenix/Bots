# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 13:30:50 2022

@author: 007
"""

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardButton
from Token_bot import Token 

session = vk_api.VkApi(token= Token)

def send_message(user_id, message, keyboard= None):
    
    post = { 
    'user_id': user_id,
    'message': message,
    'random_id': 0
    }
    if keyboard is not None:
       post['keyboard'] = keyboard.get_keyboard()
    
    session.method('messages.send', post)

#def inform(user_id, Name = None, male = None, age = None, Vp = None, Crash_male = None, Adress = None): 
information = {
    'user_id': None,
    'Name': None,
    'male': None,
    'age': None,
    'VP': None,
    'Crash_male': None,
    'Adress': None
    }

start_keyboard = VkKeyboard(one_time= True)
start_keyboard.add_button('Купить пропуск:')    

age_keyboard = VkKeyboard(one_time= True)
age_keyboard.add_button('Введите возраст:')

male_keyboard = VkKeyboard(one_time= True)
male_keyboard.add_button('Ж')
male_keyboard.add_button('М')

i = 0

for event in VkLongPoll(session).listen():
    if event.type ==  VkEventType.MESSAGE_NEW and event.to_me:
        text = event.text.lower()
        user_id = event.user_id
        information['user_id'] = user_id   
        i += 1
        if text == 'начать' and i == 1:
               
            start_keyboard = VkKeyboard(one_time= True)
            start_keyboard.add_button('Купить пропуск:') 
            send_message(user_id, 'Привет! :D', start_keyboard)
            
        if text == 'купить пропуск:' and i == 2 and information['VP'] == None:
               
            send_message(user_id, 'Начнем настройку профиля')
            information['VP'] = True 
            send_message(user_id, 'Введите ваше имя: ')
        
        if i == 3 and information['Name'] == None:
         
            male_keyboard = VkKeyboard(one_time= True)
            male_keyboard.add_button('Ж')
            male_keyboard.add_button('М')

            information['Name'] = str(event.text)
            send_message(user_id, 'Ваш пол:',  male_keyboard)
            
        if i == 4 and information['male'] == None: 
             
            information['male'] = str(event.text)
            send_message(user_id, 'Введите возраст: ')
        
        if i == 5  and information['age'] == None:
             
           information['age'] = str(event.text)
           send_message(user_id, 'Какого пола должен быть партнер?', male_keyboard)
       
        if i == 6 and information['Crash_male'] == None: 
                
                information['Crash_male'] = str(event.text)
                send_message(user_id, 'Какой у вас город?')
        
        if i == 7 and information['Adress'] == None: 
                
                information['Adress'] = str(event.text)
        #print(information)