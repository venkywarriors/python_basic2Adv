import os
import openpyxl


dir_path = os.path.dirname(os.path.realpath(__file__))

Excel_path = dir_path+"\TestData\Testdata.xlsx"

def createFolder(directory):   # './Testdata/'
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print('Folder created successfully')
        else:
            print('Folder already exists')                
    except OSError:
        print ('Error: Creating directory. ' +  directory)
