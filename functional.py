
# coding: utf-8

# only ints are summed (not float nor double)
def sum_stg_to_int(mylist=  ["around", "sun", " 1 ", " +5", "1.0", "-10"] ):
    
    lst = []
    #removing the signs and empty characters by replacing them with void  
    
    removetable = str.maketrans('', '', '+- ')
    # getting the int of the item from the list if the transformed item from the list represents a digit 
    
    lst = [int(s) for s in mylist if s.translate(removetable).isdigit()]

    return(sum(lst))

# Returning the persistance of the number 
def persistence(num = 4856):   

    count = 0
    digit = 1
    num = abs(num)
    while num // 10 !=0:  
        while num:
            digit *= num % 10
            num //= 10
        count += 1
        if digit == 0:
            break
        num = digit
        digit = 1
    return(count)

# summing the consecutive numbers of a list 

def sum_consecutives(ar = [5, 5, 5, 0, 0, 8, -8]):
    ar3 = []
    j = 1
    for i in range(len(ar) - 1):
        if ar[i] != ar[i+1]:
            ar3.append(ar[i]*j)
            j = 1           
        else:
            j += 1

    ar3.append(ar[-1]*j)
    return (ar3)

print(sum_stg_to_int())
print(persistence())
print(sum_consecutives())