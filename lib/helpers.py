import random
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


