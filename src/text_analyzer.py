import locale
locale.setlocale(locale.LC_ALL, "en_US")
from sys import argv
import os

def number_of_words(inp):    #find number of words in given text
    words=inp.split(" ")
    words+=inp.split("\n")
    number_of_words2=len(words)-1
    return number_of_words2

def number_of_sentences(inp):   #find number of sentences in given text
    sentences=inp.count(".")+inp.count("!")+inp.count("?")
    sentences+=inp.count("...")
    sentences-=inp.count("...")*3
    return sentences

def average_number_of_words_per_sentence(inp): #find number of words per sentence
    words=number_of_words(inp)
    sentences=number_of_sentences(inp)
    if sentences>0 :
        average_number_of_words=words/sentences  #by dividing them
        return average_number_of_words
    else :
        return 0.00

def number_of_characters(inp):
    character= len(inp) #finding length of the text
    return character

def number_of_characters_word(inp):
    t = inp.lower() #finding length of the letters in given text
    list1 = t.split()
    punctuations = "!""#$%&()*+,./:;<=>?@[\]^_`{|}~"
    list2 = []
    characters=0
    for w in list1: #excluding punctuations if they not including word
        x = w.strip(punctuations)
        if x[-1] == "'":
            x = x[:-1]

        list2.append(x)
    for e in list2:
        characters+=len(e)
    return characters

def shortest_word(inp):
    t=inp.lower()
    list1=t.split()
    punctuations="!""#$%&()*+,./:;<=>?@[\]^_`{|}~"
    list2 = []
    for w in list1:
        x = w.strip(punctuations)
        if x[-1] == "'":
            x=x[:-1]

        list2.append(len(x))

    list2.sort(reverse=True)
    a=list2[-1]
    list3=[] #all shortest words
    list4=[] #frequency of shortest words
    dictionary = dict()
    for y in list1:
        if a==len(y) :
            if y not in list3:
               list3.append(y)
    for m in list3:
        frequency=list1.count(m)/number_of_words(inp) #frequency calculation
        list4.append(frequency)
        dictionary[m] = frequency # Updates existing key
   #sorting dictionary by its values in decreasing way
    sorted_items = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_items

def longest_word(inp):
    t = inp.lower()
    list1 = t.split()
    punctuations = "!""#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    list2 = []
    for w in list1:
        x = w.strip(punctuations)
        if x[-1] == "'":
            x=x[:-1]

        list2.append(len(x))
    list2.sort()
    b = list2[-1]
    list5 = []  # all longest word
    list6 = []  # frequency of longest words
    dictionary = dict()
    for z in list1:
        if b == len(z):
            if z not in list5:
                list5.append(z)
    for n in list5:
        frequency = list1.count(n) / number_of_words(inp)
        list6.append(frequency)
        dictionary[n] = frequency #updates existing key
        #sorting dictionary by its values in decreasing way
    sorted_items = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    return sorted_items


def frequencies_of_words(inp):
    punctuations ="!""()#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    p=inp.lower()
    d=p.split()
    list1=[]

    for w in d:
        x=w.strip(punctuations)
        list1.append(x)

    list2=list(set(list1))
    list3=[]
    for x in list2 :
        y=list1.count(x)
        list3.append((x,y))
    frequency=[(x,y/number_of_words(inp))for x,y in list3] #making a list with words and their frequencys
    #sorting words frequency by their values in decreasing way
    list4=sorted(frequency, key=lambda x:(-x[1],x[0]))
    return list4

def main():
    with open(argv[1],"r") as f_in:
        f_str=f_in.read()
    with open(argv[2],"w") as f_out:
        f_out.write(f"Statistics about {os.path.basename(argv[1]):<7}:\n")
        f_out.write(f"{'#Words':<24}: {number_of_words(f_str)}\n")
        f_out.write(f"{'#Sentences':<24}: {number_of_sentences(f_str)}\n")
        f_out.write(f"{'#Words/#Sentences':<24}: {average_number_of_words_per_sentence(f_str):.2f}\n")
        f_out.write(f"{'#Characters':<24}: {number_of_characters(f_str)}\n")
        f_out.write(f"{'#Characters (Just Words)':<24}: {number_of_characters_word(f_str)}\n")
        if len(shortest_word(f_str).keys()) > 1:
            f_out.write(f"{'The Shortest Words':<24}:\n")
            for x in shortest_word(f_str).keys():
                f_out.write(f"{x:<25}({shortest_word(f_str)[x]:.4f})\n")
        else:
            f_out.write(f"{'The Shortest Word':<24}: {list(shortest_word(f_str).keys())[0]:<24} "
                        f"({list(shortest_word(f_str).values())[0]:.4f})\n")
        if len(longest_word(f_str).keys()) > 1:
            f_out.write(f"{'The Longest Words':<24}:\n")
            for x in longest_word(f_str).keys():
                f_out.write(f"{x:<25}({longest_word(f_str)[x]:.4f})\n")
        else:
            f_out.write(f"{'The Longest Word':<24}: {list(longest_word(f_str).keys())[0]:<24} "
                        f"({list(longest_word(f_str).values())[0]:.4f})\n")
        f_out.write(f"{'Words and Frequencies':<24}:")
        for (x, y) in frequencies_of_words(f_str):
            f_out.write(f"\n{x:<24}: {y:.4f}")

if __name__ == "__main__":
    main()
