''' A simple cron-like utility. No additional packages required. '''

from datetime import *
from time import *
import os

#name_of_file = input('Enter the name of your file: ')
name_of_file = 'sample.txt' # comment this line out later and uncomment the previous line
abspath = os.path.abspath(__file__)  # will get the path of the file that is running
directory_name = os.path.dirname(abspath)  # if the path is home/ichigo/cron-like/main.py, will change it home/ichigo/cron-like, (ie will move down the directory)
os.chdir(directory_name)  # will change current working directory to directory of the file, doing this because the input file is expected to be present in the same directory.
final_path = os.path.join(directory_name, name_of_file) #the directory to the file
'''

Reading from the file and splitting them in cron format

'''
with open(final_path, 'r+') as f:
    l = f.readlines()
    stripped = [i.strip().split(' ') for i in l]

'''

Set 'True' for values which have '*

'''

stripped = [[True if j == "*" else j for j in i] for i in stripped]

'''

j is initialized to 1, as in the mail

'''

j = 1

while True:
    '''
     
     Makes sure that the process starts at the beginning of a minute
    
    '''
    sleep(60 - datetime.now().second)

    current_time = datetime.now()

    '''
    
    If the current time matches any of the events then print the task name
    
    '''
    
    flag = 0
    for i in stripped:

        if((i[0] == True or int(i[0]) == current_time.minute) and
            (i[1] == True or int(i[1]) == current_time.hour) and
            (i[2] == True or int(i[2]) == current_time.day) and
            (i[3] == True or int(i[3]) == current_time.month) and
                (i[4] == True or int(i[4]) == (current_time.isoweekday()) % 7)):

            print('{}. {}'.format(str(j), i[5]))
            flag = 1
    '''  
    
    "j" would increment only when a task is performed and if mutiple tasks have to performed at the same time, then "j" would be the same for all of them 
    
    '''
    if flag == 1:
        j += 1

