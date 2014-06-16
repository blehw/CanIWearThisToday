#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

# .___________. _______     ___      .___  ___.                                        
# |           ||   ____|   /   \     |   \/   |                                        
# `---|  |----`|  |__     /  ^  \    |  \  /  |                                        
#     |  |     |   __|   /  /_\  \   |  |\/|  |                                        
#     |  |     |  |____ /  _____  \  |  |  |  |                                        
#     |__|     |_______/__/     \__\ |__|  |__|                                        
#                                                                                      
#   _______ .______       __  .___  ___. .___  ___.  __   _______                      
#  /  _____||   _  \     |  | |   \/   | |   \/   | |  | |   ____|                     
# |  |  __  |  |_)  |    |  | |  \  /  | |  \  /  | |  | |  |__                        
# |  | |_ | |      /     |  | |  |\/|  | |  |\/|  | |  | |   __|                       
# |  |__| | |  |\  \----.|  | |  |  |  | |  |  |  | |  | |  |____                      
#  \______| | _| `._____||__| |__|  |__| |__|  |__| |__| |_______|                     
#                                                                                      
# .______          ___   ____    __    ____ ____    __    ____  __  ___      _______.  
# |   _  \        /   \  \   \  /  \  /   / \   \  /  \  /   / |  |/  /     /       |  
# |  |_)  |      /  ^  \  \   \/    \/   /   \   \/    \/   /  |  '  /     |   (----`  
# |      /      /  /_\  \  \            /     \            /   |    <       \   \      
# |  |\  \----./  _____  \  \    /\    /       \    /\    /    |  .  \  .----)   |     
# | _| `._____/__/     \__\  \__/  \__/         \__/  \__/     |__|\__\ |_______/      
#                                                                                      
#   _______ .__   __.  __    __       _______ .______    __          ____        ___   
#  /  _____||  \ |  | |  |  |  |     /  _____||   _  \  |  |        |___ \      / _ \  
# |  |  __  |   \|  | |  |  |  |    |  |  __  |  |_)  | |  |          __) |    | | | | 
# |  | |_ | |  . `  | |  |  |  |    |  | |_ | |   ___/  |  |         |__ <     | | | | 
# |  |__| | |  |\   | |  `--'  |    |  |__| | |  |      |  `----.    ___) |  __| |_| | 
#  \______| |__| \__|  \______/      \______| | _|      |_______|   |____/  (__)\___/  

import cgi
import cgitb
import json
import urllib2
import random
import sys
import os
cgitb.enable()
formData=cgi.FieldStorage()
 
# This code is needed to set the proxy
proxy_support = urllib2.ProxyHandler({"http":"http://149.89.1.30:3128"})
opener = urllib2.build_opener(proxy_support)
urllib2.install_opener(opener)

def getData(query):
    try:
        response = urllib2.urlopen(\
            'http://api.openweathermap.org/data/2.5/weather?q=' + query)
        jayson = response.read()
        response.close()
        return json.loads(jayson)
    except:
        return {
            'error': 404,
            'message': "We're sorry, we were unable to retrieve the data from the OpenWeatherMap API."
            }

print "<!DOCTYPE html>"
print "<html>"
print "<head>"
print "<title>Can I Wear This Today?</title>"
print '''<link rel="shortcut icon" href="favicon.ico">'''
    
try:
    data=getData(formData.getvalue('city').replace(' ','_'))
    test=data['main']
except:
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
    print "</head>"
    print "<body>"
    print '<br><br><br><br><br>Bleep  bloop.City. Boop. Not found.'
    print '<p><a href="http://lisa.stuy.edu/~winton.yee/proj/">Phone home</a>'
    sys.exit(1)

refinedData = {
"weather": data['weather'][0]['main'],
"summary": data['weather'][0]['description'], 
"temp": {
    "hi": data['main']['temp_max'] - 273.15,
    "lo": data['main']['temp_min'] - 273.15,
    "now": data['main']['temp'] - 273.15
    },
"wind": data['wind']['speed'],
"% humidity": data['main']['humidity']
}
tempCelsius = refinedData['temp']['now']
wind = refinedData['wind']
weather = refinedData['weather']

img=''
if tempCelsius<=7.5:
    img='winter-wide.png'
elif tempCelsius<=21:
    img='fall-wide.png'
elif tempCelsius<=26.5:
    img='spring-wide.png'
else:
    img='summer-wide.png'

