'''
takes a folder as input, goes through every subfolder
and returns the list of files with specified extension
'''

import os

def prev(path):
    '''returns path one level higher than current'''
    #print (path)
    if len(path.split("\\")) > 1:
        List = path.split("\\")
        List=List[:-1]
        Path=""
        for folder in List[:-1]:
            Path += folder+"\\"
        Path += List[-1]
        return Path
    else:

        pass

L= []

def createList(F,ext):
    global L
    if F.split("\\")[-1]=="DSD":
        pass
    else:
        #print(F)#
        os.chdir(F)
        for G in os.listdir():
            G=F+"\\"+G
            flag=True
            for i in str(G):
                if i==".":
                    flag=False
            if flag==True:
                createList(G,ext)
            else:
                if G.endswith(ext): # to find all files with given extention
                    L+=[G]
        os.chdir(prev(F))

def main():
    Path = input("Enter path: ")
    ext = input("Enter extention: ")
    os.chdir(prev(Path))
    createList(Path,ext)
    N=[]
    for folder in L:
        folder=folder.split("\\")
        N+=[folder[-1]]
    print ("\n",len(N),ext,"files found.")
    for i in range(len(N)):
        print(str(i+1).rjust(len(str(len(N)))), N[i])
    input("")

main()
