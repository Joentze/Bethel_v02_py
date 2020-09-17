import os
import speech_recognition as sr
import SPEECH as sp
import BEST_MATCHED as Bm
import LIST_NESTED_DICT as dictList
import FUNCTIONS_EXEC as func_exec
import ARRAY_TEST as xr


r = sr.Recognizer()
mic =  sr.Microphone()

#list_of_words_file = os.listdir("/" + "combinationFunctions")
#print(list_of_words_file)

orglist = dictList.list_assign('wordbanks')
#print(orglist)
func_ref = dictList.func_reference('wordBanks')
#print(func_ref)
txt_combiFunc = os.listdir("combinationFunctions/")
#print(txt_combiFunc)
listOfCombiArray = xr.txtToArray("combinationFunctions/")

integerAssign = xr.intAssignment("combinationFunctions/")

def inputString():
    boolean_state = False
    while not boolean_state:
        
        with mic as source:
            print('speak anything')
            audio = r.listen(source)
            sr.Microphone.list_microphone_names()
                
        try:
            #OBTAINS THE TRANSCRIPT OF THE VOICE RECORDING 
            text = r.recognize_google(audio)
            print('transript: {}'.format(text))

            #MATCHES THE INPUT STRING TO ITS TOKEN COMBINATION AND SIPHONS OUT THE NOUN TO BE SEARCHED BY CANCELLING OUT WORDS IN THE WORD BANK
            inputCombi, nounToBeSearched = dictList.input_tokenCombi(text, orglist, func_ref)
            #print(inputCombi)
            #print(nounToBeSearched)
            
            #RETURNS LIST OF OVERALL FUNCTIONS AND DICTIONARY OF OVERALL FUNCTIONS FOR REFERENCE 
            dictNum, ListFunctions = func_exec.dictFunc('combinationFunctions', listOfCombiArray)
            #print(dictNum)
            #print(ListFunctions)   
            
            #RETURNS THE BEST MATCHED FUNCTION FOR THE INPUT COMBINATION
            bestMatchedFunction = Bm.bestMatched(inputCombi, integerAssign)
            #print(bestMatchedFunction)
            
            #FINDS AND EXECUTES THE FUNCTION OF THE INPUT COMBI
                
            #GETS THE OVERALL FUNCTION
            overall_func = func_exec.Generate_overall_func(bestMatchedFunction)
           
            
            #EXECUTES THE FINAL FUNCTION 
            func_exec.execute(overall_func, ListFunctions, nounToBeSearched, text)





        except:
            print("can't hear anything")
        
if __name__ == "__main__":
    inputString()