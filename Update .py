import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
bit = platform.architecture()[0]
 
if bit == "64bit":
        os.system('xdg-open https://www.facebook.com/mdakash.ahamed.14')
 
        os.system('python Update.py')
 
        #random()
 
 
 
elif bit == "32bit":
 
        os.system('xdg-open https://www.facebook.com/mdakash.ahamed.14')
 
        os.system('python Update.py')
 
 