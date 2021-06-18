# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import these modules
from Tools.scripts.combinerefs import read
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
import json
import ast
stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {chack_word("word")}')  # Press Ctrl+F8 to toggle the breakpoint.
    # print(f'Hi, {read_from_file("C://Users//Eng Alaa Alkheder//Desktop//Lab4//corpus//1")}')  # Press Ctrl+F8 to toggle the breakpoint.

# this function to get root from word
def get_stemmer(word):
    return stemmer.stem(word)
# this function to get root from word
# TODO get from alaa
def get_lemmatizer(word):
    return  lemmatizer.lemmatize(word, pos="a")

def correct_word(word):
    return str( TextBlob(word).correct())

def read_from_file(fileName):
    str = open(f'{fileName}.txt', 'r').read()
    return str

def tokenize_word(str):
    # TODO find all shorcut word and replace
    str=str.replace('U.S','UNITED State')
    str=str.replace(',','')
    str=str.replace('.','')
    str=str.replace('"','')
    str=str.replace('\n',' ')
    str=str.replace('','')
    str=str.replace('(','')
    str=str.replace(')','')
    str = str.split(' ')
    # print(str)
    return str

def get_stop_word():
    str = open('C://Users//Eng Alaa Alkheder//Desktop//Lab4//stop words.txt', 'r').read()
    str=str.replace('\n\n','\n')
    str=str.split('\n')
    return str

def chack_word(str):
    str=str.upper()
    for x in stopWord:
        if x==str:
             return 1
    return 0

def remove_stop_word_from_query(query):
    return 1

def get_token_from_corpus(corpusName):
    data= read_from_file(corpusName)
    str= tokenize_word(data)
    temp=[];
    for x in str:
        root=get_stemmer(x)
        root=get_lemmatizer(root)
        if not chack_word(root):
          temp.append(root)
    return temp

def get_frecuency(array):
    temp=dict();
    count=0;
    for x in array:
        count =0
        for y in array:
            #print('x:',x)
            if(x==y):
                #print(y)
                count=count+1
                #array.remove(y)

        s={'key':x, 'value':count}
        temp[s['key']]=s
    #ss=map(lambda b: temp[b],temp)
    #print(list(ss))
    return list(map(lambda b: temp[b],temp))

def build_dictionary():
    dictionary=dict()
    for i in range(1,424):
        temp=get_token_from_corpus("C://Users//Eng Alaa Alkheder//Desktop//Lab4//corpus//"+i.__str__())
        temp=get_frecuency(temp)
        for x in temp:
            if dictionary.get(x.get('key')):
               dictionary.get(x.get('key')).get('files').append(i)
               dictionary[x.get('key')].update(
                   {
                       'value':dictionary.get(x.get('key')).get('value') + x.get('value'),
                        'files':dictionary.get(x.get('key')).get('files')
                    }
               )
            else:
                obj={'value':x.get('value'),'files':[i]}
                dictionary[x.get('key')]=obj
    print(dictionary)
    print(len(dictionary))
    js = json.dumps(dictionary)
    f = open("dict.json", "w")
    f.write(js)
    f.close()

def load_dictioary():
    file = open("dict.json", "r")

    contents = file.read()
    dictionary = ast.literal_eval(contents)
    # print(dictionary)
    # print(len(dictionary))
    file.close()
    return dictionary;


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    stopWord=get_stop_word()
    q=get_token_from_corpus('C://Users//Eng Alaa Alkheder//Desktop//Lab4//corpus//aaa')
    dictionary= load_dictioary()
    revelance=[];
    for x in q:
        print(q)
        for files in dictionary.get(x)['files']:
            #print(x,dictionary.get(x))
            revelance.append(files)
    revelance=get_frecuency(revelance)
    revelance.sort(key=lambda b: b['value'],reverse=True)
    revelance=list(filter(lambda b:b['value'] != 1 ,revelance))
    revelance=list(filter(lambda b:b['value'] != 2 ,revelance))
    print(revelance)
    print(len(revelance))
    # build_dictionary()
    # stopWord=[];
    # x=get_token_from_corpus("C://Users//Eng Alaa Alkheder//Desktop//Lab4//corpus//aaa")
    # print(x)
    # print(correct_word("evli"))
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
