#!/usr/bin/python
import cgi
import urllib
import random
import os
import sys
import re
import md5
import urllib
import cgitb
cgitb.enable()
formData=cgi.FieldStorage()
session=random.randint(1,1000000)
print 'Set-Cookie: '+str(session)
print "Content-Type: text/html\n"
print ""

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

inStream=open('894a30d7e8f4004d2cb86ea57714f148.txt','r')
data=inStream.read()
inStream.close

sessionfile=open('a49b4c00328dc77a3cdd5da5e38856a5.txt','r')
usersessions=sessionfile.read()
sessionfile.close

if formData.getvalue('username')==None or formData.getvalue('password')==None:
    print '<br><br><br><br><br>Username or password not entered.'
    print '''<p><a href="http://lisa.stuy.edu/~winton.yee/proj/login.py">Try again</a>, you, who is like a summer's day.
             <p>Do you mean to <a href="http://lisa.stuy.edu/~winton.yee/proj/register.py">sign up</a>?'''
    sys.exit(1)

def check(username,password):
    if data!='':
        c=username+':'+password
    else:
        print '''Error, but you're the first on the site. Go <a href="http://lisa.stuy.edu/~winton.yee/proj/register.py">sign up</a>!'''
        sys.exit(1)
    if data.find(c)==-1:
        return '''<br><br><br><br><br>Incorrect username or password.
                <p><a href="http://lisa.stuy.edu/~winton.yee/proj/login.py">Try again</a>, you, who is like a summer's day.
                <p>Do you mean to <a href="http://lisa.stuy.edu/~winton.yee/proj/register.py">sign up</a>?'''
    else:
        try:
            if usersessions[usersessions.find(username)+len(username)]==' ' or\
            usersessions[usersessions.find(username)+len(username)]=='~':
                a=usersessions.find(username)-2
                prevsession=''
                while usersessions[a]!=' ':
                    prevsession+=usersessions[a]
                    a-=1
                prevsession=prevsession[::-1]
                newusersession=usersessions.replace(prevsession, str(session))
                newsessionfile=open('a49b4c00328dc77a3cdd5da5e38856a5.txt','w')
                newsessionfile.write(newusersession)
                newsessionfile.close()
            else:
                with open("a49b4c00328dc77a3cdd5da5e38856a5.txt", "a+") as myfile:
                    myfile.write(str(session)+':'+formData.getvalue('username')+' ')
                myfile.close()
        except:
            with open("a49b4c00328dc77a3cdd5da5e38856a5.txt", "a+") as myfile:
                myfile.write(str(session)+':'+formData.getvalue('username')+' ')
            myfile.close()
        return '''<br><br><br><br><br>Successful login!
                <p><a href="http://lisa.stuy.edu/~winton.yee/proj/">Phone home</a>'''
                
print check(formData.getvalue('username'),md5.new(formData.getvalue('password')).hexdigest())

