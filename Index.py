import os,sys,shutil, time
try:from colorama import init, Fore, Back, Style
except:pass

try:init(convert=True, autoreset=True)
except:pass

#####################  TJ Module functions ###################
def delete(path):
    try:shutil.rmtree(path)
    except:
        try:
            os.remove(path)
        except:
            print("Could not delete "+path+" due to some error.")

def get_startup_path():
    a = "C:\\Users\\"
    b = "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    user_L = os.listdir(a)
    L = []
    for user in user_L:
        if user in ['Public', 'Default', 'All Users', 'Default User']:
            continue
        if not os.path.isdir(a + user):
            continue
        path = a + user + b
        L += [path]
    return L





def copy2clip(string):
    cmd='echo '+string+'|clip'
    os.system(cmd)
    

def print_colored_text(text, snippets):
    #text- big string of text
    #snippet- the part of text to be coloured
    string=""
    for snippet in snippets:
        
        if string=="":L=(text.lower()).split(snippet.lower())
        else:L=string.split(snippet.lower())
        i=len(L)
        string=L[0]
        
        for x in range(1,i):
            try:string+=(Fore.GREEN+snippet.upper()+Fore.WHITE+L[x])
            except:string+=(snippet.upper()+L[x])
    return string


def make_drives():
    l=[]
    for i in range(65,92):
        l+=[chr(i)]

    return l

All_Drives=make_drives()+['C:\\Users\\','C:\\Program Files\\', 'C:\\Program Files (x86)\\']

       
def Index(Drives=All_Drives, startupMode=False):
    try:
        folder="Index\\"
        os.mkdir(folder)
    except:
        folder="C:\\Users\\Public\\Documents\\Index\\"
        try:os.mkdir(folder)
        except:pass
        
    
    for Drive in Drives:
        File_Num=0
        Folder_Num=0
        tempx=0
        if os.path.isdir(Drive+":\\"):pass
        else:continue
        print("\n\n\nIndexing "+Drive+" Drive")
        f=open(folder+"Drive "+Drive+".txt","w",encoding="utf-8")
        temp=[]
        for root, dirs, files in os.walk(Drive+':\\'):
            Folder_Num+=1
            temp+=[root+"\n"]
            
            for file in files:
                tempx+=1
                if tempx>120:
                    tempx=0
                    if startupMode:time.sleep(0.05)
                    
                name= root+'\\'+file+'\n'
                File_Num+=1
                temp+=[name]
                if len(temp)>1024:
                    f.writelines(temp)
                    temp=[]
        f.writelines(temp)
        temp=[]

        pluralfile="s"
        pluralfolder="s"
        if File_Num==1:
            pluralfile=""
        if Folder_Num==1:
            pluralfolder="" 
        print (Drive+" Drive: "+str(File_Num)+" file"+pluralfile+" and "+str(Folder_Num)+" folder"+pluralfolder)
                
                

def Search(word_list, Drives=All_Drives):
    total=0
    Paths_Found=[]
    for Drive in Drives:
        if os.path.isdir(Drive+":\\"):pass
        else:continue
        try:
            try:
                folder="Index\\"
                f=open(folder+"Drive "+Drive+".txt","r",encoding="utf-8")
            except:
                folder="C:\\Users\\Public\\Documents\\Index\\"
                f=open(folder+"Drive "+Drive+".txt","r",encoding="utf-8")
        except:
            folder="Index\\"
            print("Indexed files not found! Doing Indexing and then search will resume, please wait...")
            Index()
            os.system("cls")
            try:f=open(folder+"Drive "+Drive+".txt","r",encoding="utf-8")
            except:
                folder="C:\\Users\\Public\\Documents\\Index\\"
                f=open(folder+"Drive "+Drive+".txt","r",encoding="utf-8")

        for line in f.readlines():
            LINE=line.upper()
            a=True
            for word in word_list:
                if word.upper() not in LINE:
                    a=False
                    break
                else:pass
            if a:
                if "\n" in list(line):path=line[:-1]
                else:path=line
                total+=1
                thing="Folder"
                if os.path.isfile(path):thing="File"
                if total==1:
                    print(" S No. |  Type   |  File/Folder Path")
                    print("----------+---------+--------------------------------------------------------------------------")
                path_print=print_colored_text(path, word_list)
                print("  %-5s | %-8s| %s" % (str(total),thing,path_print))
                Paths_Found+=[path]
                
    plural="s"
    if total==1:
        plural=""
    print ("\n\n",total," result"+plural+" found")
    print ("* If you think that the search result is wrong, then please do the Indexing, and then search again!")

    if total==0:
        input("Enter to continue...")
        return None
    
    print("\t\nSPEED SEARCHER will copy the file/folder path directly to your clipboard, just enter the S No. of the path\n")
    print("\t\nIf you want to open that file/folder instead of copying its path, type S No. and O with it.")
    print("\t\tEg. 5 O or 12 O or 5 OPEN or 12 OPEN etc.\n")
    print("\t\nIf you want to delete that file/folder instead, type DELETE instead of O as in the above case.\n")
    msg="Enter the S No. of the path from above or type Q to quit: "

    while True:
        openit, deleteit= False, False
        choice=input(msg).upper()
        if choice in ["Q", "E", "QUIT", "EXIT", "0"]:return None
        if ("O" in choice) or ("OPEN" in choice) or (" 0" in choice):
            temp=choice.split()
            choice=temp[0]
            openit=True

        if (" DELETE" in choice):
            temp=choice.split()
            choice=temp[0]
            deleteit=True
        
        try:choice=int(choice)
        except:
            msg="Enter only numbers of the path from above or type Q to quit: "
            continue
        if not 0<choice<=total:
            msg="Please enter the S No. of the path only from above or type Q to quit: "
            continue
        break

    path=Paths_Found[choice-1]
    thing="folder"
    if os.path.isfile(path):thing="file"
    
    if openit:
        os.startfile(path)
        print("\n\nOpened  "+thing+" "+path)
    elif deleteit:
        delete(path)
        print("\n\nDeleted "+thing+" "+path)
    else:
        copy2clip(path)
        print("\n\n"+path+"    is copied to clipboard.")
        
    return None

        
def get_word_list():
    word=input("Enter filename to search: ")
    L=word.split()
    return L


def addStartup():
    myName=sys.argv[0]
    x=f'"{myName}" @SI!'
    
    try:f=open("SSIndex.bat", "w")
    except:
        print('Could not add to startup')
        return
    f.write(x)
    f.close()

    paths=get_startup_path()
    for startup_path in paths:
        shutil.copy("SSIndex.bat", startup_path)
        os.remove("SSIndex.bat")
        
    
