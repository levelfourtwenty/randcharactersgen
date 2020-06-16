#!/opt/local/bin/python3.8

from string import ascii_letters, punctuation, digits
from random import choice, randint 
import random
import string
import time


try:
   print('Please do not abuse this tool, it is not made to harrass people or cause intended damage to something that you do not have permission to damage.')
   time.sleep(7)
   #decrease this amount of time as you wish, it was meant so it was seen very clearly#
   print ('Please enter the number of characters you would like your output to be to be. Please only input valid numerals or else the program will fail.')
   inputted_number = input()
   length_of_string = int(inputted_number) 
   a = "".join(random.choice(string.digits + string.ascii_letters + string.punctuation)for i in range(length_of_string))
   print('Your string will be output in 4 seconds')
#feature added to help prevent lag in certain terminals#
   time.sleep(4)

   print(a)
   
except:
   print ('The script failed, this is most likely because a string or non whole number was input instead of an integer or a number was input that was too high, if so, please try again with a valid input, if not, mention it on the github repo page.')
   exit()
 
