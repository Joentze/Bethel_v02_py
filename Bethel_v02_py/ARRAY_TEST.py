import os

combiFuncFile = "combinationFunctions"
wordBanksFile = "wordBanks"

txt_combiFunc = os.listdir(combiFuncFile + "/")
"""
print(txt_combiFunc)
"""
def txtToArray(directory):
    return_array = []
    listOfFiles = os.listdir(directory)
    for currFn in listOfFiles:
        #print(currFn)
        open_linesOfTxt = open(directory + currFn, 'r')
        for currLn in open_linesOfTxt:
            return_array.append(currLn.strip())
    return return_array
    
"""
print(txtToArray(combiFuncFile + '/'))            

array = txtToArray('combinationFunctions/')
print(array)

"""
def intAssignment(directory):
    return_dict = {}
    tempArr = []
    listOfFile = os.listdir(directory)
    for nameOfDoc in listOfFile:
        tempArr = open(directory + nameOfDoc, 'r')
    for currln in tempArr:

        keyName = currln.split(':')[0]
        valStr = currln.split(':')[1]
        numVal = ''.join(valStr.split('/'))
        return_dict[keyName] = numVal.strip()
    return return_dict
dictionary = intAssignment('combinationFunctions/')
print(dictionary)
