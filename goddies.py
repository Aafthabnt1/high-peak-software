import numpy as np
def sort_values(arr):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr
  

goodies = dict()                                                                      
input_file = open('sample_input.txt','r')                                                  

for line in input_file:                                                             #read line from input
    if line != '\n':                                                                #exclude empty lines
        a = line.split(":")                                                         #separate names of goodies and their cost
        a[1] = a[1][1:]                                                             #remove an unwanted space in cost string
        if a[1] != "":                                                              #remove lines which have no value
            if a[1][-1] == "\n":                                                    #remove endline 
                a[1] = a[1][:-1]
            goodies[a[0]] = int(a[1])                                               #add the name of goodies and their cost as integer to dictionery
            
            
input_file.close()                                                                  #close file input


noofEmp = goodies["Number of employees"]                                                        #extract the number of employees
del goodies["Number of employees"]                                                        #once extracted, key and value deleted


data = list(goodies.values())                                                            #convert dict to array for sorting
an_array = np.array(data)                                                                #then store in array variable
sortedValuesArray = sort_values(an_array)                                                #send the array values in sort_values function for sorting

#for i in range(len(sortedValuesArray)):
#    print ("%d" %sortedValuesArray[i])
                                                            #sort the cost in ascending order and add to a new list

lengthOfArray=len(sortedValuesArray)                                                                          #number of goodies
minDifference = sortedValuesArray[-1] - sortedValuesArray[0]                                                              #initialise minimum for worst case
goodieIndex=0                                                                                 #goodieIndex is used to store the index of the goodie with the lowest cost
for i in range((lengthOfArray-noofEmp)+1):                                                            #traverse through the costs
    difference = sortedValuesArray[i+(noofEmp-1)] - sortedValuesArray[i]                                                       #calculate difference between max and min
    if difference<minDifference:                                                                       #check if difference is lowest
        minDifference=difference                                                                       #if yes, update min value
        goodieIndex=i                                                                         #also update goodieIndex to store the index where min cost was found

        
output_file = open('sample_output.txt','w')                                                #write file       
output_file.write("The goodies selected for distribution are:\n")                   
output_file.write("\n")
for i in range(goodieIndex,goodieIndex+noofEmp):                                                              #traverse through the costs identified to come up with minimum difference
    for j in goodies.keys():                                                              #traverse through goodies                                                             
        if goodies[j] == sortedValuesArray[i]:                                                          #if costs match, goodies matched
            output_file.write(j+": ")                                               #print name of goodie
            output_file.write(str(goodies[j]))                                            #print cost of goodie
            output_file.write("\n")
            break
output_file.write("\n")
output_file.write("And the difference between the chosen goodie with highest price and the lowest price is ")
output_file.write(str(minDifference))                                                         #print the difference between max and min
output_file.close()