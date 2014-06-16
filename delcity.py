#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
import random
import cgi
import cgitb
cgitb.enable()
formData=cgi.FieldStorage()

print '''<!DOCTYPE html>
<html>
<head>
<link rel="shortcut icon" href="favicon.ico">
<title>Can I Wear This Today?</title>
<meta charset="UTF-8">
</head>'''

imgnum=random.randint(0,3)
img=''
if imgnum==0:
    img='winter-wide.png'
if imgnum==1:
    img='fall-wide.png'
if imgnum==2:
    img='spring-wide.png'
if imgnum==3:
    img='summer-wide.png'

print '''<style>
body
{ 
background-image:url('''+img+''');
background-repeat:no-repeat;
background-attachment:fixed;
background-position:center
}
body {
    font-family: Futura, Helvetica, sans-serif;
    color: rgb(255,255,255);
     text-align: Center;
}
</style>'''

sessionfile=open('a49b4c00328dc77a3cdd5da5e38856a5.txt','r')
usersessions=sessionfile.read()
sessionfile.close

def delcity(query):
    e=usersessions.find(query)
    with open ("a49b4c00328dc77a3cdd5da5e38856a5.txt", "w") as myfile:
        myfile.write(usersessions[:e-1]+usersessions[(e+len(query)):])
    myfile.close()
    return '<br><br><br><br><br>City successfully removed! :D'

saveshirt=''
saveshorts=''
savesweater=''
savejacket=''
savehat=''
saveumbrella=''

if 'shirt' in formData and formData.getvalue('shirt') == 'on':
    saveshirt='&shirt=on'
if 'shorts' in formData and formData.getvalue('shorts') == 'on':
    saveshorts='&shorts=on'
if 'sweater' in formData and formData.getvalue('sweater') == 'on':
    savesweater='&sweater=on'
if 'jacket' in formData and formData.getvalue('jacket') == 'on':
    savejacket='&jacket=on'
if 'hat' in formData and formData.getvalue('hat') == 'on':
    savehat='&hat=on'
if 'umbrella' in formData and formData.getvalue('umbrella') == 'on':
    saveumbrella='&umbrella=on'

delstr='city='+formData.getvalue('city').replace(' ','_')+\
        saveshirt+saveshorts+savesweater+\
        savejacket+savehat+saveumbrella

print delcity(delstr)
print '<p><a href="http://lisa.stuy.edu/~winton.yee/proj/">Phone home</a></p>'

    
