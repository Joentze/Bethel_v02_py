#MODULE FOR WOLFRAM ALPHA SEARCH

import requests as rx

import SPEECH as sp

API_WA = "JK3YYP-LPYQXL27Q6"

Http_link_WA = "http://api.wolframalpha.com/v1/result?appid="+API_WA+"&i="

def wolfram_search(StringToBeSearched):
    
    #SEPERATION BETWEEN SPACES
    seperation = StringToBeSearched.split(' ')
    #JOIN WITH "+"
    cat_string = '+'.join(seperation)
    #RETURN FROM WOLFRAM ALPHA 
    return_text = rx.get(Http_link_WA + cat_string+"%3f").text
    
    return return_text
