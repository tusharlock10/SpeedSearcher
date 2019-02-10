import os,Index,sys


if len(sys.argv)!=1:
    sArg=sys.argv[1].upper()
    if sArg in ["-I", "-INDEX", "--INDEX", "--I", "#I", "#INDEX", "@INDEX", "@I", "-U", "-O"]:IndexArg, word_list, DocArg= "-i", None, None
    elif sArg in ["-D", "-DOC", "--DOC", "--D", "#D", "#DOC", "-DOCUMENTATION",
                  "--DOCUMENTATION", "-DOCS", "--DOCS", "--DOG", "-DOG"]:IndexArg, word_list, DocArg= None, None, "-d"
    elif sArg in ["@STARTUPINDEX!", "@SI!"]:IndexArg, word_list, DocArg= "-si", None, None
    else:
        word_list=sys.argv[1:]
        IndexArg, DocArg= None, None

else:
    IndexArg, word_list, DocArg= None, None, None
    

def copy2clip(string):
    cmd='echo '+string+'|clip'
    os.system(cmd)
    

doc=f"""
Welcome to 
    SPEED SERCHER
        -By TJ Productions 2018
        (Tushar Jain Software Solutions)
                
1) Indexing- This means storing the name and location of your files present on your system in a file.
             Choosing this option will create/update your file Index, which then will be used to give
             you instant and up-to-date search results. To get upto date results, do indexing manually
             every alternate day, or let this app start at system startup. Press 4 in the Menu to add this
             app in startup.
             

2) Searching- A powerful and fast tool to search files in your system. It has a smart searching algorithm.
              Not only it displays results instaltly, but smartly also.
              Lets say you want to search a file, and its name big (eg. Common Dance Results India.txt), say
              you want to search this file, but you don't know its whole name, so you can just type
              'dance results common .txt' and it will show you your file. How cool!

3) Adding at startup- Tired of doing Indexing yourself again and again? Well then make it automatic. All this
                      app needs is your consent to run in the startup. So whenever the system will start, this
                      app will automatically index.

** You can also Open Files/Folders or Copy the path of Files/Folders directly after a search or even Delete them,
which takes away the pain to go to the file/folder and take that action.

You can also run SPEED SEARCHER from Command Line or CMD, which is the fast and the best way to run SS.
Open CMD by either typing CMD in windows search, or Opening Run box using (Windows Key+R) and then typing
CMD in it. You can also place CMD on your Taskbar for easy access. You can also place SPEED SEARCH on your
Taskbar.



After opening CMD, type ss in it and hit enter. You will see that you can run SPEED SEARCHER from anywhere,
anytime, just by opening CMD and typing ss in it.

*IF TYPING 'ss' IN CMD GIVES YOU ERROR LIKE 'ss is not recognized as an internal or external command', THEN
ALL YOU NEED T DO IS THAT COPY SPEEDSEARCHER PROGRAM AND PASTE IT IN C:\Windows Folder.

You can also do specific tasks in SPEED SEARCHER, for even faster experience.
Type-
1) ss -i or ss -index or ss #i to run Indexing instantly. This will skip going to main menu, and just do
        the indexing and stop the program.
2) ss <type your search here> to instantly search. This will skip going on the main menu, and directly
        do the searching of the things your told.
        eg. ss Hello.txt
        eg. ss Office Document.doc
3) ss -d or ss -doc or ss -documentation. This will instatly show you this the documentation from anywhere.
        If you forgot some feature (which is really hard as all these features are very intuitive), you can
        always refer to this documentation.
        
        
BUT THE QUESTION ARISES, WHY USE SPEED SPEARCHER IN THE FIRST PLACE?

You see, Windows search feature is very slow. You might have seen that even doing a simple file
search in Windows search or the search feature in File Explorer, takes too much time. SPEED SEARCHER
cuts down this time, to almost doing it instaltly. You can search for a file/folder, and you will get
the results instatly. This is because SPEED SEARCHER does the hard job of finding files beforehand,
all thanks to the indexing feature, which is why you will see instant results.

Also you can run SPEED SEARCHER from anywhere, at anytime, using CMD. Type ss -i or ss <files to search>
in CMD and you will see the result there and then. Also you can open the file/folder in the results just
by typing its S No. in the result. The interface is very easy to use and you will get the hang of it in
no time. If you will use SPEED SEARCHER regularly, you will save much more time.
"""



if IndexArg=="-i":
    print(r"""
+----------------------------------------+
|                                        |
|   Welcome to :                         |
|                                        |
   _____ ____  ________________     _____ _________    ____  ________  ____________ 
  / ___// __ \/ ____/ ____/ __ \   / ___// ____/   |  / __ \/ ____/ / / / ____/ __ \
  \__ \/ /_/ / __/ / __/ / / / /   \__ \/ __/ / /| | / /_/ / /   / /_/ / __/ / /_/ /
 ___/ / ____/ /___/ /___/ /_/ /   ___/ / /___/ ___ |/ _, _/ /___/ __  / /___/ _, _/ 
/____/_/   /_____/_____/_____/   /____/_____/_/  |_/_/ |_|\____/_/ /_/_____/_/ |_|
|                                        |
|           -By TJ Production (c) 2018   |
+----------------------------------------+

INDEXING
Please wait, this might take some time...

This window will close automatically after a successfull Indexing process, please
do not close this window.""")
    Index.Index()
    sys.exit()


