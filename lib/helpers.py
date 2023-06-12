import random

def check_num(x):
    if x:
        try:
            x=int(x)
            return x
        except ValueError:
            print('Must input a number!')
            return None
    else:
        return None
    
# Random functions
def random_50():
    num = random.random()
    if num < 0.5:
        return True
    else: 
        return False

def random_33():
    num = random.random()
    if num < 0.33:
        return True
    else: 
        return False
   
def analyze_left(arr):
    
    result = []
    if 13 in arr:
        if 14 in arr:
            result.append([13,14])
            arr.remove(13)
            arr.remove(14)
        else:
            result.append([13])
            arr.remove(13)
        
    if 14 in arr:
        if 15 in arr:
            if 16 in arr:
                result.append([14,15,16])
                arr.remove(14)
                arr.remove(15)
                arr.remove(16)
            else:
                result.append([14,15])
                arr.remove(14)
                arr.remove(15)
        else:
            result.append([14])
            arr.remove(14)

    if 15 in arr:
        if 16 in arr:
            result.append([15,16])
            arr.remove(15)
            arr.remove(16)
        else:
            result.append([15])
            arr.remove(15)
    if 16 in arr:
        result.append([16])
        arr.remove(16)
    
    # if arr == []:
    #     print("Success!")
    #     print(result)
    return result

