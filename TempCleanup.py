import os

userinput = int(input("1 for local temps, 2 for windows temps, 3 for both"))


def deletetemps():
    
    tempfolder = r'C:\Windows\Temp'
    
    for FileName in os.listdir(tempfolder):
        FilePath = os.path.join(tempfolder, FileName)
      
        try:
            # Check if the path is a file and delete it
            if os.path.isfile(FilePath) or os.path.islink(FilePath):
                os.remove(FilePath)
                print(f'Deleted file: {FilePath}')
        except Exception as e:
            print(f'Error deleting {FilePath}: {e}')
    

def deleteTemps():
    tempfolder = r"C:\Users\panct\AppData\Local\Temp"
    
    for FileName in os.listdir(tempfolder):
        FilePath = os.path.join(tempfolder, FileName)
      
        try:
            
            if os.path.isfile(FilePath) or os.path.islink(FilePath):
                os.remove(FilePath)
                print(f'Deleted file: {FilePath}')
        except Exception as e:
            print(f'Error deleting {FilePath}: {e}')


if userinput == 1:
    deleteTemps()
elif userinput == 2:
    deletetemps()
else:
    deletetemps()
    deleteTemps()