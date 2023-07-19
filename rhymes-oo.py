"""File: rhymes-oo.py
Author: Emily Savarese
Purpose: Find perfect rhyming words to an input word based on phonemes and
their stressed parts using objects.
#CSC 120, Section 1C, Fall 2018"""


import sys

class Word:
    def __init__(self,word,pronun):
        """establishes the object with the string name of itself,
        a list with one list of pronunciations. Its in a list
        for easy appending of other pronunciations."""
        self._word=word
        self._pronun=[pronun]

    def __str__(self):
        return self._word + " : " + str(self._pronun)

    def getrhyme(self,otherword):
        """returns True/False depending on whether or not a word is a perfect rhyme
        to another word. otherword is the word that this word is comparing
        against."""
        for pronun in self._pronun:
            #loops through the pronunciations of the first word
            pos1=self.primary_stress_pos(pronun)
            tomatch= self.create_mini_string(pronun,pos1)
            
            for pronun2 in otherword._pronun:
                #loops through the pronunciations for the second word
                pos2=otherword.primary_stress_pos(pronun2)
                
                if pos2!= None:
                    #as long as there is a stressed vowel within the second word
                    if pronun[pos1]==pronun2[pos2]:
                        tomatch2=otherword.create_mini_string(pronun2,pos2)
                        return ((tomatch==tomatch2) and (pronun[pos1 -1] !=pronun2[pos2-1]))
    
    
        

    def primary_stress_pos(self,pronun):
        """finds the position of the stress, if there is one.
        pronun is a list of strings (pronunciations for the word)"""
        for j in range(len(pronun)):
            if "1" in pronun[j]:
                return j


    def create_mini_string(self,pronun,pos):
        """creates a list of strings after a stressed vowel.
        this is used to compare to another ministring and see if they are
        perfect rhymes. pronun is a pronunciation of a word and pos
        is the position of the stressed vowel."""
        mini_string=[]
        for k in range (pos,len(pronun)):
            mini_string.append(pronun[k])
        return mini_string



class WordMap:
    def __init__(self):
        """establishes wordmap with an empty dictionary,
        which will later contain all words in the input file."""
        self._worddict={}


    def add_in_dict(self,word,pronun):
        if word._word not in self._worddict:
            self._worddict[word._word]=word
        else:
            #appends the pronunciation for the word to the word in the dictionary
            self._worddict[word._word]._pronun.append(pronun)


    def in_dict(self,newword):
        return (newword in self._worddict)
            

    def find_rhymes(self,tomatch):
        """finds all the words that are a perfect rhyme
        with the word tomatch"""
        for word in self._worddict:
            if self._worddict[tomatch].getrhyme(self._worddict[word]):
                print (word.lower())


    def __str__(self):
        toprint=[]
        for elem in self._worddict:
            toprint.append(str(self._worddict[elem]))
        return str(toprint)



def read_file(wordmap):
    """reads in an input file, erroring out when not available.
    wordmap is an object WordMap"""
    try:
        file=input()
        file=open(file)
    except:
        print("ERROR: Could not open file " +file)
        sys.exit(1)
    file=file.readlines()
    for i in range (len(file)):
        line=file[i].strip().split()
        word=line[0]
        pronun=[]
        for j in range (1,len(line)):
            pronun.append(line[j])
        wordobj=Word(word,pronun)
        wordmap.add_in_dict(wordobj,pronun)
    

def collect_rhymes(wordmap):
    """grabs the input from user_word and asserts that
    user_word is in the wordmap dictionary."""
    user_word=input().upper()
    try:
        assert wordmap.in_dict(user_word)
    except AssertionError:
        print("ERROR: the word input by the user is not in the pronunciation dictionary " + user_word.lower())
        sys.exit(1)
    wordmap.find_rhymes(user_word)
    
    
 
def main():
    wordmap=WordMap()
    read_file(wordmap)
    collect_rhymes(wordmap)





main()




    

    
