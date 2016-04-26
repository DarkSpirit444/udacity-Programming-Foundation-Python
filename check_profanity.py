import urllib
import json

def read_text():
    quotes = open("movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    #connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    data = json.loads(output)
    #if "true" in output:
    if data['response'].lower() == "true":
        print("Profanity Alert!!")
    #elif "false" in output:
    else:
        print("This document has no curse words!")

read_text()
