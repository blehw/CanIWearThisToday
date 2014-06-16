#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import random

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

print '''<body>

<h1>Login</h1>

<form method="post" action="check.py">

<input type="text" name="username" placeholder="Username">
<br>
<input type="password" name="password" placeholder="Password">

<p>

<input type="submit" value="Login">

</form>

<p><a href="http://lisa.stuy.edu/~winton.yee/proj/">Phone home</a>

</body>
</html>'''
