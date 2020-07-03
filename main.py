#!/opt/local/bin/python3.8

from string import ascii_letters, punctuation, digits
from random import choice, randint 
import random
import string
import time

try:
   print ('What kind of string would you like to output? l/L outputs standard latin charaters, n/N outputs standard numerals, p/P outputs punctuation, a/A outputs all of the .')
   string_type = input()
   print ('Please enter the number of characters you would like your output to be to be. Please only input valid numerals or else the program will fail.')
   inputted_number = input()
   length_of_string = int(inputted_number) 
   let = "".join(random.choice(string.ascii_letters)for i in range(length_of_string))
   dig = "".join(random.choice(string.digits)for i in range(length_of_string))
   pun = "".join(random.choice(string.punctuation)for i in range(length_of_string))
   full = "".join(random.choice(string.digits + string.ascii_letters + string.punctuation)for i in range(length_of_string))

   if string_type.lower() == 'a':
      print (full)
   if string_type.lower() == 'l':
      print (let)
   if string_type.lower() == 'p':
      print (pun)   
   if string_type.lower() == 'n':
      print (dig)

except:
   print ('An exception has occurred! This most commonly happens when an invalid input was recieved, please check your entries and try again, if this is not the case and the error persists please raise the issue on the github page.')

#repo url is https://github.com/levelfourtwenty/randcharactersgen#
