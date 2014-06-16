#!/usr/bin/python
import os
import random
print 'Set-Cookie: '+os.environ.get('HTTP_COOKIE')+\
      '; expires=Wed, 31-Dec-1969 19:00:01 GMT'

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

print '<br><br><br><br><br>You are now logged out'
print '<p><a href="http://lisa.stuy.edu/~winton.yee/proj/">Phone home</a>'

