#! /usr/bin/env python3

from random import *

class Encryption:

    global checker
    global read_file
    global split_data
    global write_file
    global comparison
    global list_shuffle
    global read_db0_files
    global read_db1_files
    global list_generator

    def list_generator(count):
        random_list = []
        for i in range(count):
            if len(random_list)<4:
                random_list.append(i)
            else:
                break
        while True:
            if random_list[0] == 0 and random_list[-1] == 3:
                for i in range(2):
                    value0 = randint(0,3)
                    value1 = randint(0,3)

                    #swap the list values
                    random_list[value0],random_list[value1] = random_list[value1],random_list[value0]

            elif random_list[1] == 0 and random_list[2]:
                for i in range(2):
                    value0 = randint(0,3)
                    value1 = randint(0,3)

                    #swap the list values
                    random_list[value0],random_list[value1] = random_list[value1],random_list[value0]
            else:
                break
        return random_list

    def list_shuffle(value = [0,0,0,0]):
        #lowercase = 0
        #upercase = 1
        #number = 2
        #symbol = 3

        random_list  = []

        lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        numbers = ['1','2','3','4','5','6','7','8','9','0']
        symbols = [',','.','/',';',';','-','_','+','=','[',']','{','}','<','>','?','!','@','#','$','%','^','&','*','(',')']

        if value == [0,0,0,0]:
            value = list_generator(4)
        
        
        if value[0] == 0:
            if value[1] == 1:
                if value[2] == 2:
                    #0,1,2,3
                    random_list = lowercase+uppercase+numbers+symbols   
                else:
                    #0,1,3,2
                    random_list = lowercase+uppercase+symbols+numbers
            elif value[1] == 2:
                if value[2] == 1:
                    #0,2,1,3
                    random_list = lowercase+numbers+uppercase+symbols
                    
                else:
                    #0,2,3,1
                    random_list = lowercase+numbers+symbols+uppercase
            elif value[1] == 3:
                if value[2] == 1:
                    #0,3,1,2
                    random_list = lowercase+symbols+uppercase+numbers   
                else:
                    #0,3,2,1
                    random_list = lowercase+symbols+numbers+uppercase
        elif value[0] == 1:
            if value[1] == 0:
                if value[2] == 2:
                    #1,0,2,3
                    random_list = uppercase+lowercase+numbers+symbols
                else:
                    #1,0,3,2
                    random_list = uppercase+lowercase+symbols+numbers
            elif value[1] == 2:
                if value[2] == 0:
                    #1,2,0,3
                    random_list = uppercase+numbers+lowercase+symbols
                else:
                    #1,2,3,0
                    random_list = uppercase+numbers+symbols+lowercase 
            elif value[1] == 3:
                if value[2] == 0:
                    #1,3,0,2
                    random_list = uppercase+symbols+lowercase+numbers  
                else:
                    #1,3,2,0
                    random_list = uppercase+symbols+numbers+lowercase   
        elif value[0] == 2:
            if value[1] == 0:
                if value[2] == 1:
                    #2,0,1,3
                    random_list = numbers+lowercase+uppercase+symbols
                else:
                    #2,0,3,1
                    random_list = numbers+lowercase+symbols+uppercase
            elif value[1] == 1:
                if value[2] == 0:
                    #2,1,0,3
                    random_list = numbers+uppercase+lowercase+symbols   
                else:
                    #2,1,3,0
                    random_list = numbers+uppercase+symbols+lowercase
            elif value[1] == 3:
                if value[2] == 0:
                    #2,3,0,1
                    random_list = numbers+symbols+lowercase+uppercase
                else:
                    #2,3,1,0
                    random_list = numbers+symbols+uppercase+lowercase 
        elif value[0] == 3:
            if value[1] == 0:
                if value[2] == 2:
                    random_list = symbols+lowercase+numbers+uppercase
                else:
                    #3,0,1,2
                    random_list = symbols+lowercase+uppercase+numbers 
            elif value[1] == 2:
                if value[2] == 0:
                    #3,2,0,1
                    random_list = symbols+numbers+lowercase+uppercase 
                else:
                    random_list = symbols+numbers+uppercase+lowercase
            elif value[1] == 1:
                if value[2] == 0:
                    random_list = symbols+uppercase+lowercase+numbers
                else:
                    #3,1,2,0
                    random_list = symbols+uppercase+numbers+lowercase 
        #file_write('store_list.txt',value)
        
        return random_list,value

    def checker(random_list,list_shuffle_type,checking_data):
        encrypted_data = []
        for i in range(len(random_list)):
            for letter in checking_data:
                if letter == random_list[i]:
                    if len(encrypted_data) < len(checking_data):
                        encrypted_data.append(i)
                    else:
                        break
        if len(encrypted_data)< len(checking_data)+4:
            encrypted_data += list_shuffle_type

        return encrypted_data

    def split_data(data):
        length_of_data = len(data)
        data_list = []

        for letter in data:
            if len(data_list)<length_of_data:
                data_list.append(letter)

        random_list, list_shuffle_type = list_shuffle()
        encrypted_value = checker(random_list,list_shuffle_type,data)

        return encrypted_value

    def write_file(file_name,data):
        with open(file_name, 'w') as file:
            file.write(str(data))
            file.close()
    
    def read_file(file_name):
        with open(file_name, 'r') as file:
            data = file.read()
            file.close()
        return data

    def read_db0_files(file_name):
        new_list = []
        with open(file_name, 'r') as file:
            value = file.readline()
            """new_list.append(str(value[1]+value[2]))
            new_list.append(str(value[5]+value[6]))
            new_list.append(str(value[9]+value[10]))
            new_list.append(str(value[13]+value[14]))"""
            new_list.append(int(value[17]))
            new_list.append(int(value[20]))
            new_list.append(int(value[23]))
            new_list.append(int(value[26]))
            file.close()

        return new_list

    def read_db1_files(file_name):
        new_list = []
        with open(file_name, 'r') as file:
            value = file.readline()
            """new_list.append(str(value[1]))
            new_list.append(str(value[4]))
            new_list.append(str(value[7]))
            new_list.append(str(value[10]))
            new_list.append(str(value[13]+value[14]))
            new_list.append(str(value[17]+value[18]))
            new_list.append(str(value[21]+value[22]))
            new_list.append(str(value[25]+value[26]))"""
            new_list.append(int(value[29]))
            new_list.append(int(value[32]))
            new_list.append(int(value[35]))
            new_list.append(int(value[38]))
            
            file.close()
        return new_list
    def comparison(encrypted_data,file_name):
        new_list = []
        value = 0
        

        if file_name == "user_detail0.db":
            with open(file_name,'r') as file:
                value = file.readline()
                new_list.append(str(value[1]+value[2]))
                new_list.append(str(value[5]+value[6]))
                new_list.append(str(value[9]+value[10]))
                new_list.append(str(value[13]+value[14]))
                new_list.append(int(value[17]))
                new_list.append(int(value[20]))
                new_list.append(int(value[23]))
                new_list.append(int(value[26]))
                file.close()
            for i in range(len(new_list)):
                if isinstance(new_list[i],str):
                    value = int(new_list[i])
                    new_list[i] = value
            for count in range(len(encrypted_data)):
                if encrypted_data[count] != new_list[count]:
                    return 0
                else:
                    value += 1
            if len(encrypted_data) == value:
                return 1
        elif file_name == "user_detail1.db":
            with open(file_name,'r') as file:
                value = file.readline()
                new_list.append(str(value[1]))
                new_list.append(str(value[4]))
                new_list.append(str(value[7]))
                new_list.append(str(value[10]))
                new_list.append(str(value[13]+value[14]))
                new_list.append(str(value[17]+value[18]))
                new_list.append(str(value[21]+value[22]))
                new_list.append(str(value[25]+value[26]))
                new_list.append(int(value[29]))
                new_list.append(int(value[32]))
                new_list.append(int(value[35]))
                new_list.append(int(value[38]))
                file.close()
            for i in range(len(new_list)):
                if isinstance(new_list[i],str):
                    value = int(new_list[i])
                    new_list[i] = value
            for count in range(len(encrypted_data)):
                if encrypted_data[count] != new_list[count]:
                    return 0
                else:
                    value += 1
            if len(encrypted_data) == value:
                return 1

class Handler():

    global parser

    def parser(value = 0):
        if value == 0:
            with open('xmarine.db','w')as file:
                file.write(str(0))
                file.close()
        else:
            with open('xmarine.db','w')as file:
                file.write(str(1))
                file.close()

    def __init__(self,data,type):

        if type == "enc":
            encrypted_data =split_data(data)
            write_file('user_detail1.db',encrypted_data)

        elif type == "dec":
            value0 = read_db0_files("user_detail1.db")
            random_list, list_shuffle_type = list_shuffle(value0)
            encrypted_value = checker(random_list,list_shuffle_type,data)
            value2 = comparison(encrypted_value,"user_detail1.db")
            parser(value2)
            
            
        """else:
            value1 = read_db1_files(file_name)
            random_list, list_shuffle_type = list_shuffle(value1)
            encrypted_value = checker(random_list,list_shuffle_type,data)
            value2 = comparison(encrypted_value,file_name)
            parser(value2)"""