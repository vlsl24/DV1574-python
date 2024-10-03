from collections import Counter

file=open("FileManager/sonnets.txt","r")
text=str(file.read())
text=text.lower()

def letterCount(string):
    letter_dict={}
    for letter in string:
        if letter not in letter_dict:
            letter_dict[letter]=1
        else:
            letter_dict[letter]+=1
    
    return letter_dict            

def wordCount(string):
    word_dict={}
    for i in range(0,len(string)):
        if i not in word_dict:
            word_dict[i]=1
        
        else:
            word_dict[i]+=1    



for i in range(0,len(text)):
  text=text.replace(",","")
  text=text.replace(".","")
  text=text.replace("!","")
  text=text.replace("?","")
  text=text.replace(":","")
  text=text.replace("'","")
  

listified=text.split()

print(wordCount(text))
wordCount =Counter(listified)  




