#Alinea Grace Del Mundo
#MIDTERM EXAMINATION

def match_a():
    print ("Function match_a() \n")

    alea1 = input ("Enter 1st input:")
    alea2 = input ("Enter 2nd input:")
    alea3 = input ("Enter 3rd input:")

    alea22 = []
    alea33 = []
    alea11 = []

    
    for i in alea1:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                alea11.append(i)

    for i in alea2:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                alea22.append(i)

    for i in alea3:
        if len(i) != 1:      #exclude character
            if i == i[::-1]: #Palindrome checker
                alea33.append(i)

    print "1st output: ",len(alea11)
    print "2nd output: ",len(alea22)
    print "3rd output: ",len(alea33)

match_a()
print ("\n\n")






def front_x():
    print ("Function front_x()\n")

    alea1 = input ("Enter 1st input:")
    alea2 = input ("Enter 2nd input:")
    alea3 = input ("Enter 3rd input:")

    alea11 = []
    alea111 = []
    alea22 = []
    alea222 = []
    alea33 =[]
    alea333 = []

    for i in alea1:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            alea11.append(i)
        else:
            alea111.append(i) #new list of other strings
            
    print "1st output: ",sorted(alea11) + sorted(alea111) #to alphabetically arranged


    for i in alea2:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            alea22.append(i)
        else:
            alea222.append(i) #new list of other strings
            
    print "2nd output: ",sorted(alea22) + sorted(alea222) #to alphabetically arranged


    for i in alea3:
        if i.startswith('x'): #new list of strings that starts with 'x' from others
            alea33.append(i)
        else:
            alea333.append(i) #new list of other strings
            
    print "3rd output: ",sorted(alea33) + sorted(alea333) #to alphabetically arranged

    
front_x()
