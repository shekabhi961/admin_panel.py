import urllib
from urllib import request
import re


url = "http://aunico.in"

pesse = ('admin/','administrator/','login.php','administration/',"administrator/index.asp","administrator/account.asp",
"adminpanel.asp","fileadmin/","fileadmin.php")


for hany in pesse :
    curly = url+hany
    try :
        openurl = urllib.request.urlopen(curly)
        print("ADMIN PAGE FOUND " + curly)
    except urllib.request.URLError as msg:
        print(" SORRY NOT FOUND : " + curly)

if "([\w\-\.]+[\-\.][\w\-\.]+)" == url :
    print(re.match("([\w\-\.]+[\-\.][\w\-\.]+)"),url)
else:
    print("fail")