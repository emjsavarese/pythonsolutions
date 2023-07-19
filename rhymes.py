#File: rhymes.py
#Author: Emily Savarese
#Purpose: Find perfect rhyming words to an input word based on phonemes and
#their stressed parts.
#CSC 120, Section 1C, Fall 2018



def read_file():
    #Read a file that is inputted and turn it into a dictionary of a list of lists.
    
    #Returns: a dictionary of words that correspond to a list of lists of phonemes.
    
    #Pre-condition: The input is a filename of words/phonemes.
    
    #Post-condition: "words" is a dictionary.
    
    filename=input()
    pfile=open(filename).readlines()
    words={}
    
    for i in range (len(pfile)):
        line=pfile[i].strip().split()
        word=line[0]
        if word not in words:
            words[word]=[]
            
        pronun=[]
        for j in range (1,len(line)):
            pronun.append(line[j])
        words[word].append(pronun)
        
    return words
    
        


def collect_rhymes(words):
    #Collects rhymes based on the stressed vowel matching, the unmatching phoneme before
    #and the matching phoenemes after.
    
    #Parameters: words is a dictionary.
    
    #Returns: A list of words that rhyme with a user-inputted word.

    #Pre-condition: The inputted word is in the file.

    #Post-condition: The return value is a list.
    
    
    user_word=input().upper()
    matched_words=[]
    for pronun in words[user_word]:
        
        pos1 = primary_stress_position(pronun)
        mini1 = create_mini_string(pronun,pos1)
        for word in words:
            
            for i in range (0,len(words[word])):
                pos2 = primary_stress_position(words[word][i])
                if pos2 != None:
                    if pronun[pos1] == words[word][i][pos2]:
                        mini2=create_mini_string(words[word][i],pos2)
                    
                        if (mini1 == mini2) and pronun[pos1-1] != words[word][i][pos2-1]:
                            matched_words.append(word)
                        
    return matched_words


            
        
def primary_stress_position(phoneme_list):
    #Finds the location of the primary stress position in a list of phonemes.

    #Parameters: phoeneme_list is a list of strings.

    #Returns: A number correlating to the position of the primary stressed phoneme.
    #returns None if not found.

    #Pre condition: phoeneme_list is a list.

    #Post condition: The return value is a number.

    
    for j in range(len(phoneme_list)):
        if "1" in phoneme_list[j]:
            return j    
    



def create_mini_string(phoneme_list,pos):
    #Creates a small list of strings. Sorry for the confusing name.

    #Parameters: Phoeneme_list is a list of strings, pos is a number value.

    #Pre-condition: Pos is not None.

    #Post-condition: mini_string is a list of strings.
    
    mini_string=[]
    for k in range (pos,len(phoneme_list)):
        mini_string.append(phoneme_list[k])
    return mini_string



def print_all(matched_words):
    #prints all elements in a list.

    #Parameters: matched_words is a list.
    
    for m in range (len(matched_words)):
        print(matched_words[m])
   
    


def main():
    #Runs the program rhymes by creating a dictionary and matching words to an input before
    #printing the matching words.
    
    words=read_file()
    matched_words=collect_rhymes(words)
    print_all(matched_words)


main()
