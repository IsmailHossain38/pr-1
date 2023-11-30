from django.shortcuts import render
import datetime

# Create your views here.
def about(request):
    d = {'author': 'Ismail hossan' ,
         'Age':21 ,
         'Department':'computer',
         'Joining_date': datetime.datetime.now(),
         'default':'',
         'lst':[
             
                {'name': 'zed', 'age': 19},
                {'name': 'amy', 'age': 22},
                {'name': 'joe', 'age': 31},

         ]}
    return render(request,'first_app/about.html',d)


def contect(request):
    return render(request ,'first_app/contect.html')
