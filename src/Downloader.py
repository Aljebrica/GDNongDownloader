import subprocess
import os
import os.path

clear = lambda: os.system("cls")

def SetUp():
    #opens/creates the file and then checks if appdata/local/geometrydash is a directory
    with open('bin\\settings.cfg','a') as SetConfigs:
        appdata=os.path.join(os.environ['LOCALAPPDATA']) + '\\GeometryDash'
        Path=appdata if os.path.exists(appdata) else input('GD songs folder not found. Enter your GD songs folder with double \\ \n- ')
        SetConfigs.write(Path)

try: Settings=open('bin\\settings.cfg','r'); SongsPath=Settings.readlines()
except: SetUp();


#Functions
def Download():#1
    try:
        clear()
        #User inputs the song
        URL=input("Enter the YouTube URL of the NONG\n- ");
        ID=int(input("Enter the NONG ID\n- "))
        #Realizes the download of the NONG
        os.chdir('bin')
        subprocess.run(f'yt-dlp.exe --no-restrict-filenames -o {ID} {URL} -x --audio-format mp3 --paths {SongsPath[0]}')
        os.chdir('..')
        print("Done!")
    #Stops the process if the ID has invalid characters
    except ValueError:
        print('Insert a valid ID.')


def Switch():#2
    #User inputs the IDs
    try:
        clear()
        ID1=int(input('Enter the ID of the song to be switched\n- '))
        ID2=int(input('Enter the ID of the song to switch\n- '))
        #Renames the files
        os.chdir(SongsPath[0])
        os.rename(f'{ID1}.mp3','6f 77 6f 0d 0a.mp3')
        os.rename(f'{ID2}.mp3',f'{ID1}.mp3')
        os.rename('6f 77 6f 0d 0a.mp3',f'{ID2}.mp3')
        print("Done!")
    #Stops the process if the ID has invalid characters
    except ValueError:
        print('Insert a valid ID.')
    

#Runs all the code
while True:
    print('\t\t[1] Download NONGs \t\t [2] Switch songs')
    ChooseOption=int(input('- '))
    if ChooseOption == 1: Download()
    elif ChooseOption == 2: Switch()
    else: print('Invalid Option.')
