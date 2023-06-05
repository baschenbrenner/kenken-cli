import random
import colorama
from colorama import Fore, Style

def create_board():
    def find_missing(arr):
        start = [1,2,3,4]
        for x in arr:
            start.remove(x)
        return start[0]

    board = []
    row1 = []
    row1.append(random.randrange(1,5))
    while len(row1)<4:
        curr_length = len(row1)
        if (curr_length == 3):
                num = find_missing(row1)
                row1.append(num)
        new_num = random.randrange(1,5)
        while new_num not in row1:
            row1.append(new_num)
            new_num = random.randrange(1,5)

    board.append(row1)
    
    row2=[]
    finished = False
    while finished == False:

        while len(row2)<4:
            new_num = random.randrange(1,5)
            curr_length = len(row2)
            while curr_length != 4 and row1[curr_length] != new_num:
                if (new_num not in row2):
                    row2.append(new_num) 
                    curr_length+=1
                elif (curr_length == 3):
                    num = find_missing(row2)
                    row2.append(num)
                    curr_length+=1
                new_num = random.randrange(1,5)

        if row2[3] == row1[3]:
            row2=[]
        else:
            finished=True
            
    board.append(row2)
    

    finished = False
    row3=[]
    while finished == False:
        
        while len(row3)<4:
            new_num = random.randrange(1,5)
            curr_length = len(row3)
            while (curr_length != 4) and (row1[curr_length] != new_num) and (row2[curr_length] != new_num):
                if curr_length == 1:
                    check_array = [*set([row1[0],row1[1],row2[0],row2[1],row3[0]])]
                    if len(check_array) == 3:
                        row3.append(find_missing(check_array))
                        curr_length+=1
                    else:
                        if new_num not in row3:
                            row3.append(new_num)
                            curr_length+=1

                elif new_num not in row3:
                    row3.append(new_num)
                    curr_length+=1
                elif (curr_length == 3):
                    num = find_missing(row3)
                    row3.append(num)
                    curr_length+=1
                new_num = random.randrange(1,5)

                if curr_length==2 and sorted([row3[0], row3[1], row1[2], row2[2]]) == [1,2,3,4]:
                    row3 = []
                    curr_length=0

        
        if row3[3]==row1[3] or row3[3]==row2[3]:
                row3 = []
        else:
            finished = True

        



    board.append(row3)
    # print("------------------")
    # for row in board:
    #     print(row)
    row4 = [find_missing([row1[0],row2[0],row3[0]]),find_missing([row1[1],row2[1],row3[1]]), find_missing([row1[2],row2[2],row3[2]]), find_missing([row1[3],row2[3],row3[3]])]
    board.append(row4)
    # print("here's your board!")
    # print("------------------")
    # for row in board:
    #     print(row)
    

    board_rep = {}
    counter = 1 
    for x in range(4):
        for y in range(4):
            board_rep[counter]=board[x][y]
            counter+=1
    return (board, board_rep)
    




        
#groupings - start with 1, try 2, if not 2 then add 5, then try 9  if 9, then done, if not 9 try 6. else try 5, 

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


