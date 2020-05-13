import os
import sys
import time
import json
import pyttsx3
import datetime
from playsound import playsound
from os import system, name


#> str(sys.argv)
#>>> from playsound import playsound
#>>> playsound('/path/to/a/sound/file/you/want/to/play.mp3')
#> https://www.urbandictionary.com/define.php?term=Swag

#vscode://file/{full path to project}/
#cmd = "start vscode://file/" + pdir #+ "/"


with open('D:\\auto\\settings.json', 'r') as f:
    st = json.load(f)

with open('D:\\auto\\natural_language.json', 'r') as f:
    nl = json.load(f)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
call_time = datetime.datetime.now()
args = sys.argv

#load

pdir = st["default directory"]
ldir = st["log directory"]
if name == 'nt':
    ddir = str(os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop'))
else:
    ddir = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
curd = "Current dir error"


def log():
    log = '\n' + str(call_time) + '\t' + str(args[1:])
    #sfn = ddir[:21] + "\\log.txt"
    #print(sfn,log)
    #"C:\\Users\\Alan K John\\logauto\\log.txt"
    #with open(sfn, 'a') as logfile:
    #    logfile.write(log)
    if '--log' in args:
        pass
    else:
        with open(ldir, 'a') as logfile:
            logfile.write(log)


def speak(audio):
    if st["toggle_audio"]:
        if '-a' in args:
            pass
        else:
            engine.say(audio)
            engine.runAndWait()



print('auto!')


if __name__ == "__main__":
    log()
    jobs = len(args) - 1
    curd = os.getcwd()      #> current directory
    print(args,jobs)
    print('hewego')


    for arg in args:
        #print(arg)

        if arg == 'sp':
            projname = str(args[2])

            if '--here' in args:
                os.makedirs(curd + '\\' + projname)
                os.chdir(curd + '\\' + projname)
                system("code .")
                speak("Project sequence initiated in the current directory!")


            
            elif '--desk' in args:
                os.makedirs(ddir + '\\' + projname)
                os.chdir(ddir + '\\' + projname)
                system("code .")
                speak("Project sequence initiated in the home directory!")



            else:
                os.makedirs(pdir + '\\' + projname)
                os.chdir(pdir + '\\' + projname)
                system("code .")
                speak("Project sequence initiated in the default directory!")
        
        elif arg == 'toggle_audio':
            if jobs == 1 :
                if st["toggle_audio"]:
                    st["toggle_audio"] = False
                else:
                    st["toggle_audio"] = True
                    speak("Toggle audio: On")
                
                with open('D:\\auto\\settings.json', 'w') as f:
                        json.dump(st, f)
            
            else:
                if args[2] in nl["on"]:
                    if st["toggle_audio"]:
                        print("It was already true but ok..")

                    st["toggle_audio"] = True
                    speak("Toggle audio: On")
                    with open('D:\\auto\\settings.json', 'w') as f:
                        json.dump(st, f)
                    
                elif args[2] in nl["off"]:
                    st["toggle_audio"] = False
                    with open('D:\\auto\\settings.json', 'w') as f:
                        json.dump(st, f)



        elif arg == 'settings':
            if jobs == 1 :
                print("\nSettings")
                for k,v in st.items():
                    if len(str(k)) <= 4:
                        print(str(k)+': ' , '\t\t\t' , v)
                    
                    elif len(str(k)) >= 13:
                        print(str(k)+': ' , '\t' , v)
                    else:
                        print(str(k)+': ' , '\t\t' , v)

    
    #playsound("D:\\auto\\sounds\\windows_xp_sounds_by_joshlalonde\\Windows Pop-up Blocked.wav")
