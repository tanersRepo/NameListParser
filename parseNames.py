from collections import Counter

fullname_list = []
lineOfData = []
name_list = []
firstname_list = []
lastname_list = []
unique_list = []
first_temp_list = []
last_temp_list = []
N = 25
modified_list = []
tmp = ""
firstname_modified_list = []
lastname_modified_list = []

with open("test-data.txt") as inpFile: #open input file
    lineOfData = inpFile.readlines() #read file line by line
    #numOfLines = len(lineOfData) #number of lines in file
    for line in lineOfData:
        if line[0].isupper() and line[0].isalpha():
            fullname_list = line.split(",")[0] + ", " + line.split(" ")[1]
            name_list.append(fullname_list)
            lastname_list.append(line.split(",")[0]) #last name_list = first element of the split by comma
            firstname_list.append(line.split(" ")[1]) #first name_list = second element of the split by space
            
    print("The number of unique full names is: {}".format(len(list(set(name_list))))) # using a set removes duplicates - 49,157 name_lists

    print("The number of unique last names is: {}".format(len(list(set(lastname_list)))))

    print("The number of unique first names is: {}".format(len(list(set(firstname_list)))))
    
    print("The 10 most common last names are: ", Counter(lastname_list).most_common(10)) # 10 most common last name_lists and number of occurences
    print("\n")
    print("The 10 most common first names are: ", Counter(firstname_list).most_common(10)) # 10 most common first name_lists and number of occurrences
    print("\n")

        #add every first and last name in name_list to their own list. -- check if the current first name or last name has been encountered in the corresponding list up until the current name. - if not, add to unique list
    for j in range(0,len(name_list)):
        last_temp_list.append(name_list[j].split(",")[0]) # temporary list of first name_lists encountered so far.
        first_temp_list.append(name_list[j].split(" ")[1]) # temporary list of last name_lists encountered so far.
        if firstname_list[j] not in first_temp_list[:j-1] and firstname_list[j] not in last_temp_list[:j-1] and len(unique_list) < N:
            unique_list.append(name_list[j])
    print("The unique list of names are: ", unique_list)
    print("\n")

    #put the first and last names into their own respective lists.  modify each element in the first name list, swapping each index's value - leave the last names in the same index spot
    for i in range(0, len(unique_list)):
        lastname_modified_list.append(unique_list[i].split(",")[0])
        firstname_modified_list.append(unique_list[i].split(" ")[1])
        tmp = firstname_modified_list[i]
        firstname_modified_list[i] = firstname_modified_list[i-1]
        firstname_modified_list[i-1] = tmp
    for items in range(0, len(lastname_modified_list)):
        modified_list.append(lastname_modified_list[items] + ", " + firstname_modified_list[items])
    print("The modified list of names are: ", modified_list)
    print("\n")

#### swapping 2 elements in a list with eachother
##    tmp = my_list[index]
##my_list[index] = my_list[index + 1]
##my_list[index + 1] = tmp
        
##    for word in firstname_list:
##        if word in lastname_list_counter:
##            lastname_list_counter[word] += 1
##        else:
##            lastname_list_counter[word] = 1
##    print(lastname_list_counter)
##    common_last = sorted(lastname_list_counter, key = lastname_list_counter.get, reverse = True)
##    print(common_last)
##    top_10 = common_last[:10]
##    print(top_10) # only prints top 10 last name_lists - (missing number of occurrences), need to use Counter
                    
    #print("The total number of first names is {}".format(len(firstname_list)))