if weather == 'Snow':
    img='winter-snow-wide'

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
print "</head>"
print "<body>"

print "<h1>Weather for " + data['name']+', '+data['sys']['country'] + "</h1>"

# Aggregate the output text into a list, then print all at once.
output = []

# Start by telling the temperature
output.append("It is " + str(tempCelsius) + "&deg;C/" +  str((tempCelsius*9/5)+32) + "&deg;F.<br>")

#      _______. __    __   __  .______     .___________.
#     /       ||  |  |  | |  | |   _  \    |           |
#    |   (----`|  |__|  | |  | |  |_)  |   `---|  |----`
#     \   \    |   __   | |  | |      /        |  |     
# .----)   |   |  |  |  | |  | |  |\  \----.   |  |     
# |_______/    |__|  |__| |__| | _| `._____|   |__|     

layers = ''
if tempCelsius <= 1:
    layers = "three thick layers"
elif tempCelsius <= 21:
    layers = "two moderate layers"
elif tempCelsius <= 35:
    layers = "one thin layer"

# sleeves and pant legs, which are basically sleeves for your lower limbs
sleeves = " "
if tempCelsius >= 0 and tempCelsius <= 21:
    if random.randrange(2) == 0:
        sleeves = "Wear a long-sleeved shirt."
    else:
        sleeves = "It is a good idea to wear a long-sleeved shirt today."
elif tempCelsius <= 32:
    if random.randrange(2) == 0:
        sleeves = "Wear a short-sleeved shirt."
    else:
         sleeves = "We advise you wear a short-sleeved shirt."
elif tempCelsius > 32:
    if random.randrange(2) == 0:
        sleeves = "Wear a sleeveless shirt."
    else:
        sleeves = "No sleeves required. Go forth!"
else:
    if random.randrange(2) == 0:
        sleeves = "Stay home, it's too cold outside."
    else:
        sleeves = "It will be extremely cold today. If you can stay home, the better."

if 'shirt' in formData and formData.getvalue('shirt') == 'on':
    if layers != '':
        output.append("Wear " + layers + " today.")
    else:
        output.append('''Do the Vladimir Putin...
    <br>
    <img src="vlad.jpg" width="150">
    <br>
    ...or go with a T-shirt.<br>''')
    output.append(sleeves)

#     _______. __    __    ______   .______     .___________.    _______.
#    /       ||  |  |  |  /  __  \  |   _  \    |           |   /       |
#   |   (----`|  |__|  | |  |  |  | |  |_)  |   `---|  |----`  |   (----`
#    \   \    |   __   | |  |  |  | |      /        |  |        \   \    
#.----)   |   |  |  |  | |  `--'  | |  |\  \----.   |  |    .----)   |   
#|_______/    |__|  |__|  \______/  | _| `._____|   |__|    |_______/    

shorts = " "
if (20 <= tempCelsius < 32 and 0 < wind < 8) or \
   (tempCelsius >= 32):
    if random.randrange(2)== 0:
        shorts = "Let your calves be free! Put on some shorts!"
    else:
        shorts = "It's shorts season!"
else:
    if random.randrange(2) == 0:
        shorts = "Abort shorts."
    else:
        shorts = "Shorts are a no go."

if 'shorts' in formData and formData.getvalue('shorts') == 'on':
    output.append(shorts)

#      _______.____    __    ____  _______     ___   .___________. _______ .______      
#     /       |\   \  /  \  /   / |   ____|   /   \  |           ||   ____||   _  \     
#    |   (----` \   \/    \/   /  |  |__     /  ^  \ `---|  |----`|  |__   |  |_)  |    
#     \   \      \            /   |   __|   /  /_\  \    |  |     |   __|  |      /     
# .----)   |      \    /\    /    |  |____ /  _____  \   |  |     |  |____ |  |\  \----.
# |_______/        \__/  \__/     |_______/__/     \__\  |__|     |_______|| _| `._____|

sweater = " "
if tempCelsius <= 15 or (tempCelsius <=18.5 and wind >= 8):
    if random.randrange(2) == 0:
        sweater = '''<a href="https://www.youtube.com/watch?v=GCdwKhTtNNw">It's sweather weather!</a>'''
    else:
        sweater = "You'll be needing that embarassing Christmas sweater today."
else:
    if random.randrange(2) == 0:
        sweater = "Better without a sweater."
    else:
        sweater = "Wool doesn't feel that good anyway. No sweater, dude."

