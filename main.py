from string import ascii_letters, punctuation, digits
from random import choice, randint 
import random
import string
import time

try:
    print ('Please do not abuse this tool, it is not made to harrass people or cause intended damage to something that you do not have permission to damage.')
    time.sleep(6.9)
    print ('Please enter the number of characters you would like your output to be to be. Please only input valid numerals or else the program will fail.')
    inputted_number = input()
    length_of_string = (inputted_number) 
    a = "".join(random.choice(string.digits + string.ascii_letters + string.punctuation)for i in range(length_of_string))
    print ('Your string will be output in 10 seconds')
    #feature added to help prevent lag in certain terminals#
    time.sleep(1)
    print ('9 seconds')
    time.sleep(1)
    print ('8 seconds')
    time.sleep(1)
    print ('7 seconds')
    time.sleep(1)
    print('6 seconds')
    time.sleep(1)
    print ('5 seconds')
    time.sleep(1)
    print ('4 seconds')
    time.sleep(1)
    print ('3 seconds')
    time.sleep(1)
    print ('2 seconds')
    time.sleep(1)
    print('1 second')
    time.sleep(1)
    print (a)
except:
    print ('The script failed, this is most likely because a string or non whole number was input instead of an integer or a number was input that was too high, if so, please try again with a valid input, if not, mention it on the github repo page.')
    exit()
 
    