if IndexArg=="-si":
    print(r"""
+----------------------------------------+
|                                        |
|   Welcome to :                         |
|                                        |
   _____ ____  ________________     _____ _________    ____  ________  ____________ 
  / ___// __ \/ ____/ ____/ __ \   / ___// ____/   |  / __ \/ ____/ / / / ____/ __ \
  \__ \/ /_/ / __/ / __/ / / / /   \__ \/ __/ / /| | / /_/ / /   / /_/ / __/ / /_/ /
 ___/ / ____/ /___/ /___/ /_/ /   ___/ / /___/ ___ |/ _, _/ /___/ __  / /___/ _, _/ 
/____/_/   /_____/_____/_____/   /____/_____/_/  |_/_/ |_|\____/_/ /_/_____/_/ |_|
|                                        |
|           -By TJ Production (c) 2018   |
+----------------------------------------+

INDEXING in StartupMode
Please wait, this might take some time...

*PLEASE DO NOT CLOSE THIS WINDOW

This automatically updates your SpeedSearcher Index after every computer restart.
This StartupMode is a special type of index, which will not affect the performance of
your Laptop/PC, so you can go on with your work, this window will close automatically.""")
    Index.Index(startupMode=True)
    sys.exit()
    

if word_list!=None:
    words=" ".join(word_list)
    print(fr"""
+----------------------------------------+
|                                        |
|   Welcome to :                         |
|                                        |
   _____ ____  ________________     _____ _________    ____  ________  ____________ 
  / ___// __ \/ ____/ ____/ __ \   / ___// ____/   |  / __ \/ ____/ / / / ____/ __ \  
  \__ \/ /_/ / __/ / __/ / / / /   \__ \/ __/ / /| | / /_/ / /   / /_/ / __/ / /_/ /
 ___/ / ____/ /___/ /___/ /_/ /   ___/ / /___/ ___ |/ _, _/ /___/ __  / /___/ _, _/ 
/____/_/   /_____/_____/_____/   /____/_____/_/  |_/_/ |_|\____/_/ /_/_____/_/ |_|
|                                        |
|           -By TJ Production (c) 2018   |
+----------------------------------------+

SEARCHING...  for -> "{words}"


""")
    Index.Search(word_list)
    sys.exit()


if DocArg=="-d":
    print(doc)
    sys.exit()



msg=r"""

+----------------------------------------+
|                                        |
|   Welcome to :                         |
|                                        |
   _____ ____  ________________     _____ _________    ____  ________  ____________ 
  / ___// __ \/ ____/ ____/ __ \   / ___// ____/   |  / __ \/ ____/ / / / ____/ __ \
  \__ \/ /_/ / __/ / __/ / / / /   \__ \/ __/ / /| | / /_/ / /   / /_/ / __/ / /_/ /
 ___/ / ____/ /___/ /___/ /_/ /   ___/ / /___/ ___ |/ _, _/ /___/ __  / /___/ _, _/ 
/____/_/   /_____/_____/_____/   /____/_____/_/  |_/_/ |_|\____/_/ /_/_____/_/ |_|  
|                                        |
|           -By TJ Production (c) 2018   |
+----------------------------------------+    

Options-

1) Indexing
          
2) Search

3) Open Help Documentation

4) Add to startup

5) Exit


"""

run=True
while run:
    os.system("cls")
    print (msg)
    err_str="Enter the option number"
    run2=True
    while run2:
        try:
            opt=input(err_str+" from 1, 2, 3, 4 or 5: ")
            opt=int(opt)
            run2=False
        except:
            os.system("cls")
            print (msg)
            err_str="Please enter option only"

    if opt==5:
        run=False

    if opt==1:
        os.system("cls")
        print("\n\nINDEXING\n\nPlease wait this might take some time...")
        Index.Index()
        print ("\n\nPlease do this process of Indexing every alternate days\nor, as a consequence of which, you will get outdated search results")
        input("\n\nEnter to continue...")
        continue

    if opt==2:
        os.system("cls")
        print("\nSTARTING SEARCH ENGINE...\n\n")
        word_list=Index.get_word_list()
        Index.Search(word_list)
        """
        while True:
            a=input("\n\nEnter 1 to continue...")
            if a=="1":
                break
            else:continue"""

    if opt==3:
        print(doc)
        input("\n\nEnter to continue...")

    if opt==4:
        print ("Adding to startup...")
        loc=__file__+" -i"
        Index.addStartup()
        input("\nDone\n\nEnter to continue...")
            
            
            
            
            
