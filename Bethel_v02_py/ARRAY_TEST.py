import os

wordBanksFile = "wordBanks"
combiFuncFile = "combinationFunctions"
txt_combiFunc = os.listdir(combiFuncFile)
"""
print(txt_combiFunc)
"""
def txtToArray(directory):
    return_array = []
    listOfFiles = os.listdir(directory)
    for currFn in listOfFiles:
        #print(currFn)
        with open(os.path.join(directory,currFn), 'r') as open_LinesOfTxt:
            for currLn in open_LinesOfTxt:
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
        tempArr = open(os.path.join(directory,nameOfDoc), 'r')
    for currln in tempArr:

        keyName = currln.split(':')[0]
        valStr = currln.split(':')[1]
        numVal = ''.join(valStr.split('/'))
        return_dict[keyName] = numVal.strip()
    
    return return_dict



if __name__ == "__main__":

    dictionary = intAssignment('combinationFunctions')
    print(dictionary)
