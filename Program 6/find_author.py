# CS101
# Program 5
# Gregory Gagnon
# gmg634@mail.umkc.edu
# 
# PROBLEM:  Authorship Detection 
#
# ALGORITHM:
#
# 1) Define clean_up:
#    Convert the string to lowercase
#    Check the first and last index for punctuation and delete.
#
# 2) Define average_word_length:
#    Iterate through text (list of strings).
#    For each string, add string length to a character count variable.
#    Divide by length of list (total number of words)
#
# 3) Define type_token_ratio:
#    Iterate through text (list of strings) and create a set from the list of words.
#    Divide set length by list length to find TTR.
#
# 4) Define hapax_legomana_ratio:
#    Iterate through text (list of strings) and create a dictionary from the list of words.
#    Key will be word, value will be word count.
#    Create reverse dictionary of only "1" values.
#    Divide length of dictionary by length of text (list of strings).
#
# 5) Define split_on_separators:
#    Create a list of strings.
#    Append new strings to list each time a separator value is reached.
#    Separators are punctuation - !.,?
#
# 6) Define average_sentence_length:
#    Iterate through text (string), splitting on terminating punctuation, to create list of strings.
#    For each string (sentence), count words, splitting on " ".
#    Add word count to word count variable.
#    Divide by length of list (number of sentences).
#
# 7) Define average_sentence_complexity:
#    Iterate through text (string), splitting on terminating punctuation, to create list of strings.
#    Length of this list = number of sentences.
#    Iterate through text, splitting on ALL punctuation, including ",;:" along with "?!."
#    Length of this list = number of phrases.
#    Divide number of phrases by number of sentences
#
# 8) Define get_valid_filename:
#    Prompt with a loop to get the filename for analysis, and catch any invalid entries.
#
# 9) Define read_directory_name:
#    Prompt with a loop to get the directory for analysis, and catch any invalid entries.
#
# 10) Define compare_signatures:
#    Pass two signatures and weights to function.
#    Calculate weighted difference between signatures accordingly.
#
# 11) Define read_signature:
#   Using functions created, calculate the five linguistic features:
#    1. Average Word Length
#    2. Type-Token Ratio
#    3. Hapax Legomana Ratio
#    4. Average Sentence Length
#    5. Sentence Complexity
#
# 12) Compare the specified mystery text against the signatures in the specified directory.
# 13) Record the best score and the best author.
# 14) Output the results.
#
# ERROR HANDLING:
#
#
# OTHER COMMENTS: 



import os.path, math
import string

# 1) Define clean_up:
#    Convert the string to lowercase
#    Check the first and last index for punctuation and delete.
def clean_up(s):        
    ''' Return a version of string str in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. '''
    s = s.lower()
    new_s = s.strip(string.punctuation)
    return new_s

# 2) Define average_word_length:
#    Iterate through text (list of strings).
#    For each string, add string length to a character count variable.
#    Divide by length of list (total number of words)
def average_word_length(text):
    ''' Return the average length of all words in text. Do not
    include surrounding punctuation in words. 
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word.'''
    avg_int = 0
    word_count = 0
    char_count = 0
    line_count = 0
    for line in text:
        line_count += 1
        word_list = line.strip("\n").split(" ")
        word_count += len(word_list)
        clean_word_list = [clean_up(word) for word in word_list]
        for word in clean_word_list:
            char_count += len(word)
    avg_float = char_count/word_count
    return avg_float

# 3) Define type_token_ratio:
#    Iterate through text (list of strings) and create a set from the list of words.
#    Divide set length by list length to find TTR.
def type_token_ratio(text):
    ''' Return the type token ratio (TTR) for this text.
    TTR is the number of different words divided by the total number of words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word. '''
    ttr_list = []
    ttr_set = set()
    for line in text:
        word_list = line.strip("\n").split(" ")
        clean_word_list = [clean_up(word) for word in word_list]
        ttr_list.extend(clean_word_list)
        ttr_set.update(set(clean_word_list))
    if len(ttr_list) == 0:
        return 0
    ttr_float = len(ttr_set) / len(ttr_list)
    return ttr_float
  
# 4) Define hapax_legomana_ratio:
#    Iterate through text (list of strings) and create a dictionary from the list of words.
#    Key will be word, value will be word count.
#    Create reversed list of only "1" values.
#    Divide length of dictionary by length of text (list of strings).                
def hapax_legomana_ratio(text):
    ''' Return the hapax_legomana ratio for this text.
    This ratio is the number of words that occur exactly once divided
    by the total number of words.
    text is a list of strings each ending in \n.
    At least one line in text contains a word.'''

    hlr_dict = {}
    word_count = 0
    for line in text:
        word_list = line.strip("\n").split(" ")
        word_count += len(word_list)
        clean_word_list = [clean_up(word) for word in word_list]    
        for word in clean_word_list:
            hlr_dict[word] = hlr_dict.get(word, 0) + 1
    rev_hlr_list = [(y,x) for x,y in hlr_dict.items() if y==1]    
    if word_count == 0:
        return 0
    hlr_float = (len(rev_hlr_list)) / word_count          
    return hlr_float

