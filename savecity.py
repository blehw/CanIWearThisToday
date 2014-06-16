#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi
import cgitb
cgitb.enable()
formData=cgi.FieldStorage()

print formData.getvalue('Save city')
