#!/usr/bin/python
print "Content-Type: text/html\n"
print ""
import cgi
import urllib
import cgitb
import re
import md5
import random
import sys
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

inStream=open('894a30d7e8f4004d2cb86ea57714f148.txt','r')
data=inStream.read()
inStream.close()

def writefile():
    message='<br><br><br><br>'
    if formData.getvalue('username')==None or formData.getvalue('password1')==None or formData.getvalue('password2')==None:
        message+='''<p>Username or password not entered <3
                <p><a href="http://lisa.stuy.edu/~winton.yee/proj/register.py">Try again</a>, you lovely human.'''
    else:
        if (formData.getvalue('password1'))!=(formData.getvalue('password2')):
            message+='<p>Sorry, your passwords do not match <3'
        if (formData.getvalue('username')).find(' ')!=-1:
            message+='<p>Sorry, you cannot have a space in your username <3'
        if (formData.getvalue('password1')).find(' ')!=-1:
            message+='<p>Sorry, you cannot have a space in your password <3'
        if (formData.getvalue('username')).find(':')!=-1:
            message+='<p>Sorry, you cannot have a colon in your username <3'
        if (formData.getvalue('password1')).find(':')!=-1:
            message+='<p>Sorry, you cannot have a colon in your password <3'
        if (formData.getvalue('username')).find('~')!=-1:
            message+='<p>Sorry, you cannot have a tilde in your username <3'
        if (formData.getvalue('password1')).find('~')!=-1:
            message+='<p>Sorry, you cannot have a tilde in your password <3'
        if ((data.find(formData.getvalue('username'))+len(formData.getvalue('username')))>len(data)+1) and\
            (formData.getvalue('password1'))==(formData.getvalue('password2')) and\
           (formData.getvalue('username')).find(' ')==-1 and\
           (formData.getvalue('password1')).find(' ')==-1 and\
           (formData.getvalue('username')).find(':')==-1 and\
           (formData.getvalue('password1')).find(':')==-1 and\
           (formData.getvalue('username')).find('~')==-1 and\
           (formData.getvalue('password1')).find('~')==-1:
            user=formData.getvalue('username')+':'+md5.new(formData.getvalue('password1')).hexdigest()+ ' ' 
            with open("894a30d7e8f4004d2cb86ea57714f148.txt", "a+") as myfile:
                myfile.write(user)
            message+='Successful registration!<p>Login <a href="http://lisa.stuy.edu/~winton.yee/proj/login.py">here</a>'
            return message
            myfile.close()
            sys.exit(0)
        else:
            if data.find(formData.getvalue('username')+':')!=-1:
                message+='<p>Sorry, this username is already taken <3'
                message+='<p><a href="http://lisa.stuy.edu/~winton.yee/proj/register.py">Try again</a>, you beautiful person.'
                return message
                sys.exit(1)
        if (formData.getvalue('password1'))==(formData.getvalue('password2')) and\
           (formData.getvalue('username')).find(' ')==-1 and\
           (formData.getvalue('password1')).find(' ')==-1 and\
           (formData.getvalue('username')).find(':')==-1 and\
           (formData.getvalue('password1')).find(':')==-1 and\
           (formData.getvalue('username')).find('~')==-1 and\
           (formData.getvalue('password1')).find('~')==-1:
            user=formData.getvalue('username')+':'+md5.new(formData.getvalue('password1')).hexdigest()+ ' '
            with open("894a30d7e8f4004d2cb86ea57714f148.txt", "a+") as myfile:
                myfile.write(user)
            message+='Successful registration!<p>Login <a href="http://lisa.stuy.edu/~winton.yee/proj/login.py">here</a>'
            myfile.close()
        else:
            message+='<p><a href="http://lisa.stuy.edu/~winton.yee/proj/register.py">Try again</a>, you beautiful person.'
    return message

print writefile()