def produce_groupings():
    group1 = [1]

    #groupings - start with 1, try 2, if not 2 then add 5, then try 9  if 9, then done, if not 9 try 6. else try 5, 

    if random_50():
        group1.append(2)
        if random_33():
            group1.append(5)
        elif random_33():
            group1.append(6)
        else:
            if random_33():
                group1.append(3)
    else:
        group1.append(5)
        if random_33():
            group1.append(9)



    group2 = []
    if 2 in group1:
        if 3 in group1:
            group2.append(4)
            group2.append(8)
        else:
            group2.append(3)
            if random_50():
                group2.append(4)
            else:
                group2.append(7)
    else:
        group2.append(2)
        if random_50():
            group2.append(3)
        else:
            group2.append(6)
    result = [group1,group2]
    flattened = [num for sublist in result for num in sublist]
    group3=[]
    if 3 not in flattened:
        group3.append(3)
        group3.append(4)
        if random_50():
            if 7 not in flattened:
                group3.append(7)
    elif 4 not in flattened:
        group3.append(4)
        group3.append(8)
    elif 5 not in flattened:
        group3.append(5)
        if 6 not in flattened:
            group3.append(6)
        else:
            group3.append(9)
    elif 6 not in flattened:
        group3.append(6)
        group3.append(7)



    result = [group1,group2,group3]
    flattened = [num for sublist in result for num in sublist]

    group4=[]
    if 5 not in flattened:
        group4.append(5)
        if 6 not in flattened:
            group4.append(6)
        else:
            group4.append(9)
    elif 6 not in flattened:
        group4.append(6)
        if 7 not in flattened:
            group4.append(7)
        else:
            group4.append(10)
    elif 7 not in flattened:
        group4.append(7)
        if 8 not in flattened:
            group4.append(8)
        else:
            group4.append(11)
    elif 8 not in flattened:
        group4.append(8)
        group4.append(12)
        

    result = [group1,group2,group3, group4]
    flattened = [num for sublist in result for num in sublist]
    # print(sorted(flattened))

    group5=[]
    if 9 not in flattened:
        group5.append(9)
        if 10 not in flattened:
            group5.append(10)
            group5.append(14)
        else:
            group5.append(13)
    elif 10 not in flattened:
        group5.append(10)
        if 11 not in flattened:
            group5.append(11)
        else:
            group5.append(14)


    result = [group1,group2,group3, group4, group5]
    flattened = [num for sublist in result for num in sublist]

    group6=[]
    if 11 not in flattened:
        group6.append(11)
        if 12 not in flattened:
            group6.append(12)
        else:
            group6.append(15)
    elif 12 not in flattened:
        group6.append(12)
        group6.append(16)

    result = [group1,group2,group3, group4, group5, group6]
    flattened = [num for sublist in result for num in sublist]

    left =[]
    for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]:
            
        if x not in flattened:
            left.append(x)
    
    final_groupings = analyze_left(left)
    for l in final_groupings:
        result.append(l)

    # flattened = [num for sublist in result for num in sublist]
    # if len(flattened)==len(set(flattened)):
    #     print("TRUE!")
    # else:
    #     print("Something went wrong")
    if [] in result:
        result.remove([])
    return result

# counter = 0
# while counter < 5:
#     print(produce_groupings())
#     counter+=1

# group1 = produce_grouping1()
# print(group1)

#create_board produces a tuple with board (array of arrays) and board dict
#produce groupings produces an array of arrays
#random operations produces an array of tuples with operation and result

def random_operations(tup, groups):
    result=[]
    options =["+","-","x","/"]
    counter = 0
    while counter < len(groups):
    #   print(groups[counter])
       if len(groups[counter]) == 1:
           result.append((" ", tup[1][groups[counter][0]]))
       elif len(groups[counter]) == 2:
           op = random.choice(options)
           if op == "+":
               end = tup[1][groups[counter][0]] + tup[1][groups[counter][1]]
               result.append(("+", end))
           elif op == "-":
               if tup[1][groups[counter][0]] - tup[1][groups[counter][1]] > 0:
                    end = tup[1][groups[counter][0]] - tup[1][groups[counter][1]]
                    result.append(("-", end))
               else:
                   end = tup[1][groups[counter][1]] - tup[1][groups[counter][0]]
                   result.append(("-", end))
           elif op == "x":
               end = tup[1][groups[counter][0]] * tup[1][groups[counter][1]]
               result.append(("x", end))
           elif op == "/":
               if tup[1][groups[counter][0]]/tup[1][groups[counter][1]] == 2:
                   end = 2
                   result.append(("/", end))
               elif tup[1][groups[counter][1]]/tup[1][groups[counter][0]] == 2:
                   end = 2
                   result.append(("/", end))
               elif tup[1][groups[counter][1]]/tup[1][groups[counter][0]] == 3:
                   end = 3
                   result.append(("/", end))
               elif tup[1][groups[counter][0]]/tup[1][groups[counter][1]] == 3:
                   end = 3
                   result.append(("/", end))
               elif tup[1][groups[counter][1]]/tup[1][groups[counter][0]] == 4:
                   end = 4
                   result.append(("/", end))
               elif tup[1][groups[counter][0]]/tup[1][groups[counter][1]] == 4:
                   end = 4
                   result.append(("/", end))
               else:
                   end = tup[1][groups[counter][0]] * tup[1][groups[counter][1]]
                   result.append(("x", end))
       elif len(groups[counter]) == 3:
           if random_50():
               end = tup[1][groups[counter][0]] * tup[1][groups[counter][1]]*tup[1][groups[counter][2]]
               result.append(("x", end))
           else:
               end = tup[1][groups[counter][0]] + tup[1][groups[counter][1]]+tup[1][groups[counter][2]]
               result.append(("+", end))

       counter += 1

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
                    print("hit 1")
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


    # print(Fore.RED + 'This text is red in color')
    # print(Fore.BLUE + 'This text is blue in color')
    # print(Fore.GREEN + 'This is GREEN!')
               
           
           
           




board = create_board()


groupings = produce_groupings()

print(groupings)



pairs = random_operations(board, groupings)

print(pairs)

produce_board(groupings, pairs)




