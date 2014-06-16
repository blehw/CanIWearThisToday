#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cookielib
import json
import urllib2
import os
import random
import cgi
import cgitb
cgitb.enable()
formData=cgi.FieldStorage()

print '''<!DOCTYPE html>
<html>
<head>
<link rel="shortcut icon" href="favicon.ico">
<title>Team Grimmie Rawwks</title>
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

print '<body><h1>Can I Wear This Today?</h1>'

def getData(query):
    try:
        response = urllib2.urlopen(\
            'http://lisa.stuy.edu/~winton.yee/proj/backEnd.py?' + query)
        responsestr=response.read()
        responsestr=responsestr.replace('''<br>
<p><a href="http://lisa.stuy.edu/~winton.yee/proj/">Phone home</a></p>''','')
        return responsestr
    except:
        return {
            'error': 404,
            'message': "We're sorry, we were unable to retrieve the data from our own damn site."
            }

if os.environ.get('HTTP_COOKIE')==None:
    print '''<a href="http://lisa.stuy.edu/~winton.yee/proj/login.py">Log in<a/>
            or <a href="http://lisa.stuy.edu/~winton.yee/proj/register.py">register
            for an account</a> to save cities and preferences</p>'''
else:
    try:
        sessionfile=open('a49b4c00328dc77a3cdd5da5e38856a5.txt','r')
        usersessions=sessionfile.read()
        sessionfile.close
        cookie=os.environ.get('HTTP_COOKIE')
        d=usersessions.find(str(cookie))
        user=''
        while usersessions[d]!='~' and usersessions[d]!=' ':
            user+=usersessions[d]
            d+=1
        useronly=''
        back=-1
        while user[back]!=':':
            useronly+=user[back]
            back-=1
        useronly=useronly[::-1]
        print 'Hello, '+useronly+'<br>'
        print '<a href="http://lisa.stuy.edu/~winton.yee/proj/logout.py">Log out<a/>'
        print '<br><a href="http://lisa.stuy.edu/~winton.yee/proj/oldpassword.py">Change password<a/>'
        sessionfile=open('a49b4c00328dc77a3cdd5da5e38856a5.txt','r')
        usersessionz=sessionfile.read()
        usersessions=' '
        counter=usersessionz.find(os.environ.get('HTTP_COOKIE'))
        while usersessionz[counter]!=' ':
            usersessions+=usersessionz[counter]
            counter+=1
        usersessions+=' '
        sessionfile.close
        if usersessions.find('~')!=-1:
            # This code is needed to set the proxy
            proxy_support = urllib2.ProxyHandler({"http":"http://149.89.1.30:3128"})
            opener = urllib2.build_opener(proxy_support)
            urllib2.install_opener(opener)
            e=usersessions.find(os.environ.get('HTTP_COOKIE'))
            querystr=''
            while usersessions[e]!=' ' and usersessions[e]!='~':
                e+=1
            e+=1
            while usersessions[e]!=' ' and usersessions[e]!='~':
                querystr+=usersessions[e]
                e+=1
            print '<p>'
            print getData(querystr)
            print '<br><a href="http://lisa.stuy.edu/~winton.yee/proj/delcity.py?'+querystr+'">Delete city</a>'
            while usersessions[e]!=' ':
                querystr=''
                e+=1
                while usersessions[e]!=' ' and usersessions[e]!='~':
                    querystr+=usersessions[e]
                    e+=1
                print '<p>'
                print getData(querystr)
                print '<br><a href="http://lisa.stuy.edu/~winton.yee/proj/delcity.py?'+querystr+'">Delete city</a>'
    except:
        print '''<a href="http://lisa.stuy.edu/~winton.yee/proj/login.py">Log in<a/>
            or <a href="http://lisa.stuy.edu/~winton.yee/proj/register.py">register
            for an account</a> to save cities and preferences</p>'''

print '<h1>Enter a city below:</h1>'
print '''<form method="GET" action="backEnd.py">

<input type="text" name="city" placeholder="City, Country...">

<p>Select the items you would like recommendations for:
<br><label for="shirt">Shirt</label>
<input type="checkbox" name="shirt" checked>
<br><label for="shorts">Shorts</label>
<input type="checkbox" name="shorts" checked>
<br><label for="sweater">Sweater</label>
<input type="checkbox" name="sweater" checked>
<br><label for="jacket">Jacket</label>
<input type="checkbox" name="jacket" checked>
<br><label for="hat">Hat</label>
<input type="checkbox" name="hat" checked>
<br><label for="umbrella">Umbrella</label>
<input type="checkbox" name="umbrella" checked>'''

if os.environ.get('HTTP_COOKIE')!=None:
    print '<p><label for="savecity">Save City</label><input type="checkbox" name="savecity" unchecked>'
    
print '''</p></p>

<input type="submit" value="Go!">

</form>

<p><a href="http://shorts.today/">Inspired by</a>
<br><a href="http://openweathermap.org/">Made possible by</a>

</body>
</html>'''
