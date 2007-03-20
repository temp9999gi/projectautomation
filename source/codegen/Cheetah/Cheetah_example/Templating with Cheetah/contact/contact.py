# All we need to do is create an object with the above properties and pass it under the profile key:

from Cheetah.Template import Template

class Profile:
   def __init__ ( self, name, email, phone, msn, aim, icq, yim ):
      self.name = name
      self.email = email
      self.phone = phone
      self.msn = msn
      self.aim = aim
      self.icq = icq
      self.yim = yim

johnDoe = Profile ( 'John Doe', 'jdoe@google.com', '(555) 555-5555', \
                    'jdoe@google.com', 'JDoe', '0123456789', 'JDoe' )

print Template ( file = 'contact.tmpl', searchList = 
[{ 'profile': johnDoe }] )
