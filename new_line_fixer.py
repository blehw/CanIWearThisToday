## the MAGIC NEWLINE FIXER
##
## by
##
## ooo        ooooo          oooo    oooo 
## `88.       .888'          `888   .8P'  
##  888b     d'888  oooo d8b  888  d8'    
##  8 Y88. .P  888  `888""8P  88888[      
##  8  `888'   888   888      888`88b.    
##  8    Y     888   888      888  `88b.  
## o8o        o888o d888b    o888o  o888o 
## 
## Remedies the Windows newline problem.
## Usage:
## $ python new_line_fixer.py <fileToFix>    


import sys

if len(sys.argv)>1:
    fileName=sys.argv[1]    
    f=open(fileName)
    s=f.read()
    f.close()
    f=open(fileName,'w')
    f.write(s.replace('\r\n','\n'))
    f.close()
else:
    print "Error: No arguments given. (File to fix not specified.)"
    print "Proper syntax: 'python new_line_fixer.py fileToFix'"
