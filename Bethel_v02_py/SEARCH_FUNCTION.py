#HTTP REQUEST LIBRARY
import requests as req

#IMPORTS REGEX RECOGNITION
import re as regex

#IMPORTS XML PARSER
import xml.etree.ElementTree as ET

#IMPORT SPEECH MODULE
import SPEECH as sp

#API KEY FOR WOLFRAM ALPHA SEARCH
API_key = "JK3YYP-LPYQXL27Q6"
#URL FOR WOLFRAM ALPHA SEARCH 
URL_WA = "http://api.wolframalpha.com/v1/result?appid=" + API_key + "&i="

suggest_google_api = "http://suggestqueries.google.com/complete/search?output=toolbar&hl=en&q="
wikiString = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles="


def suggest(ambiguous_noun):
        
    # THIS FUNCTION TAKES THE NOUN TO BE SEARCHED AND RETURNS THE WIKIPEDIA RESULTS
    search_string = suggest_google_api + ambiguous_noun

    # SENDS A GET REQUEST USING THE GOOGLE SUGGEST API
    google_suggest_get = req.get(search_string).text

    # WIKIPEDIA RETURNS NULL WHEN THE SEARCHED NOUN IS NOT PROMENIENT OR VAUGE, THEREFORE A SUGGEST API
    # THAT PROVIDES CERTAIN CONTEXTUAL SIGNIFICANCE TO THE SEARCH WILL HELP IN RETURNING A USEFUL SEARCH RESULT
    suggestions = regex.search('<suggestion data="(.*?)"/>', google_suggest_get)
    
    return_suggest = str(suggestions.group(1))

    return return_suggest
def search_suggestions(ambiguous_noun):
    suggestions = suggest(ambiguous_noun)
    
    return_extract = ""
    return_title = ""

    # IF THERE IS ENOUGH SIGNIFICANCE TO WHAT IS BEING SEARCHED A WIKI SEARCH WILL THEN BE CONDUCTED
    if suggestions:
        
        return_string = str(suggestions.group(1))
        
        print("alternative: " + return_string)

        splitNoun = return_string.split(' ')
        
        capitalised = []

        for currWord in splitNoun:
            capitalised.append(currWord.capitalize())
        
        curated_noun = '%20'.join(capitalised)

        response_get = req.get(wikiString + curated_noun).text

        extract = regex.search('"extract":"(.*)"', response_get)
        title = regex.search('"title":"(.*)"', response_get)
        
        try:

            found_extract = extract.group(1)
            return_extract = found_extract.strip()
            #print(return_extract)
            found_title = title.group(1)
            return_title = found_title.strip()


        except AttributeError:
            print("there's nothing here!")
    else:
        print("there's nothing here!")
    
    return return_extract, return_title


def basic_Wikipedia_search(inputString,nounToBeSearched):
    print("searching")
    
    
    capitalised = []

    for currWord in nounToBeSearched:
        capitalised.append(currWord.capitalize())

    curated_noun = '%20'.join(capitalised)
    #print(curated_noun)
    return_extract = ""
    return_title = ""

    wikiGet = req.get(wikiString + curated_noun).text
    
    extract = regex.search('"extract":"(.*)"', wikiGet)
    title = regex.search('"title":"(.*)"', wikiGet)
    
    false_positive_str = '{} may refer to:"'.format(' '.join(nounToBeSearched))
    false_positive_boolean = regex.search(false_positive_str, wikiGet)

    
    try:
        if false_positive_boolean == False:
            try:
                
                found_extract = extract.group(1)
                return_extract = found_extract.strip()
                #print(return_extract)
                found_title = title.group(1)
                return_title = found_title.strip()
                
                
            except AttributeError: 
                print("trying an alternative")
                return_extract, return_title = search_suggestions(' '.join(nounToBeSearched))
                #print(google_suggested)
        else:
            try:
                
                return_extract = wolfram_alpha_search(inputString)
                return_title = suggest(' '.join(nounToBeSearched))
                
            except RuntimeError:
                print("nothing on this topic")
            


    except RuntimeError:
        print("is the internet down?")
    
    return return_extract, return_title

def wolfram_alpha_search(entity_to_search):
    spaced = str(entity_to_search).split(' ')

    capitalised = []

    for currWord in spaced:
        capitalised.append(currWord.capitalize())

    print(spaced)
    searched_text = '+'.join(capitalised)
    print(searched_text)
    return_text = req.get(URL_WA + str(searched_text)).text
    return return_text












