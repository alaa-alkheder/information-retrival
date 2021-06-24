# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import nltk
import json
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from textblob import TextBlob, Word
# import datefinder

from num2words import num2words

# print(stopwords.words('english'))

def correct_word(word):
    return str( TextBlob(word).correct())

def get_stop_word():
    str = open('C://Users//Eng Alaa Alkheder//Desktop//Lab4//stop words.txt', 'r').read()
    str=str.replace('\n\n','\n')
    str=str.split('\n')
    return str

# this function returns a list of tokenized and stemmed words of any text
def get_tokenized_list(doc_text):
    tokens = nltk.word_tokenize(doc_text)
    return tokens

# This function will performing stemming on tokenized words
def word_stemmer(token_list):
  ps = nltk.stem.PorterStemmer()
  stemmed = []
  for words in token_list:
    stemmed.append(ps.stem(words))
  return stemmed

# Function to remove stopwords from tokenized word list
def remove_stopwords(doc_text):
  cleaned_text = []
  for words in doc_text:
    if words.upper() not in stop_words:
      cleaned_text.append(words)
  return cleaned_text

# Define function to lemmatize each word with its POS tag
def lemmatize_with_postag(sentence):
    sent = TextBlob(' '.join(sentence))
    tag_dict = {"J": 'a',
                "N": 'n',
                "V": 'v',
                "R": 'r'}
    words_and_tags = [(w, tag_dict.get(pos[0], 'n')) for w, pos in sent.tags]
    lemmatized_list = [wd.lemmatize(tag) for wd, tag in words_and_tags]
    return (lemmatized_list)

def convert_num_to_word(array):
    temp=[]
    for x in array:
        if x.isnumeric():
            x=num2words(int(x))
        temp.append(x)
    return temp;


def read_from_file(fileName):
    str = open(f'{fileName}.txt', 'r').read()
    return str

def all_opreations(temp):
    # TODO convert number to word
    temp = get_tokenized_list(temp)
    temp = remove_stopwords(temp)
    temp = lemmatize_with_postag(temp)
    temp = remove_stopwords(temp)
    temp = word_stemmer(temp)
    temp = remove_stopwords(temp)
    return temp;

def get_frecuency(array):
        temp = dict();
        count = 0;
        for x in array:
            count = 0
            for y in array:
                # print('x:',x)
                if (x == y):
                    # print(y)
                    count = count + 1
                    # array.remove(y)

            s = {'key': x, 'value': count}
            temp[s['key']] = s
        # ss=map(lambda b: temp[b],temp)
        # print(list(ss))
        return list(map(lambda b: temp[b], temp))


def build_dictionary():
    dictionary=dict()
    for i in range(1,424):
        temp=read_from_file("C://Users//Eng Alaa Alkheder//Desktop//Lab4//corpus//"+i.__str__())
        temp=get_frecuency(all_opreations(temp))
        print("C://Users//Eng Alaa Alkheder//Desktop//Lab4//corpus//"+i.__str__())
        for x in temp:
            # print(x)
            if dictionary.get(x.get('key')):
               dictionary.get(x.get('key')).get('files').append({'file':i,'repetition':x.get('value')})
               dictionary[x.get('key')].update(
                   {
                       'value':dictionary.get(x.get('key')).get('value') + x.get('value'),
                        'files':dictionary.get(x.get('key')).get('files')
                    }
               )
            else:
                obj={'value':x.get('value'),'files':[{'file':i,'repetition':x.get('value')}]}
                dictionary[x.get('key')]=obj
    print(dictionary)
    print(len(dictionary))
    js = json.dumps(dictionary)
    f = open("dict.json", "w")
    f.write(js)
    f.close()




