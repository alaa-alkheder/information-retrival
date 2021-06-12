# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# import these modules
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
stemmer = SnowballStemmer("english")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {chack_word("word")}')  # Press Ctrl+F8 to toggle the breakpoint.
    # print(f'Hi, {read_from_file("C://Users//Eng Alaa Alkheder//Desktop//Lab4//corpus//1")}')  # Press Ctrl+F8 to toggle the breakpoint.

# this function to get root from word
def get_root(word):
    return stemmer.stem(word)

def correct_word(word):
    return str( TextBlob(word).correct())

def read_from_file(fileName):
    str = open(f'{fileName}.txt', 'r').read()
    return str


def tokenize_word(str):
    str = str.split(' ')
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
        root=get_root(x)
        if chack_word(root):
            print()
        else: temp.append(root)
    return temp
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    lemmatizer = WordNetLemmatizer()

    # print("rocks :", lemmatizer.lemmatize("rocks"))
    print("corpora :", lemmatizer.lemmatize("evli"))

    # a denotes adjective in "pos"
    print("better :", lemmatizer.lemmatize("better", pos="a"))
    stopWord=get_stop_word()
    # x=get_token_from_corpus("C://Users//Eng Alaa Alkheder//Desktop//Lab4//corpus//1")
    print(get_root("syrian"))
    print(correct_word("pley"))
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