def produce_board(groups, pairs):

    
    #row 1
    string1 = f'|{pairs[0][0]}  |   |   |   |'
    if len(str({pairs[0][1]})) == 2:
        string1 = string1[:2] + str({pairs[0][1]}) + string1[4:]
    else:
        string1 = string1[:2] + str(pairs[0][1]) + string1[3:]
    string2 = '|   |   |   |   |'
    for group in groups:
        if 1 in group and 2 in group:
            string1 = string1[:4] + " " + string1[5:]
            string2 = string2[:4] + " " + string2[5:]
        if 2 in group and 3 in group:
            string1 = string1[:8] + " " + string1[9:]
            string2 = string2[:8] + " " + string2[9:]
        if 3 in group and 4 in group:
            string1 = string1[:12] + " " + string1[13:]
            string2 = string2[:12] + " " + string2[13:]
    

    
    #first horizontal row
    string3 = ' --- --- --- --- '
    for group in groups:
        if 1 in group and 5 in group:
            string3 = string3[:1] + "   " + string3[4:]
        if 2 in group and 6 in group:
            string3 = string3[:5] + "   " + string3[8:]
        if 3 in group and 7 in group:
            string3 = string3[:9] + "   " + string3[12:]
        if 4 in group and 8 in group:
            string3 = string3[:13] + "   " + string3[16:]
   

     #row 2
    string4 = '|   |   |   |   |'
    
    for group in groups:
        if 5 in group and 6 in group:
            string4 = string4[:4] + " " + string4[5:]
            
        if 6 in group and 7 in group:
            string4 = string4[:8] + " " + string4[9:]
            
        if 7 in group and 8 in group:
            string4 = string4[:12] + " " + string4[13:]
            
    

    #second horizontal
    string5 = ' --- --- --- --- '
    for group in groups:
        if 5 in group and 9 in group:
            string5 = string5[:1] + "   " + string5[4:]
        if 6 in group and 10 in group:
            string5 = string5[:5] + "   " + string5[8:]
        if 7 in group and 11 in group:
            string5 = string5[:9] + "   " + string5[12:]
        if 8 in group and 12 in group:
            string5 = string5[:13] + "   " + string5[16:]
    

    #row 3
    string6 = '|   |   |   |   |'
    
    for group in groups:
        if 9 in group and 10 in group:
            string6 = string6[:4] + " " + string6[5:]
            
        if 10 in group and 11 in group:
            string6 = string6[:8] + " " + string6[9:]
            
        if 11 in group and 12 in group:
            string6 = string6[:12] + " " + string6[13:]
    
  

    #second horizontal
    string7 = ' --- --- --- --- '
    for group in groups:
        if 13 in group and 9 in group:
            string7 = string7[:1] + "   " + string7[4:]
        if 14 in group and 10 in group:
            string7 = string7[:5] + "   " + string7[8:]
        if 15 in group and 11 in group:
            string7 = string7[:9] + "   " + string7[12:]
        if 16 in group and 12 in group:
            string7 = string7[:13] + "   " + string7[16:]
    
    
    #row 4
    string8 = '|   |   |   |   |'
    
    for group in groups:
        if 13 in group and 14 in group:
            string8 = string8[:4] + " " + string8[5:]
            
        if 14 in group and 15 in group:
            string8 = string8[:8] + " " + string8[9:]
            
        if 15 in group and 16 in group:
            string8 = string8[:12] + " " + string8[13:]
    

    #last horizontal row
    stringA = string2
    stringB = string4
    stringC = string6
    stringD = string8
    
    counter = 0
    first_row=[]
    second_row=[]
    third_row=[]
    fourth_row=[]

    while counter < len(groups):
        if groups[counter][0] < 5:
            first_row.append(counter)
            if len(str(pairs[counter][1])) == 2:
                if groups[counter][0]==1:
                    stringA = f"{stringA[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[4:]}"
                if groups[counter][0]==2:
                    print("hit 2")
                    stringA = f"{stringA[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[8:]}"
                if groups[counter][0]==3:
                    print("hit 3")
                    stringA = f"{stringA[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[12:]}"
                if groups[counter][0]==4:
                    print("hit 4")
                    stringA = f"{stringA[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[16:]}"
            else:
                if groups[counter][0]==1:
                    stringA = f"{stringA[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[3:]}"
                if groups[counter][0]==2:
                    stringA = f"{stringA[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[7:]}"
                if groups[counter][0]==3:
                    stringA = f"{stringA[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[11:]}"
                if groups[counter][0]==4:
                    stringA = f"{stringA[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[15:]}"

            #this is a first row change involving stringA
        elif groups[counter][0] < 9:
            if len(str(pairs[counter][1])) == 2:
                if groups[counter][0]==5:
                    stringB = f"{stringB[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[4:]}"
                if groups[counter][0]==6:
                    stringB = f"{stringB[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[8:]}"
                if groups[counter][0]==7:
                    stringB = f"{stringB[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[12:]}"
                if groups[counter][0]==8:
                    stringB = f"{stringB[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[16:]}"
            else:
                if groups[counter][0]==5:
                    stringB = f"{stringB[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[3:]}"
                if groups[counter][0]==6:
                    stringB = f"{stringB[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[7:]}"
                if groups[counter][0]==7:
                    stringB = f"{stringB[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[11:]}"
                if groups[counter][0]==8:
                    stringB = f"{stringB[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[15:]}"

            #this is a second row change involving stringB
            second_row.append(counter)
        elif groups[counter][0] < 13:
            if len(str(pairs[counter][1])) == 2:
                if groups[counter][0]==9:
                    stringC = f"{stringC[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[4:]}"
                if groups[counter][0]==10:
                    stringC = f"{stringC[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[8:]}"
                if groups[counter][0]==11:
                    stringC = f"{stringC[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[12:]}"
                if groups[counter][0]==12:
                    stringC = f"{stringC[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[16:]}"
            else:
                if groups[counter][0]==9:
                    stringC = f"{stringC[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[3:]}"
                if groups[counter][0]==10:
                    stringC = f"{stringC[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[7:]}"
                if groups[counter][0]==11:
                    stringC = f"{stringC[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[11:]}"
                if groups[counter][0]==12:
                    stringC = f"{stringC[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[15:]}"
            #this is a third row change involving stringC
            third_row.append(counter)
        else:
            if len(str(pairs[counter][1])) == 2:
                if groups[counter][0]==13:
                    stringD = f"{stringD[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[4:]}"
                if groups[counter][0]==14:
                    stringD = f"{stringD[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[8:]}"
                if groups[counter][0]==15:
                    stringD = f"{stringD[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[12:]}"
                if groups[counter][0]==16:
                    stringD = f"{stringD[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[16:]}"
            else:
                if groups[counter][0]==13:
                    if not pairs[counter][0]:
                        # stringD = f"{stringD[:1]}{str(pairs[counter][1])}{stringD[2:]}"
                        pass
                    else:
                        stringD = f"{stringD[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[3:]}"
                if groups[counter][0]==14:
                    if not pairs[counter][0]:
                        pass
                    else:
                        stringD = f"{stringD[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[7:]}"
                if groups[counter][0]==15:
                    if not pairs[counter][0]:
                        # stringD = f"{stringD[:9]}{str(pairs[counter][1])}{stringD[10:]}"
                        pass
                    else:
                        stringD = f"{stringD[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[11:]}"
                if groups[counter][0]==16:
                    if not pairs[counter][0]:
                        # stringD = f"{stringD[:13]}{str(pairs[counter][1])}{stringD[14:]}"
                        pass
                    else:
                        stringD = f"{stringD[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[15:]}"
            fourth_row.append(counter)
        counter+=1
    
    median="     \033[1;32;40m||\033[0;31;40m     "

    # print(f"{Fore.RED}{first_row}")
    # print(second_row)
    # print(third_row)
    # print(fourth_row)
    strings = ["\033[0;37;40m --- --- --- --- "+median+" --- --- --- --- ","\033[0;37;40m"+stringA+median+'|   |   |   |   |',"\033[0;37;40m"+string2+median+'| 1 | 2 | 3 | 4 |',
               "\033[0;37;40m"+string2+median+'|   |   |   |   |',"\033[0;37;40m"+string3+median+" --- --- --- --- ","\033[0;37;40m"+stringB+median+'|   |   |   |   |',
               "\033[0;37;40m"+string4+median+'| 5 | 6 | 7 | 8 |',"\033[0;37;40m"+string4+median+'|   |   |   |   |',"\033[0;37;40m"+string5+median+" --- --- --- --- ",
               "\033[0;37;40m"+stringC+median+'|   |   |   |   |',"\033[0;37;40m"+string6+median+'| 9 | 10| 11| 12|',"\033[0;37;40m"+string6+median+'|   |   |   |   |',
               "\033[0;37;40m"+string7+median+" --- --- --- --- ","\033[0;37;40m"+stringD+median+'|   |   |   |   |',"\033[0;37;40m"+string8+median+'| 13| 14| 15| 16|',
               "\033[0;37;40m"+string8+median+'|   |   |   |   |',"\033[0;37;40m"+' --- --- --- --- '+median+" --- --- --- --- "]
   
    for x in strings:
        print(x)
    return strings








