#This is a typing test game which calcuates the speed , accuracy of  your typing
#Gives a text to print and then you have to print the text
def takeInput():
    global inputStr
    inputStr=raw_input()
   
    
    
def start(f):
    output = f.read()
    timeTaken = 0 #to be implemented time takeInput()
    print output
    global inputStr
    takeInput()
    
    correct = 0
    error = {}
    for i in range(0,len(output)):
        if len(inputStr) == 0:
            break;
        if inputStr[i]==output[i]:
            correct+=1
        else:
            error[ouput[i]]=inputStr[i]
        if i+1 == len(inputStr):
            break;
    print "You have entered %d of %d characters correctly in %f time.\nAccuracy percent - %.2f " % (correct,len(output),timeTaken,correct*100/len(output))
    if error != {}:
        print "Error occurred : "
        for key in error:
            print '%s ---> %s' % (key,error[key])
          

print "Welcome to the game : Enter your favourable story .\n 1. Friend and Enemy"
ch = str(input())
f = open('data/'+ch+'.txt')
inputStr=''
start(f)