stop_words = get_stop_word()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()
    build_dictionary()
    # Check for single document
    # tokens = get_tokenized_list("better worse THE ALLIES AFTER NASSAU IN DECEMBER 1960, THE U.S . FIRST  PROPOSED TO HELP NATO DEVELOP ITS OWN NUCLEAR STRIKE FORCE . BUT EUROPE  MADE NO ATTEMPT TO DEVISE A PLAN . LAST WEEK, AS THEY STUDIED THE  NASSAU ACCORD BETWEEN PRESIDENT KENNEDY AND PRIME MINISTER MACMILLAN,  EUROPEANS SAW EMERGING THE FIRST OUTLINES OF THE NUCLEAR NATO THAT THE  U.S . WANTS AND WILL SUPPORT . IT ALL SPRANG FROM THE ANGLO-U.S .  CRISIS OVER CANCELLATION OF THE BUG-RIDDEN SKYBOLT MISSILE, AND THE  U.S . OFFER TO SUPPLY BRITAIN AND FRANCE WITH THE PROVED POLARIS (TIME,  DEC . 28) . THE ONE ALLIED LEADER WHO UNRESERVEDLY WELCOMED THE POLARIS  OFFER WAS HAROLD MACMILLAN, WHO BY THUS KEEPING A SEPARATE NUCLEAR  DETERRENT FOR BRITAIN HAD SAVED HIS OWN NECK . BACK FROM NASSAU, THE  PRIME MINISTER BEAMED THAT BRITAIN NOW HAD A WEAPON THAT \" WILL LAST A  GENERATION . THE TERMS ARE VERY GOOD . \" MANY OTHER BRITONS WERE NOT SO  SURE . THOUGH THE GOVERNMENT WILL SHOULDER NONE OF THE $800 MILLION  DEVELOPMENT COST OF POLARIS, IT HAS ALREADY POURED $28 MILLION INTO  SKYBOLT AND WILL HAVE TO SPEND PERHAPS $1 BILLION MORE FOR A FLEET OF  MISSILE-PACKING SUBMARINES . AT BEST, THE BRITISH WILL NOT BE ABLE TO  DESIGN, BUILD AND PROVE ITS NUCLEAR FLEET BEFORE 1970, THREE YEARS  AFTER BRITAIN'S BOMBER FORCE HAS PRESUMABLY BECOME OBSOLETE . THEN WHAT  ? TORY BACKBENCHERS ARE LOUDLY SKEPTICAL OF WHAT THEY CALL \" THE  SMALL TYPE \" IN THE NASSAU PACT, WHICH STIPULATES THAT BRITAIN'S  POLARIS SUBMARINE FLEET, EXCEPT WHEN \" SUPREME NATIONAL INTERESTS \"  INTERVENE, MUST BE COMMITTED TO A TRULY MULTILATERAL NATO FORCE . DOES  THAT MEAN THAT BRITAIN WILL EVENTUALLY HAVE NO STRIKE FORCE OF ITS OWN  ? WHO WILL DECIDE WHEN OR WHETHER NATIONAL INTERESTS JUSTIFY  WITHDRAWAL OF SUBMARINES FROM NATO, PARTICULARLY IF THOSE NATIONAL  INTERESTS CONFLICT WITH U.S . POLICY ? THE BIGGEST QUESTION OF ALL IS  WHETHER FRANCE'S INCLUSION IN THE OFFER WAS A DELIBERATE PLOY BY JACK  KENNEDY TO END OR AT LEAST DOWNGRADE BRITAIN'S PRIZED \" SPECIAL  RELATIONSHIP \" WITH THE U.S . THE CARTOONISTS WENT EVEN FARTHER . THEY  NOT ONLY SHOWED SUPERMAC JUMPING TO SUPERJACK'S COMMANDS, BUT DE GAULLE  AND ADENAUER AS WELL . AS EDITH SAID . THE FRENCH, WHO GOT NO HELP FROM  THE U.S . IN DEVELOPING THEIR FORCE DE FRAPPE, WERE QUICK TO CROW THAT  BRITAIN VAUNTED TIES WITH THE U.S . HAD BROUGHT IT NOTHING BUT  HUMILIATION . BY CONTRAST, BRAGGED FRENCH OFFICIALS, THE SKYBOLT FIASCO  ONLY VINDICATED FRANCE DECISION TO DEVELOP ITS OWN BOMBS AND DELIVERY  SYSTEMS . THUS, THOUGH CHARLES DE GAULLE PROMISED TO \" REFLECT \" ON THE  POLARIS OFFER, THERE WAS LITTLE LIKELIHOOD THAT HE WOULD ACCEPT ANY  OFFER THAT WOULD SUBJECT A FRENCH FORCE TO ALLIED CONTROL . IT IS DE  GAULLE'S UNSWERVING CONVICTION THAT IF THE RUSSIANS WERE ACTUALLY TO  INVADE WESTERN EUROPE, NO NATION THAT WAS NOT DIRECTLY ATTACKED MEANING  THE U.S . WOULD INVITE NUCLEAR DEVASTATION BY HELPING ITS ALLIES . THUS  UNLIKE BRITAIN'S BOMBER FORCE, WHICH ALL ALONG HAS BEEN PLEDGED TO \"  THE WESTERN STRATEGIC DETERRENT, \" FRANCE'S FORCE DE FRAPPE WILL BE  RESPONSIBLE ONLY FOR FRANCE'S DEFENSE . AT THE SAME TIME, DE GAULLE HAS  LONG ARGUED THAT THE ATLANTIC ALLIANCE COULD BE RUN MOST EFFICIENTLY BY  A TRIUMVIRATE THAT WOULD INCLUDE FRANCE AS AN EQUAL OF THE U.S . AND  BRITAIN . THIS IS ONE OF HIS MAJOR, IF UNSPOKEN, CONDITIONS FOR BRITISH  MEMBERSHIP IN THE COMMON MARKET ; AND DE GAULLE SUGGESTED POINTEDLY TO  MACMILLAN THAT IT WOULD HELP IF BRITAIN WERE TO SHARE ITS ADVANCED  MISSILE TECHNOLOGY WITH FRANCE . WHEN MACMILLAN REPLIED NONCOMMITTALLY  THAT HE WOULD HAVE TO DISCUSS THIS WITH KENNEDY, DE GAULLE TOLD HIS  GUEST WITH HAUTEUR THAT FRANCE IN THAT CASE COULD DO NOTHING TO EASE  BRITAIN'S ENTRY INTO EUROPE . GO-IT-ALONE GRANDEUR . KONRAD ADENAUER,  ON THE OTHER HAND, IS FEARFUL THAT DE GAULLE WILL SNAP UP THE POLARIS  OFFER AND IN THIS WAY ACHIEVE HIS GOAL OF A THREE-NATION NATO  DIRECTORATE . THOUGH HIS GOVERNMENT VOWED IN 1954 NOT TO MANUFACTURE  NUCLEAR WEAPONS, ADENAUER HAS BECOME INCREASINGLY APPREHENSIVE THAT  WITHOUT THEM, AND WITH NO SAY IN THEIR USE, WEST GERMANY WILL BE  RELEGATED TO SECOND-CLASS CITIZENSHIP IN THE ALLIANCE . LAST WEEK AN  OFFICIAL BULLETIN EVEN REVIVED THE OLD, BITTER CRY THAT U.S . PLEAS FOR  GREATER RELIANCE ON CONVENTIONAL FORCES ARE AIMED AT RAISING GERMAN \"  CANNON FODDER \" FOR U.S . \" ATOMIC KNIGHTS . \" A FROSTY LETTER FROM THE  CHANCELLOR TO PRESIDENT KENNEDY SUGGESTED THAT GERMANY, WHICH ALREADY  SUPPLIES ALMOST 50 PER CENT OF NATO GROUND STRENGTH, DOES NOT INTEND TO  RAISE ANY MORE DIVISIONS FOR CONVENTIONAL WARFARE . YET U.S . STRATEGIC  PLANNERS REASON THAT THE ONLY CREDIBLE DETERRENT TO SOVIET ATTACK IS A  STRONG ARMY ON THE GROUND, BACKED BY THE VAST U.S . NUCLEAR ARSENAL .  FACT IS, THE BRITISH AND FRENCH NUCLEAR WEAPONS COULD NEVER BE USED  INDEPENDENTLY OF THE U.S . AGAINST RUSSIA WITHOUT INVITING DEVASTATING  SOVIET RETALIATION . AFTER ALL THEIR EFFORTS, THE BRITISH AND FRENCH  WILL HAVE MANAGED TO CREATE A NUCLEAR CAPACITY THAT REPRESENTS ONLY 4  PER CENT OF U.S . NUCLEAR POWER . \" IT IS JUST A DAMNED NUISANCE, \"  SAID A STATE DEPARTMENT OFFICIAL LAST WEEK . \" IT MEANS NOTHING  MILITARILY EXCEPT THAT WE WILL BE EXPECTED TO BAIL OUT THE FIRST  COUNTRY THAT THROWS THE FIRST PEA AT THE RUSSIANS OR ANYONE ELSE . \"  CHARLES DE GAULLE COULD HARDLY BE EXPECTED TO AGREE, AT LEAST UNTIL HIS  FORCE DE FRAPPE BECOMES OBSOLETE . FOR BRITAIN AND GERMANY, THE  MULTILATERAL DETERRENT MAKES IMMEDIATE SENSE . EVENTUALLY, FRANCE, TOO,  MAY WELL FIND A NATO-CONTROLLED POLARIS FLEET, OR ITS POSSIBLE  SUCCESSOR, A EUROPEAN MINUTEMAN ARSENAL, THE ONLY ANSWER TO THE  SPIRALING COST AND DIMINISHING VALUE OF GO-IT-ALONE GRANDEUR .  ")
    # # print("WORD TOKENS:")
    # # matches = datefinder.find_dates(' '.join(tokens))
    # # for match in matches:
    # #     print(match)
    #
    #
    # doc_text= convert_num_to_word(tokens)
    # print(doc_text)
    # doc_text= remove_stopwords(doc_text)
    # print("\nAFTER PERFORMING THE WORD lemmatize::")
    # doc_text = lemmatize_with_postag(doc_text)
    # doc_text = remove_stopwords(doc_text)
    # print(doc_text)
    # print("\nAFTER PERFORMING THE WORD STEMMING::")
    # doc_text = word_stemmer(doc_text)
    # doc_text = remove_stopwords(doc_text)
    # print(doc_text)



# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
