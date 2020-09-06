import os as file_dir
import time

#print(list_of_txt)

inputStr = "what is the distance between mars and earth"



def list_assign(fileName):
    letter_list = {
    'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[],
    'I':[],'J':[],'K':[],'L':[],'M':[],'N':[],'O':[],'P':[],
    'Q':[],'R':[],'S':[],'T':[],'U':[],'V':[],'W':[],'X':[],
    'Y':[],'Z':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],
    '7':[],'8':[],'9':[],'0':[]
    }
    #NAME OF FILE 
    list_of_txt = file_dir.listdir(fileName + '/')
    
    #print(list_of_txt)
    for current_txt in list_of_txt:
        if current_txt.endswith( ".txt" ):
            all_lines = open(fileName + '/' +current_txt, "r")
            for currLn in all_lines:
                
                #print(currLn)
                strip_currLn = currLn.strip()
                cap_currLn = strip_currLn.capitalize()
                startsWith = cap_currLn[0]

                letter_list.setdefault(startsWith,[]).append(strip_currLn.capitalize())
    #print(letter_list)
    return letter_list



def func_reference(fileName):
    
    list_of_txt = file_dir.listdir(fileName + '/')
    return_dict = {}
    
    for textFile in list_of_txt:
        if textFile.endswith( ".txt" ):
            
            no_index = str(textFile.split('_'))
            
            file_lines = open(fileName + "/" + textFile, "r")
            for currLn in file_lines:
                return_dict[currLn.strip()] = no_index[2]

    return return_dict

def input_tokenCombi(inputString, alpha_index, reference_no):

    splitString = inputString.split(' ')
    return_tokenIndex = []
    nounToBeSearched = []
    
    for currWd in splitString:
        startsWith = currWd[0].capitalize()
        #print(startsWith)
        word_in = alpha_index[startsWith]
        #print(word_in)
        if currWd.capitalize() in word_in:
           # print(currWd)
            return_tokenIndex.append(str(reference_no.get(currWd)))
        else:
            nounToBeSearched.append(currWd)
    joint_combi = '/'.join(return_tokenIndex)
    
    return joint_combi, nounToBeSearched

"""
alpha_index = list_assign("wordBanks")
print(alpha_index)   
reference_no = func_reference("wordBanks")
print(reference_no)

inputCombi, nounSearch = input_tokenCombi(inputStr, alpha_index, reference_no)
print(inputCombi)
print(nounSearch)
"""