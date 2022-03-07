"""
Room service:
Console chatbot to order room service food from a menu. 
The program will greet the user, ask for the guest's name and room number. 
If the information provided is correct, the chatbot will ask for a starter, the main course, and a dessert. 
If the information is correct then the chatbot will proceed to ask for a delivery time and confirm the order (yes/no) after repeating all the information.

By Mr. V
"""
#import module to validate the time
import datetime

#Dictionary with the current guests and their room
from tracemalloc import start


guests = {'101':'Zelem', '102':'Tool', '104':'Iveel', '105':'Chinguun'}

#Dictionaries with the menu
starters = {'101':'Green salad', '102':'Pumpking soup', '104':'Mexican Nachos'} 
main_courses = {'201':'Beef stake', '202':'Vegetarian lasagne','203':'Pizza'} 
desserts = {'301':'Chocolate cake', '302':'Ice-cream', '303':'Fruit salad'}

#Guest name and room
name = None
room = None

#Dictionary with the customer's order
order = {}

#check if the room has been booked
while room not in guests.keys():
    room = input('Please, enter your room number: ')
    #check if room exists
    if room in guests.keys():
        name = input('Please, enter your name: ')
        #Check if the room and guest name match
        if guests[room] != name:
            print ('Your name does not match our records.')
            room = None
    else:
        print (f'Room {room} has not been booked.')

#Print starters
print ()
print ('Starters menu')
print ('-------------')
for code, food in starters.items():
    print (code, '->', food)

#Add a blank line
print()

#Select starters
starter = None
#validate the starter
while starter not in starters.keys():
    starter = input ('Please, enter the starter code: ')
    if starter not in starters:
        print('Wrong starter code.')
    else:
        order[starter] = starters[starter]

#Print main courses
print ()
print ('Main courses menu')
print ('-----------------')
for code, food in main_courses.items():
    print (code, '->', food)

#Add a blank line
print()

#Select main course
main_course = None
#validate the starter
while main_course not in main_courses.keys():
    main_course = input ('Please, enter the starter code: ')
    if main_course not in main_courses:
        print('Wrong main course code.')
    else:
        order[main_course] = main_courses[main_course]

#Print desserts
print ()
print ('Desserts menu')
print ('-------------')
for code, food in desserts.items():
    print (code, '->', food)

#Add a blank line
print()

#Select starters
dessert = None
#validate the starter
while dessert not in desserts.keys():
    dessert = input ('Please, enter the starter code: ')
    if dessert not in desserts:
        print('Wrong dessert code.')
    else:
        order[dessert] = desserts[dessert]

#Validate the delivery time
validtime = False
timeformat = "%H:%M"
while not validtime:
    delivery_time = input("Please, enter delivery time (hh:mm): ")
    try:
        validtime = datetime.datetime.strptime(delivery_time, timeformat)
    except ValueError:
       print ('Time format hh:mm')

#Print the order:
print ()
print ('Your order')
print ('----------')
for code, food in order.items():
    print (code, '->', food)

print('Delivery time:', delivery_time)

#Confirm the order
place_order = ''

while place_order.lower() not in ('yes', 'no'):
    place_order = input ('Would you like to place your order (yes/no)? ')

print ()
if place_order == 'yes':
    print ('Your order is being processed')
else:
    print ('Your order has been cancelled')

print ('Thank you for choosing us!')