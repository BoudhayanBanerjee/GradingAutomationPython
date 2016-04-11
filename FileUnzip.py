import glob
import zipfile
import os
import time

ff = r'C:\Users\boudh\Desktop\dl\ul'
af = r'C:\Users\boudh\Desktop\dl'
#this function unzips the zip files
def FileUnzip():

    zip_files = glob.glob1(af,'*.zip')
    
#------ unzip the files and store in the directory -------#
    try:
        for zip_filename in zip_files:
            dir_name = os.path.splitext(zip_filename)[0]
            dir_name = ff + '\\'+dir_name
            os.mkdir(dir_name)
            zip_handler = zipfile.ZipFile(zip_filename, "r")
            zip_handler.extractall(dir_name)
        print("Sir,all files are unzipped and ready to be checked\n")
    except Exception as e:
        print("Problem,Sir I can not unzipp the files.System says\n")
        print(e)    
    #------- remove the zipped files -------#
    time.sleep(10)

    try:
        for i in zip_files:
            os.remove(i)   
        
        print("Sir,I removed all the zipped files\n")
    except Exception as e:
        print("Problem,Sir I can not delete all the zip files.Please delete remaining files manually.\n")
            
if __name__ == '__main__':
    FileUnzip()