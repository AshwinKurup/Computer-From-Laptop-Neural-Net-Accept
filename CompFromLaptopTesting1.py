# todo pull a file from github and run it here
import urllib.request

#TODO unless I make it exist already, remove that folder and then replace it with the git clone (which itself will be removed after single use) 

import send2trash
import time
from github import Github
import base64
import pygit2
import shutil
import os

# TODO shove all of this inside a while loop that has a try except thing for when the module from the laptop isn't there

is_L2C_imported = False

''' 
this is increased by 1 everytime the laptop file is cloned in. 
it will be used to add to the last number in the Counter file present in this directory
'''
counterFile = open("Counter.txt", "r+")
counter = int(counterFile.readlines()[-1]) # start from the last number in the counter file



def generateNewRepoName():
    global counter
    ''' 
    :return: returns a path string of the new repo name. also returns the path of test1.py, the neural net file from laptop
    '''
    LaptopCodeDirectory = 'C:\\Users\\Ashok\\Documents\\GitHub\\CompFromLaptop\\LAPTOPCODE' + str(counter)
    NNPyFile = LaptopCodeDirectory + '\\test1.py'
    return LaptopCodeDirectory, NNPyFile


def cloneLaptopToCompRepoAndCopyMainPyFile():
    g = Github("AshwinKurup", "1Ashwin_Kurup1")
    repo = g.get_user().get_repo("LaptopToComp")
    try:
        repoClone = pygit2.clone_repository(repo.git_url, generateNewRepoName()[0])  # this creates a repo, btw
        print(repoClone, "THis is the repoclone path")
        copyFileToMainDirectory()
    except ValueError:
        print("the previous repo has not yet been deleted")

def copyFileToMainDirectory():
    try:
        newPath = shutil.copy(generateNewRepoName()[1],
                           'C:\\Users\\Ashok\\Documents\\GitHub\\CompFromLaptop\\CompFromLaptop')
    except OSError:
        print("the file can't be copied yet cos the directory has not been cloned")
print("delete this now lol just this printline")
print("delete this now lol just this printline")
print("delete this now lol just this printline")
print("delete this now lol just this printline")
while True:
    cloneLaptopToCompRepoAndCopyMainPyFile() # after this can delete the directory already, cos all I need is the py file
    try:
        import test1 # the file containing Neural Net
    except ImportError:
        print("LaptopToComp repository has not been cloned yet")
    print(test1.booleanSwitch()) # okay then this can be used as the switch. Unless this is set to false, the prog keeps running.
    print("ONE CYCLE DONE")
    counter +=1 # this represents the number of LAPTOPCODE files that have already been cloned in
    counterFile.write(str(counter) + "\n")
    ''' this increases the number in the Counter file. 
        therefore when the program ends, and a new one starts, the last number corresponding to the last
        LAPTOPCODE file cloned in during the last the the program ran will be added to and then used to create the next
        LAPTOPCODE file. I don't want the counter to start again from zero because there'd already be a file called
        LAPTOPCODE0, therefore will have an error cloning if the file already exists
    ''' 
    counterFile.truncate() # TODO find out why need truncate















