from SendEmailAttachment import SendEmailAttachment
from MakeZip import MakeZip
import csv
import os
import shutil
import glob
import time

ff = r'C:\Users\boudh\Desktop\dl\ul'
af = r'C:\Users\boudh\Desktop\dl'

email_dict={'AbigailEdgington':'aedgingt@iastate.edu',
             'AlexSplittgerber' :'ajsplit@iastate.edu',
             'AlexandriaForbes' :'atforbes@iastate.edu',
             'AlexandriaLemke' :'adlemke@iastate.edu',
             'BilliLovan' :'bllovan@iastate.edu',
             'BrklynBraaksma' :'braaksma@iastate.edu',
             'CaeonaKrivolavy' :'cakriv18@iastate.edu',
             'CaliseHammes' :'cahammes@iastate.edu',
             'CarlyHubbard' :'chubbard@iastate.edu',
             'CassieFuerstenberg' :'cassief@iastate.edu',
             'ChristopherNuckolls' :'cjn@iastate.edu',
             'DaceyLannutti' :'lannutti@iastate.edu',
             'DenverJohnson' :'denverj@iastate.edu',
             'EmilyLogan' :'evlogan@iastate.edu',
             'HeatherDanburg' :'hdanburg@iastate.edu',
             'JeffreyDowns' :'jdowns@iastate.edu',
             'JessicaLuna' :'jyluna@iastate.edu',
             'JessieHeintz' :'jheintz@iastate.edu',
             'JesusGil' :'jgil@iastate.edu',
             'JodyHagedorn' :'jodyh@iastate.edu',
             'KalenMartsching' :'kalenm@iastate.edu',
             'KaraHutton' :'kehutton@iastate.edu',
             'KatrinaChoong' :'kachoong@iastate.edu',
             'KaylynnGlance' :'kmglance@iastate.edu',
             'KyleeHoskey' : 'kyhoskey@iastate.edu',
             'LeslieMartinez-Lopez' :'lesliem@iastate.edu',
             'MollyHelgren' :'mhelgren@iastate.edu',
             'SamanthaChizek' :'schizek@iastate.edu',
             'SavannahMendenhall' :'srm2@iastate.edu',
             'TaylorBlatchford' :'tblatchf@iastate.edu',
             'YentingChen' :'yentingc@iastate.edu'
}

def SendFeedback():
    zip_files = glob.glob1(af,'*.zip')
    countm = 0

    for filename in zip_files:
        studentname = filename[0:int(filename.find('G5'))].replace(' ','')
        studentemail = email_dict[studentname]
        SendEmailAttachment(studentemail,filename)
        countm += 1
    print("Total email sent ",countm)
        

def MakeZipC():
    subdirectories = os.listdir(ff)
    countf =0
    for i in subdirectories:
        basedir = ff + '\\' + i
        archivename = af +'\\'+i+'.zip'
        MakeZip(basedir, archivename)
        countf +=1
    print("Folders zipped succesfully ",countf)

def main():
    try:    
        MakeZipC()
    except Exception as e:
        print("Problem,Sir I can not create zip files.\n")
        print(e)
    try:
        SendFeedback()
    except Exception as e:
        print("Problem,Sir I can not send email.\n")
        print(e)

    #----------- delete the folders from ul folder ----------#
    time.sleep(60)
    shutil.rmtree(ff)
    os.mkdir(ff)


if __name__ == '__main__':
    main()