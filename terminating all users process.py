## imp note make sure to give the exception for the user prosess that will terminate other proscess
##here the name of file appending .exe is given in the exception 
##so that the terminating process would not terminatee itself

import os
os.system("pip install psutil")
os.system("pip3 install psutil")
import psutil
for proc in psutil.process_iter(['pid', 'name', 'username']):
    try:
        if((proc.info['username'] == None)):
            print('skipped :',proc.info['pid'])
        elif((proc.info['name'] == None)):
            print('skipped :',proc.info['pid'])
        elif('WindowsTerminal.exe' in proc.info['name']):
            print('skipped :',proc.info['pid'])
        elif('terminating all users process.exe' in proc.info['name']):   #################the process### ref imp above###
            print('skipped :',proc.info['pid'],proc.info['name'])
        elif('conhost.exe' in proc.info['name']):
            print('skipped :',proc.info['pid'])
        elif('explorer.exe' in proc.info['name']):
            print('skipped :',proc.info['pid'])
        elif('cmd.exe' in proc.info['name']):
            print('skipped :',proc.info['pid'])        
        elif(psutil.users()[0][0] not in proc.info['username']):
            print('skipped :',proc.info['pid'])
        else:
            print(proc.info)
            #x=input('else : ')
            print('killed')
            proc.kill()
    except Exception as e:
            print(e)
            pass