if 'sweater' in formData and formData.getvalue('sweater') == 'on':
    output.append(sweater)

#        __       ___       ______  __  ___  _______ .___________.
#       |  |     /   \     /      ||  |/  / |   ____||           |
#       |  |    /  ^  \   |  ,----'|  '  /  |  |__   `---|  |----`
# .--.  |  |   /  /_\  \  |  |     |    <   |   __|      |  |     
# |  `--'  |  /  _____  \ |  `----.|  .  \  |  |____     |  |     
#  \______/  /__/     \__\ \______||__|\__\ |_______|    |__|     

jacket = " "
if tempCelsius <= 9 or (tempCelsius <=13 and wind >= 8):
    if random.randrange(2) == 0:
        jacket = "Jacket necessary, leather optional."
    else:
         jacket = "This might not be Hoth, but you still need a jacket."
else:
    if random.randrange(2) == 0:
        jacket = "Leave the jacket at home."
    else:
        jacket = "Jackets are so yesterday."

if 'jacket' in formData and formData.getvalue('jacket') == 'on':
    output.append(jacket)

# .___________.  ______   .______       __       __   _______       _______.
# |           | /  __  \  |   _  \     |  |     |  | |       \     /       |
# `---|  |----`|  |  |  | |  |_)  |    |  |     |  | |  .--.  |   |   (----`
#     |  |     |  |  |  | |   ___/     |  |     |  | |  |  |  |    \   \    
#     |  |     |  `--'  | |  |         |  `----.|  | |  '--'  |.----)   |   
#     |__|      \______/  | _|         |_______||__| |_______/ |_______/    

hat = " "
if data['clouds']['all']<=50:
    if random.randrange(2) == 0:
        hat = "Few clouds = hat time."
    else:
        hat = "Show off that beanie/snapback/sombrero today."
else:
    if random.randrange(2) == 0:
        hat = "Cloudy day; the hat is an eh."
    else:
        hat = "Show off your beautiful head! No hat today."

if 'hat' in formData and formData.getvalue('hat') == 'on':
    output.append(hat)

#  __    __  .___  ___. .______   .______       _______  __       __          ___      
# |  |  |  | |   \/   | |   _  \  |   _  \     |   ____||  |     |  |        /   \     
# |  |  |  | |  \  /  | |  |_)  | |  |_)  |    |  |__   |  |     |  |       /  ^  \    
# |  |  |  | |  |\/|  | |   _  <  |      /     |   __|  |  |     |  |      /  /_\  \   
# |  `--'  | |  |  |  | |  |_)  | |  |\  \----.|  |____ |  `----.|  `----./  _____  \  
#  \______/  |__|  |__| |______/  | _| `._____||_______||_______||_______/__/     \__\ 

umbrella = ""
if weather == 'Rain':
    umbrella = '''Fetch that umbrella, cause <a href="http://youtu.be/tu812Bs_0RM?t=36s">it will rain</a>.'''
else:
    if random.randrange(2) == 0:
        umbrella = "Goodbye rain, hello world!"
    else:
        umbrella = "No rain to screw up your day!"
    
if 'umbrella' in formData and formData.getvalue('umbrella') == 'on':
    output.append(umbrella)

snow = ""
if weather == 'Snow':
    snow = '''<a href="https://www.youtube.com/watch?v=mN7LW0Y00kE&feature=kp">Prepare yourself...</a>'''

output.append(snow)

sessionfile=open('a49b4c00328dc77a3cdd5da5e38856a5.txt','r')
usersessions=sessionfile.read()
sessionfile.close

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

if 'savecity' in formData and formData.getvalue('savecity') == 'on':
    e=usersessions.find(os.environ.get('HTTP_COOKIE'))
    while usersessions[e]!=' ':
        e+=1
    with open("a49b4c00328dc77a3cdd5da5e38856a5.txt", "w") as myfile:
        myfile.write(usersessions[:e]+'~'+\
        'city='+formData.getvalue('city').replace(' ','_')+\
        saveshirt+saveshorts+savesweater+\
        savejacket+savehat+saveumbrella+' '+\
        usersessions[e+1:]+' ')
    myfile.close()

# Putting it all together
print "<br>".join(output)

print '<p><a href="http://lisa.stuy.edu/~winton.yee/proj/">Phone home</a></p>'
print "</body>"
print "</html>"