# 5) Define split_on_separators:
#    Create a list of strings.
#    Append new strings to list each time a separator value is reached.
#    Separators are punctuation - !.,?
def split_on_separators(original, separators):
    ''' Return a list of non-empty, non-blank strings from the original string
    determined by splitting the string on any of the separators.
    separators is a string of single-character separators.'''
    sentence_list = []
    text_str = ""
    
    for char in original:
        if char not in separators:
            text_str += char
        else:
            text_str += char
            sentence_list.append(text_str.strip())
            text_str = ""
    if text_str.strip() != "":        
        sentence_list.append(text_str.strip())
    return sentence_list

# 6) Define average_sentence_length:
#    Iterate through text (string), splitting on terminating punctuation, to create list of strings.
#    For each string (sentence), count words, splitting on " ".
#    Add word count to word count variable.
#    Divide by length of list (number of sentences).                
def average_sentence_length(text):
    ''' Return the average number of words per sentence in text.
    text is guaranteed to have at least one sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. '''

    sentence_list = split_on_separators(text, "!?.")
    sentence_count = len(sentence_list)
    word_count = 0
    for sentence in sentence_list:
        sentence_len = len(sentence.split(" "))
        word_count += sentence_len
    if sentence_count == 0:
        return 0
    return word_count/sentence_count
        
    
# 7) Define average_sentence_complexity:
#    Iterate through text (string), splitting on terminating punctuation, to create list of strings.
#    Length of this list = number of sentences.
#    Iterate through text, splitting on ALL punctuation, including ",;:" along with "?!."
#    Length of this list = number of phrases.
#    Divide number of phrases by number of sentences
def avg_sentence_complexity(text):
    '''Return the average number of phrases per sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file.
    Phrases are substrings of a sentences separated by
    one or more of the following delimiters ,;: '''

    sentence_list = split_on_separators(text, "!?.")
    sentence_count = len(sentence_list)
    phrase_list = split_on_separators(text, "!?.;:,")    
    phrase_count = len(phrase_list)
    if sentence_count == 0:
        return 0
    return phrase_count/sentence_count
    
# 8) Define get_valid_filename:
#    Prompt with a loop to get the filename for analysis, and catch any invalid entries.
def get_valid_filename(prompt):
    
    '''Use prompt (a string) to ask the user to type the name of a file. If
     the file does not exist, keep asking until they give a valid filename.
     Return the name of that file.'''
    loop_bool = True
    while loop_bool:
        filename = input(prompt)
        if os.path.exists(filename):
            return filename
        else:
            print("That file does not exist.")
            print()

# 9) Define read_directory_name:
#    Prompt with a loop to get the directory for analysis, and catch any invalid entries.    
def read_directory_name(prompt):
    '''Use prompt (a string) to ask the user to type the name of a directory. If
    the directory does not exist, keep asking until they give a valid directory.
    '''
    loop_bool = True
    while loop_bool:
        dirname = input(prompt)
        if os.path.exists(dirname):
            return dirname
        else:
            print("That directory does not exist.")
            print()
        

# 10) Define compare_signatures:
#    Pass two signatures and weights to function.
#    Calculate weighted difference between signatures accordingly.   
def compare_signatures(sig1, sig2, weight):
    '''Return a non-negative real number indicating the similarity of two 
    linguistic signatures. The smaller the number the more similar the 
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0  : author name (a string)
    1  : average word length (float)
    2  : TTR (float)
    3  : Hapax Legomana Ratio (float)
    4  : average sentence length (float)
    5  : average sentence complexity (float)
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    '''

    total_1 = abs(sig1[1] - sig2[1]) * weight[1]
    total_2 = abs(sig1[2] - sig2[2]) * weight[2]
    total_3 = abs(sig1[3] - sig2[3]) * weight[3]
    total_4 = abs(sig1[4] - sig2[4]) * weight[4]
    total_5 = abs(sig1[5] - sig2[5]) * weight[5]

    result = total_1 + total_2 + total_3 + total_4 + total_5 
    return result
    

def read_signature(filename):
    '''Read a linguistic signature from filename and return it as 
    list of features. '''
    
    file = open(filename, 'r')
    # the first feature is a string so it doesn't need casting to float
    result = [file.readline()]
    # all remaining features are real numbers
    for line in file:
        result.append(float(line.strip()))
    return result
        

if __name__ == '__main__':
    
    prompt = 'enter the name of the file with unknown author: '
    mystery_filename = get_valid_filename(prompt)

    # readlines gives us the file as a list of strings each ending in '\n'
    file = open(mystery_filename, 'r')
    text = file.readlines()
    file.close() 
    # calculate the signature for the mystery file
    mystery_signature = [mystery_filename]
    mystery_signature.append(average_word_length(text))
    mystery_signature.append(type_token_ratio(text))
    mystery_signature.append(hapax_legomana_ratio(text))
    mystery_signature.append(average_sentence_length(text))
    mystery_signature.append(avg_sentence_complexity(text))
    
    weights = [0, 11, 33, 50, 0.4, 4]
    
    prompt = 'enter the path to the directory of signature files: '
    dir = read_directory_name(prompt)
    # every file in this directory must be a linguistic signature
    files = os.listdir(dir)

    # we will assume that there is at least one signature in that directory
    this_file = files[0]
    signature = read_signature('{} {}'.format(dir,this_file))
    best_score = compare_signatures(mystery_signature, signature, weights)
    best_author = signature[0]
    for this_file in files[1:]:
        signature = read_signature('{} {}'.format(dir,this_file))
        score = compare_signatures(mystery_signature, signature, weights)
        if score < best_score:
            best_score = score
            best_author = signature[0]
    print( "best author match: {} with score {}".format(best_author, best_score))
    
