#IMPORTS WEBBROWSER MODULE
import webbrowser as wb

#IMPORTS ARRAY_TEST
import ARRAY_TEST as xr

#IMPORTS SEARCH_FUNCTION
import SEARCH_FUNCTION as SF

#IMPORTS WA_SEARCH
import WA_SEARCH as WA

#IMPORTS SPEECH MODULE 
import SPEECH as sp

#IMPORTS GMAPS MODULE
import MAPS as maps

#IMPORTS BEST_MATCHED 
#import BEST_MATCHED as BM_mod

nameFile = "combinationFunctions"
txtsInFile = xr.txt_combiFunc

def dictFunc(directory, txtsInFile):
    
    return_dict = {}
    list_of_functions = []

 
    #READS THE DIRECTORY OF THE COMBINATION FILE
    for currTxt in txtsInFile:
        iterateLines = xr.txtToArray(directory + '/' + currTxt )        
        #FOR EVERY LINE THERE IS A NEW COMBINATION, THE FOR LOOP ITERATES THROUGH THEM TO RETURN THE COMBI NUMBER AND THE NAME
        for currLn in iterateLines:
            currLineName = currLn.split(':')
            keyName = currLineName[0]
            
            nameOfFunc = keyName.split('_')
            valName = nameOfFunc[1]

            if valName not in list_of_functions:
                list_of_functions.append(valName)
            
            return_dict[keyName] = valName
        
        return return_dict, list_of_functions
        
dict_num, list_func = dictFunc(nameFile, txtsInFile)
print(list_func)





def execute(bestMatched, functionsList, nounToSearch, inputString):
    #EXECUTES THE BEST MATCHED FUNCTION W/REF TO THE FUNCTION LIST
    
    def RequestQuery():
        print('RQ')

    def Search():
        
        print('search')
        print_extract, print_title =  SF.basic_Wikipedia_search(inputString,nounToSearch)
        print(print_extract)
        sp.say(print_extract)
        
    def WASearch():

        print('WASearch')
        return_WA = WA.wolfram_search(inputString)
        print(return_WA)
        sp.say(return_WA)
        
    
    def News():
        print('news')
    
    def MapsDR():
        maps.maps_search_directions(inputString)
        

    
    locals()[functionsList[functionsList.index(bestMatched)]]()


def Generate_overall_func(bestMatched_return):
    return_func = bestMatched_return.split('_')[1]
    return return_func

#FINAL EXECUTION PATH
#execute(Generate_overall_func("01_Search"), list_func, "covid-19")



