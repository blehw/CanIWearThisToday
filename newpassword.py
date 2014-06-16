#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import os
import cgi
import md5
import sys
import random
import cgitb
cgitb.enable()
formData=cgi.FieldStorage()

print '''<!DOCTYPE html
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

inStream=open('894a30d7e8f4004d2cb86ea57714f148.txt','r')
data=inStream.read()
inStream.close

sessionfile=open('a49b4c00328dc77a3cdd5da5e38856a5.txt','r')
usersessions=sessionfile.read()
sessionfile.close

cookie=os.environ.get('HTTP_COOKIE')
d=usersessions.find(str(cookie))
user=''

message='<br><br><br><br><br>'
if formData.getvalue('oldpass')==None or formData.getvalue('newpass1')==None or formData.getvalue('newpass2')==None:
    message+='''Not all fields filled out <3
            <p><a href="http://lisa.stuy.edu/~winton.yee/proj/oldpassword.py">Try again</a>, you tantalizing enchanter.'''
    print message
    sys.exit(1)

while usersessions[d]!='~' and usersessions[d]!=' ':
    user+=usersessions[d]
    d+=1
useronly=''
back=-1
while user[back]!=':':
    useronly+=user[back]
    back-=1
useronly=useronly[::-1]

c=useronly+':'+md5.new(formData.getvalue('oldpass')).hexdigest()

if (formData.getvalue('newpass1'))!=(formData.getvalue('newpass2')):
    print '''<br><br><br><br><br>Sorry, your new passwords do not match <3
            <p><a href="http://lisa.stuy.edu/~winton.yee/proj/oldpassword.py">Try again</a>, you total stud.'''
elif data.find(c)==-1:
    print '''<br><br><br><br><br>Incorrect password<p><a href="http://lisa.stuy.edu/~winton.yee/proj/oldpassword.py">Try again</a>, you, who is like a summer's day.'''
else:
    if (formData.getvalue('newpass1')).find(' ')!=-1:
        message+='<br>Sorry, you cannot have a space in your password <3'
    if (formData.getvalue('newpass1')).find(':')!=-1:
        message+='<br>Sorry, you cannot have a colon in your password <3'
    if (formData.getvalue('newpass1')).find('~')!=-1:
        message+='<br>Sorry, you cannot have a tilde in your password <3'
    if (formData.getvalue('newpass1')).find(' ')==-1 and\
       (formData.getvalue('newpass1')).find(':')==-1 and\
       (formData.getvalue('newpass1')).find('~')==-1:
        a=data.find(c)+len(useronly)+1
        prevpass=''
        while data[a]!=' ':
            prevpass+=data[a]
            a+=1
        prevpass=':'+prevpass
        newpass=data.replace(prevpass, ':'+md5.new(formData.getvalue('newpass1')).hexdigest())
        newpassfile=open('894a30d7e8f4004d2cb86ea57714f148.txt','w')
        newpassfile.write(newpass)
        newpassfile.close()
        print '<br><br><br><br><br>Password changed! :D'
        print '<p><a href="http://lisa.stuy.edu/~winton.yee/proj/">Phone home</a></p>'
    else:
        message+='''<p><a href="http://lisa.stuy.edu/~winton.yee/proj/oldpassword.py">Try again</a>, you stunning stunner person.'''
        print message

