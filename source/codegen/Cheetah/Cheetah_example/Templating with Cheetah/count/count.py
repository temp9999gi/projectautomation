import os.path
from Cheetah.Template import Template

# Update the count
countFile = 'count.txt'

if os.path.exists ( countFile ):
   count = int ( file ( countFile ).read() )
   count = count + 1
else:
   count = 1


   
file ('./' + countFile, 'w' ).write ( str ( count ) )

print Template ( file = 'counter.tmpl', searchList = [{ 'counter': str ( count ) }] )