def board_in_play(groups, pairs, solution={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' ',10:' ',11:' ',12:' ',13:' ',14:' ',15:' ',16:' '}):

    
    #row 1
    string1 = f'|{pairs[0][0]}  |   |   |   |'
    if len(str({pairs[0][1]})) == 2:
        string1 = string1[:2] + str({pairs[0][1]}) + string1[4:]
    else:
        string1 = string1[:2] + str(pairs[0][1]) + string1[3:]
    string2A = '|   |   |   |   |'
    string2 = f'| {solution[1]} | {solution[2]} | {solution[3]} | {solution[4]} |'
    for group in groups:
        if 1 in group and 2 in group:
            string1 = string1[:4] + " " + string1[5:]
            string2 = string2[:4] + " " + string2[5:]
            string2A = string2A[:4] + " " + string2A[5:]
        if 2 in group and 3 in group:
            string1 = string1[:8] + " " + string1[9:]
            string2 = string2[:8] + " " + string2[9:]
            string2A = string2A[:8] + " " + string2A[9:]
        if 3 in group and 4 in group:
            string1 = string1[:12] + " " + string1[13:]
            string2 = string2[:12] + " " + string2[13:]
            string2A = string2A[:12] + " " + string2A[13:]
    
    # string2A = '| 3 | 4 | 5 | 6 |'
    # need to write code to add formatting to string 2
    # string2 = "| \033[1;34;40m"+solution[1]+"\033[1;37;40m | \033[1;34;40m"+solution[2]+"\033[1;37;40m | \033[1;34;40m"+solution[3]+"\033[1;37;40m | \033[1;34;40m"+solution[4]+"\033[1;37;40m |"
    # string2 = string2[:2]+"\033[1;34;40m" + string2[2] + "\033[1;37;40m" + string2[3:6] +"\033[1;34;40m" + string2[6] + "\033[1;37;40m" + string2[7:10] + "\033[1;34;40m" + string2[10] + "\033[1;37;40m" + string2[11:14] + "\033[1;34;40m" + string2[14] + "\033[1;37;40m" + string2[15:]
    # print(string2) 
    string2 = add_color(string2)
    
    #first horizontal row
    string3 = ' --- --- --- --- '
    for group in groups:
        if 1 in group and 5 in group:
            string3 = string3[:1] + "   " + string3[4:]
        if 2 in group and 6 in group:
            string3 = string3[:5] + "   " + string3[8:]
        if 3 in group and 7 in group:
            string3 = string3[:9] + "   " + string3[12:]
        if 4 in group and 8 in group:
            string3 = string3[:13] + "   " + string3[16:]
   

     #row 2
    string4 = f'| {solution[5]} | {solution[6]} | {solution[7]} | {solution[8]} |'
    string4A = '|   |   |   |   |'
    for group in groups:
        if 5 in group and 6 in group:
            string4 = string4[:4] + " " + string4[5:]
            string4A = string4A[:4] + " " + string4A[5:]
        if 6 in group and 7 in group:
            string4 = string4[:8] + " " + string4[9:]
            string4A = string4A[:8] + " " + string4A[9:]
        if 7 in group and 8 in group:
            string4 = string4[:12] + " " + string4[13:]
            string4A = string4A[:12] + " " + string4A[13:]
    
    string4 = add_color(string4)
    #second horizontal
    string5 = ' --- --- --- --- '
    for group in groups:
        if 5 in group and 9 in group:
            string5 = string5[:1] + "   " + string5[4:]
        if 6 in group and 10 in group:
            string5 = string5[:5] + "   " + string5[8:]
        if 7 in group and 11 in group:
            string5 = string5[:9] + "   " + string5[12:]
        if 8 in group and 12 in group:
            string5 = string5[:13] + "   " + string5[16:]
    

    #row 3
    string6 = f'| {solution[9]} | {solution[10]} | {solution[11]} | {solution[12]} |'
    string6A = '|   |   |   |   |'
    
    for group in groups:
        if 9 in group and 10 in group:
            string6 = string6[:4] + " " + string6[5:]
            string6A = string6A[:4] + " " + string6A[5:]
        if 10 in group and 11 in group:
            string6 = string6[:8] + " " + string6[9:]
            string6A = string6A[:8] + " " + string6A[9:]
        if 11 in group and 12 in group:
            string6 = string6[:12] + " " + string6[13:]
            string6A = string6A[:12] + " " + string6A[13:]
    
    string6 = add_color(string6)

    #second horizontal
    string7 = ' --- --- --- --- '
    for group in groups:
        if 13 in group and 9 in group:
            string7 = string7[:1] + "   " + string7[4:]
        if 14 in group and 10 in group:
            string7 = string7[:5] + "   " + string7[8:]
        if 15 in group and 11 in group:
            string7 = string7[:9] + "   " + string7[12:]
        if 16 in group and 12 in group:
            string7 = string7[:13] + "   " + string7[16:]
    
    
    #row 4
    string8 = f'| {solution[13]} | {solution[14]} | {solution[15]} | {solution[16]} |'
    string8A = '|   |   |   |   |'
    for group in groups:
        if 13 in group and 14 in group:
            string8 = string8[:4] + " " + string8[5:]
            string8A = string8A[:4] + " " + string8A[5:]
        if 14 in group and 15 in group:
            string8 = string8[:8] + " " + string8[9:]
            string8A = string8A[:8] + " " + string8A[9:]
            
        if 15 in group and 16 in group:
            string8 = string8[:12] + " " + string8[13:]
            string8A = string8A[:12] + " " + string8A[13:]
        
    string8 = add_color(string8)

    #last horizontal row
    stringA = string2A
    stringB = string4A
    stringC = string6A
    stringD = string8A
    
    counter = 0
    first_row=[]
    second_row=[]
    third_row=[]
    fourth_row=[]

    while counter < len(groups):
        if groups[counter][0] < 5:
            first_row.append(counter)
            if len(str(pairs[counter][1])) == 2:
                if groups[counter][0]==1:
                    stringA = f"{stringA[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[4:]}"
                if groups[counter][0]==2:
                    print("hit 2")
                    stringA = f"{stringA[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[8:]}"
                if groups[counter][0]==3:
                    print("hit 3")
                    stringA = f"{stringA[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[12:]}"
                if groups[counter][0]==4:
                    print("hit 4")
                    stringA = f"{stringA[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[16:]}"
            else:
                if groups[counter][0]==1:
                    stringA = f"{stringA[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[3:]}"
                if groups[counter][0]==2:
                    stringA = f"{stringA[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[7:]}"
                if groups[counter][0]==3:
                    stringA = f"{stringA[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[11:]}"
                if groups[counter][0]==4:
                    stringA = f"{stringA[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringA[15:]}"

            #this is a first row change involving stringA
        elif groups[counter][0] < 9:
            if len(str(pairs[counter][1])) == 2:
                if groups[counter][0]==5:
                    stringB = f"{stringB[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[4:]}"
                if groups[counter][0]==6:
                    stringB = f"{stringB[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[8:]}"
                if groups[counter][0]==7:
                    stringB = f"{stringB[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[12:]}"
                if groups[counter][0]==8:
                    stringB = f"{stringB[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[16:]}"
            else:
                if groups[counter][0]==5:
                    stringB = f"{stringB[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[3:]}"
                if groups[counter][0]==6:
                    stringB = f"{stringB[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[7:]}"
                if groups[counter][0]==7:
                    stringB = f"{stringB[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[11:]}"
                if groups[counter][0]==8:
                    stringB = f"{stringB[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringB[15:]}"

            #this is a second row change involving stringB
            second_row.append(counter)
        elif groups[counter][0] < 13:
            if len(str(pairs[counter][1])) == 2:
                if groups[counter][0]==9:
                    stringC = f"{stringC[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[4:]}"
                if groups[counter][0]==10:
                    stringC = f"{stringC[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[8:]}"
                if groups[counter][0]==11:
                    stringC = f"{stringC[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[12:]}"
                if groups[counter][0]==12:
                    stringC = f"{stringC[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[16:]}"
            else:
                if groups[counter][0]==9:
                    stringC = f"{stringC[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[3:]}"
                if groups[counter][0]==10:
                    stringC = f"{stringC[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[7:]}"
                if groups[counter][0]==11:
                    stringC = f"{stringC[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[11:]}"
                if groups[counter][0]==12:
                    stringC = f"{stringC[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringC[15:]}"
            #this is a third row change involving stringC
            third_row.append(counter)
        else:
            if len(str(pairs[counter][1])) == 2:
                if groups[counter][0]==13:
                    stringD = f"{stringD[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[4:]}"
                if groups[counter][0]==14:
                    stringD = f"{stringD[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[8:]}"
                if groups[counter][0]==15:
                    stringD = f"{stringD[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[12:]}"
                if groups[counter][0]==16:
                    stringD = f"{stringD[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[16:]}"
            else:
                if groups[counter][0]==13:
                    if not pairs[counter][0]:
                        # stringD = f"{stringD[:1]}{str(pairs[counter][1])}{stringD[2:]}"
                        pass
                    else:
                        stringD = f"{stringD[:1]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[3:]}"
                if groups[counter][0]==14:
                    if not pairs[counter][0]:
                        pass
                    else:
                        stringD = f"{stringD[:5]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[7:]}"
                if groups[counter][0]==15:
                    if not pairs[counter][0]:
                        # stringD = f"{stringD[:9]}{str(pairs[counter][1])}{stringD[10:]}"
                        pass
                    else:
                        stringD = f"{stringD[:9]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[11:]}"
                if groups[counter][0]==16:
                    if not pairs[counter][0]:
                        # stringD = f"{stringD[:13]}{str(pairs[counter][1])}{stringD[14:]}"
                        pass
                    else:
                        stringD = f"{stringD[:13]}{pairs[counter][0]}{str(pairs[counter][1])}{stringD[15:]}"
            fourth_row.append(counter)
        counter+=1
    
    median="     \033[1;32;40m||\033[0;31;40m     "

    # print(f"{Fore.RED}{first_row}")
    # print(second_row)
    # print(third_row)
    # print(fourth_row)
    strings = ["\033[0;37;40m --- --- --- --- "+median+" --- --- --- --- ",
               "\033[0;37;40m"+stringA+median+'|   |   |   |   |',
               "\033[0;37;40m"+string2+median+'| 1 | 2 | 3 | 4 |',
               "\033[0;37;40m"+string2A+median+'|   |   |   |   |',
               "\033[0;37;40m"+string3+median+" --- --- --- --- ",
               "\033[0;37;40m"+stringB+median+'|   |   |   |   |',
               "\033[0;37;40m"+string4+median+'| 5 | 6 | 7 | 8 |',
               "\033[0;37;40m"+string4A+median+'|   |   |   |   |',
               "\033[0;37;40m"+string5+median+" --- --- --- --- ",
               "\033[0;37;40m"+stringC+median+'|   |   |   |   |',
               "\033[0;37;40m"+string6+median+'| 9 | 10| 11| 12|',
               "\033[0;37;40m"+string6A+median+'|   |   |   |   |',
               "\033[0;37;40m"+string7+median+" --- --- --- --- ",
               "\033[0;37;40m"+stringD+median+'|   |   |   |   |',
               "\033[0;37;40m"+string8+median+'| 13| 14| 15| 16|',
               "\033[0;37;40m"+string8A+median+'|   |   |   |   |',
               "\033[0;37;40m"+' --- --- --- --- '+median+" --- --- --- --- \033[0;37;40m"]
   
    for x in strings:
        print(x)
    return strings


def add_color(str):
    new_string = str[:2]+"\033[1;34;40m" + str[2] + "\033[1;37;40m" + str[3:6] +"\033[1;34;40m" + str[6] + "\033[1;37;40m" + str[7:10] + "\033[1;34;40m" + str[10] + "\033[1;37;40m" + str[11:14] + "\033[1;34;40m" + str[14] + "\033[1;37;40m" + str[15:]
    return new_string

def games_menu():
    print("What would you like to do next?")
    print('\033[1;32;40m|To examine a game (see the board, review or add notes) type the game number|\n')
    print('\033[1;32;40m|To see another user\'s results, type "users"|\n')
    print('\033[1;32;40m|To exit type "exit" |\033[0;37;40m \n')
    return input("Type your choice here: ")


def process_solution(dict):
    keys = list(dict.keys())
    new_dict={}
    for k in keys:
        new_dict[int(k)]=dict[k]
    return new_dict
