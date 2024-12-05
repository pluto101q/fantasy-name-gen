"""
generate stupid fantasy names from lists
let user choose how many pieces they want to use for compounds

so
1. ask how many names they want in the whole name (given and family names, let them decide how many of each)
2. ask user how many words they want in the first name and loop to end
3. bring in name files to arrays
4. loop for number of names
5. loop for number of words
6. pick random word and concatenate
7. once done say name
"""
import random

#validate numbers
def validateInt(question):
    valid = False
    while valid != True:
        variable = input(question)
        if variable.isnumeric():
            variable = int(variable)
            if variable <= 10 and variable > 0:
                valid = True
            else:
                print("Must between 1 and 10")
        else:
            print("Please only enter numeric characters")
    return variable

#validate with limited options
def validateGroup(question,opts):
    valid = False
    while valid != True:
        variable = input(question)
        if variable.isascii() and variable in opts:
            valid = True
        else:
            print("Please only enter ASCII characters and use one of the categories that already exists")
            print(*opts)
    return variable

#1
def getNumbers():
    given = validateInt("How many given names do you want to generate? ")
    family = validateInt("How many family names do you want to generate? ")
    order = validateGroup("Do you want given name or family name first? ",["given first","family first"])
    return given, family, order

#2
def numPerName(given,family):
    given_nums = [1]*given
    fam_nums = [1]*family
    ordinals = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for i in range(given):
        given_nums[i] = validateInt("How many words do you want to combine for the " + ordinals[i] + " given name? ")
    for i in range(family):
        fam_nums[i] = validateInt("How many words do you want to combine for the " + ordinals[i] + " family name? ")
    return given_nums, fam_nums

#3
def getWords():
    with open ("names.txt","r") as f:
        f_read = f.read()
        wordlist =  f_read.split("\n")
        if wordlist[0] == "":
            wordlist.pop(0)
    f.close()
    return wordlist

#4-7
def genNames(given,family,giv_nums,fam_nums,words,order):
    g_name = ""
    f_name = ""
    #loop for number of names
    for i in range(given):
        #loop for number of words
        for x in range(giv_nums[i]):
            #pick random word and concatenate
            g_name += random.choice(words)
        g_name += " "
    for i in range(family):
        #loop for number of words
        for x in range(fam_nums[i]):
            #pick random word and concatenate
            f_name += random.choice(words)
        f_name += " "
    #put in order
    if order == "given first":
        name = g_name + f_name
    else:
        name = f_name + g_name
    #capitalise and strip trailing whitespace
    name = name.title()
    name = name.strip()
    print(name)

#variables
given = 0
family = 0
order = ""
giv_nums = []
fam_nums = []
words = []

#main
given, family, order = getNumbers()
giv_nums, fam_nums = numPerName(given,family)
words = getWords()
genNames(given,family,giv_nums,fam_nums,words,order)
