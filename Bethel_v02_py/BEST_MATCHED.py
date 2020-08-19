#IMPORTS DIFFLIB
import difflib as difference_ratio

#IMPORTS SPEECH RECOGNITION
#import SPEECH_RECOGNITION as sp_rec

#IMPORTS ARRAY_TEST
import ARRAY_TEST as xr

#testCombi = "2/6/3/4/5"
#listOfCombi = {'a': 23467, 'b': 3678, 'c': 2635, 'd': 23445}


def bestMatched(inputCombi, listOfCombi):
    
    seperate_slash = inputCombi.split("/")
    print(seperate_slash)
    join_inputCombi = "".join(seperate_slash)
    #CONTAINER FOR RANKING SEQUENCE RATIOS
    ranking = []

    #CHANGES THE DICTIONARY INTO A LIST
    listedCombi = list(listOfCombi)
    #SORTS THE LIST TO MITIGATE MISORDER OF THE LIST
    sortedCombi = sorted(listedCombi)

    for combiType in sortedCombi:
        #print(combiType)
        dictVal = listOfCombi[combiType]
        #print(dictVal)
        matchRatio = difference_ratio.SequenceMatcher(None, str(join_inputCombi), str(dictVal)).ratio()
        #print(matchRatio)
        ranking.append(matchRatio)

    highestFloat = max(ranking)
    indexNum = ranking.index(highestFloat)
    return_best_match = sortedCombi[indexNum]

    return return_best_match

#bestMatched_return = bestMatched("2/6/3/4/7", listOfCombi)
#rint(bestMatched_return)

