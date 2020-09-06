
import re as regex 
import SPEECH as sp
import webbrowser

def maps_search_directions(inputString):
    
    
    url_string = "https://www.google.com/maps/dir/?api=1&"
    

    query_string = ""
    regex_directions_01 = regex.search("from (.*) to (.*)", inputString)
    
    regex_directions_02 = regex.search("to (.*) from (.*)", inputString)
    
    if bool(regex_directions_01):
        query_string = "origin=" + regex_directions_01.group(1).replace(' ','+') + "&destination="+regex_directions_01.group(2).replace(' ','+')
        print(query_string)
    if bool(regex_directions_02):
        query_string = "destination=" + regex_directions_02.group(1).replace(' ','+') + "&origin="+regex_directions_02.group(2).replace(' ','+')
        print(query_string)

    webbrowser.open(url_string + query_string)
    

