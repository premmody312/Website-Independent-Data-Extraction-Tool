import csv
import datetime
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from collections import Counter
from nltk.corpus import stopwords

def clean_word(word):
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace(".", "")
    word = word.replace(":", "")
    word = word.replace(",", "")
    word = word.replace(";", "")
    word = word.replace(")", "")
    word = word.replace("{", "")
    word = word.replace("}", "")
    word = word.replace("[", "")
    word = word.replace("]", "")
    word = word.replace("(", "")
    word = word.replace("-", "")
    word = word.replace("--", "")
    word = word.replace('—', "")
    word = word.replace("\\n", "")
    word = word.replace("\\t", "")
    word = word.replace("\\r", "")
    word = word.replace("'", "")
    word = word.replace('"', "")
    word = word.replace("/", "")
    word = word.replace("\\","")
    word = word.replace("|", "")
    word = word.replace("&", "")
    word = word.replace("1", "")
    word = word.replace("2","")
    word = word.replace("3", "")
    word = word.replace("4", "")
    word = word.replace("5", "")
    word = word.replace("6","")
    word = word.replace("7", "")
    word = word.replace("8", "")
    word = word.replace("9", "")
    word = word.replace("0","")
    return word

def clean_up_words(words):
    new_words = []
    pkg_stop_words = stopwords.words('english')
    for word in words:
        word = word.lower()
        cleaned_word = clean_word(word)
        if cleaned_word in pkg_stop_words:
            pass
        else:
            new_words.append(cleaned_word)
    return new_words

def create_csv_path(csv_path):
    if not os.path.exists(csv_path):
        with open(csv_path, 'w') as csvfile: # open that path w = write/create
            header_columns = ['WORD', 'COUNT', 'TIMESTAMP']
            writer = csv.DictWriter(csvfile, fieldnames=header_columns)
            writer.writeheader()
    else:
        os.remove(csv_path)
            
print("-----------------------------------------------------------------------------",end="")
my_url = input("Enter the url to scrape: ") 
print("-----------------------------------------------------------------------------")

print("Grabbing The URL", my_url)
domain = urlparse(my_url).netloc # domain name
print("VIA Domain", domain)
print("-----------------------------------------------------------------------------")

response = requests.get(my_url) 
print("Status is", response.status_code)
print("-----------------------------------------------------------------------------")

exclusion_list=["","|","!" ,"?",".",":",",",";",")","(","-","--",'—',"&","=",'~',"–",':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*','|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';','?', '#', '$', ')', '/',"›","·"]
javascript_jargon=['abstract','else','instanceof','super','boolean','enum','int','switch','break','export','interfacesynchronized','httpschemaorg','byte','@twitter','extends','let','this','case','false','long','throw','catch','final','nativethrows','char','finally','new',"www",'http','"wwwcommon"',"wwwcommon",'"wwwwatch"',"wwwwatch",'transient','class','float','null','true','const','for','package','try','continue','function','@context','@type','=â','private','typeof','debugger','goto','protected','var','default','ifpublic','void','delete','implements','u','px','#fff','te','return','volatile','do','import','short','while','double','instatic','with']
numbers=list(map(str, range(101)))



if response.status_code != 200: # not equal, == equal
    print("You can't scrape this", response.status_code)
    print("-----------------------------------------------------------------------------")
else:
    print("Scraping")
    print("-----------------------------------------------------------------------------")
    # print(response.text)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    body_ = soup.find("body")
    #print(body_.text)
    words = body_.text.split() # removing stop words
    clean_words = clean_up_words(words)
    word_counts = Counter(clean_words)
    temp=word_counts.most_common(30)
    for word1,count1 in temp:
            if(word1 not in exclusion_list) and (word1 not in javascript_jargon)and (word1 not in numbers)and(len(word1)<=15) :
                temp="("+word1+","+str(count1)+")"
                print(temp)
    print("-----------------------------------------------------------------------------")
    filename = domain.replace(".", "-") + '.csv'    
    path  = 'csv/' + filename 
    timestamp = datetime.datetime.now()
    time=timestamp.strftime("%Y-%m-%d %H:%M:%S")
    create_csv_path(path)
    with open(path, 'a') as csvfile:
        header_columns = ['word', 'count', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=header_columns)
        for word, count in word_counts.most_common(30):
                if((word not in exclusion_list)and (word not in javascript_jargon)and (word not in numbers)and(len(word)<=15)):
                    word=word.encode("utf-8")
                    writer.writerow({
                            "word": word,
                            "count": count,
                            "timestamp": time})

