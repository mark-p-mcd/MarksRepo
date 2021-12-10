# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 11:34:08 2021

@author: mark
"""
from tkinter import *
import tkinter as tk

root = Tk()
root.title('Mad Libs')
window_width = 300
window_height = 400
# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap('\\Users\\LENOVO\\Dropbox\\PC\\Documents\\Python Scripts\\mac.ico')
Label(root, text = 'Mad Libs Generator: \n Have Fun!', font = 'arial 20 bold').pack()
Label(root, text = 'Choose a Story :', font = 'arial 15 bold').place(x = 40, y = 80) 
def madlib1():
        school = input('Enter a school name: ')
        animals = input('Enter a plural animal (eg. mice, crockodunkles): ')
        profession = input('Enter a profession (eg. lawyer, preacher): ')
        cloth = input('Enter a piece of clothing (eg. belt, pantaloons): ')
        things = input('Enter a plural noun (eg. shovels, foreigners): ')
        name = input('Enter a name: ')
        place = input('Place name: ')
        verb = input('Enter a verb in ing form: ')
        food = input('Food name: ')
        adjective = input('Adjective: ')
        expletive = input('Enter a curse word: ')
        saying = input('Enter any phrase (eg. Put a sock in it): ') 
        print('"Say ' + food + '!", the photographer said as the camera flashed. ' + name + ' and I had gone to '\
          + place + ' to get our photos taken on my birthday. The first photo we really wanted was a picture '\
          'of us dressed as ' + animals + ' pretending to be ' + profession + 's. It was a bit disturbing when '\
          + name +' yelled "'+ saying +'"! at a nearby group of '+ adjective +' '+ profession +'s who were just watching us. Anyways, the '\
          'second photo was just what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and '\
          + verb + '-- exactly what I had in mind. '+ expletive +', I cannot wait to grow up and go to '+ school + \
            ' to learn how to be a '+ profession +' !')

def madlib2():
        school = input('Enter a school name: ')
        animals = input('Enter a plural animal (eg. mice, crockodunkles): ')
        profession = input('Enter a profession (eg. lawyer, preacher): ')
        cloth = input('Enter a piece of clothing (eg. belt, pantaloons): ')
        things = input('Enter a plural noun (eg. shovels, foreigners): ')
        name = input('Enter the name of a person: ')
        name2 = input('Another person'+"'"+'s name: ')
        place = input('Place name: ')
        verb = input('Enter a verb in ing form: ')
        food = input('Food name: ')
        adjective = input('Adjective: ')
        adjective2 = input('Another Adjective: ')
        expletive = input('Enter a curse word: ')
        saying = input('Enter any phrase (eg. Put a sock in it): ') 
        print('Holy '+ expletive +'! Today we went over to Mrs.'+ name +'\'s house to help rake the '+ things +' and '+ verb +' the hedges. '\
          'We took our break to eat some '+food+' but then we heard a loud voice saying '+saying+' from inside. '+name2+' immediately went '\
        'to investigate, and I followed. What we saw inside was nothing short of '+adjective+' -- a whole herd of '+profession+'s, huddling '\
        'and making sounds like wild '+animals+'. There was Mr. Hendrickson from '+school+'! And all of them with their '+cloth+' around their'\
        ' ankles. And Mrs.'+ name +', panting and sweating, turned to us and said "Get over here '+name2+' and other guy and do me like we\'re '\
        'in '+place+'! I feel '+adjective2+' again!"')
Button(root, text= 'The Photographer', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'Yardwork' , font = 'arial 15', command = madlib2, bg = 'light blue').place(x=70, y=180)
root.mainloop()