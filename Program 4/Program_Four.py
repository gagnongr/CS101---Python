# CS101
# Program 4
# Gregory Gagnon
# gmg634@mail.umkc.edu
# 
# PROBLEM:  Ask user for the input of a .txt file. Scramble the text, maintaining first and last letters
#           of words, as well as punctuation and capitalization. Output is printed to the screen.          
#            
#
# ALGORITHM:
#
#   1. Build a function that formats the scrambled text for printing
#   2. Build a function that scrambles text of individual words per summary indications.
#   3. Prompt user for filename (e.g. input.txt), open file and assign to variable. Error control
#          for non-existent or incorrect filenames.
#       a. For each line of the text file, use the function built in step 1 to create lists of text.       
#           i. For each list of text created, using the function built in step 2, scramble the text
#               of each line.
#                   1. Function will operate on iterable list of strings, replacing each list
#                       object with the scrambled string.
#                   2. Function will keep punctuation and first/last letters intact.
#                   3. Print each string entry to screen.
#
#       b. Continue until all lines of the file have been read.
#   4. Close the file in use.
#
#
# ERROR HANDLING:
#   1. User is prompted to reenter filename if it is incorrect or missing.
#
#
# OTHER COMMENTS: 


#1. Function that formats the scrambled text for printing
def PrintScramble(input_txt):
    for para in lines:
        each = para.split(" ")
        for x in each:
             print(Scramble(x), end=" ")


#1. Function that does the Scrambling
def Scramble(word):

    # only words with 4+ letters can be scrambled
    if len(word) > 3:

        import random

        # converts word to list; initializes lists for scrambled word building
        word = list(word)
        scramble_list = [""] * len(word)
        mid_list = [] #list of middle letters of word

        # find the first letter
        for x in range(len(word)):
            if word[x].isalnum():
                first_tup = (word[x], x)
                break
            
        # find the last letter
        for x in range((len(word)-1), 0, -1):        
            if word[x].isalnum():
                last_tup = (word[x], x)
                break

        # find the punctuation and assign to correct positions
        for x in range(len(word)):
            if not word[x].isalnum():
                scramble_list[x] = word[x]

        # delete first and last letters from word
        del word[first_tup[1]]
        del word[last_tup[1]-1]

        # create list of middle letters of word
        for x in range(len(word)):
            if word[x].isalnum():
                mid_list += word[x]

        # assign first/last letters to correct positions
        scramble_list[first_tup[1]] = first_tup[0] 
        scramble_list[last_tup[1]] = last_tup[0] 

        # shuffle the middle letters and assign to empty strings in list
        random.shuffle(mid_list)
        for x in range(len(scramble_list)):
            if scramble_list[x] == "":
                scramble_list[x] = mid_list.pop()

        #rebuild word into a string
        scramble_str = "".join(scramble_list)            
        return scramble_str    

    # if three or less letters, return word unchanged
    else:
        return word



#2. Prompt user for filename
while True:
    input_str = input("What is the filename of the file you wish to open? ")
    print()
    try:
        input_file = open(input_str, "r")
        break
    except IOError:
        print("There was no file found with that filename.")
        print()

#3. Create list of words and print
lines = input_file.readlines()

PrintScramble(lines)
    
#4: Close the file
input_file.close()


