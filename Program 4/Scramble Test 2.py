def FirstLetter(word):
    """returns a tuple of the first letter and its index"""
    for x in range(len(word)):
        if word[x].isalnum():
            first_tup = (word[x], x)
            break   
    return first_tup

def LastLetter(word):
    """returns a tuple of the last letter and its index"""
    for x in range((len(word)-1), 0, -1):        
        if word[x].isalnum():
            last_tup = (word[x], x)
            break
    return last_tup

def Scramble(word):

    # only words with 4+ letters can be scrambled
    if len(word) > 3:

        import random

        # converts word to list; initializes lists for scrambled word building
        word = list(word)
        scramble_list = [""] * len(word)
        mid_list = [] #list of middle letters of word

        # find the punctuation and assign to correct positions
        for x in range(len(word)):
            if not word[x].isalnum():
                scramble_list[x] = word[x]

        # assign first/last letters to correct positions
        scramble_list[FirstLetter(word)[1]] = FirstLetter(word)[0] 
        scramble_list[LastLetter(word)[1]] = LastLetter(word)[0]

        # delete first and last letters from word
        del word[FirstLetter(word)[1]]
        del word[LastLetter(word)[1]-1]

        # create list of middle letters of word
        for x in range(len(word)):
            if word[x].isalnum():
                mid_list += word[x]

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
