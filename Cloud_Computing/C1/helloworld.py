import os
import webapp2
from google.appengine.ext.webapp import template
from google.appengine.ext import db


class Employee1(db.Model):
    id=db.IntegerProperty(indexed=True)
    firstname=db.StringProperty()
    lastname=db.StringProperty()
    employee_dept=db.StringProperty()
    employee_salary=db.IntegerProperty()
    date=db.DateTimeProperty(auto_now_add=True)

class Mainpage(webapp2.RequestHandler):
    def get(self):
        employee_query=Employee1.all()
        employees=employee_query.fetch(10)
        template_values={'employees':employees}
        path = os.path.join(os.path.dirname(__file__),'index.html')
        self.response.out.write(template.render(path,template_values))
        
        
    
class Addemployee(webapp2.RequestHandler):
    def post(self):
        employee = Employee1()
        employee.firstname=self.request.get('firstname')
        employee.lastname=self.request.get('lastname')
        employee.employee_dept=self.request.get('employee_dept')
        employee.employee_salary=int(self.request.get('employee_salary'))
        employee.put()
        self.redirect('/')
        
    

app = webapp2.WSGIApplication([
    ('/',Mainpage),
    ('/add',Addemployee)]
    ,debug = True)
if __name__=='__main__':
    app.run()
    