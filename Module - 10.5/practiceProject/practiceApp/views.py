from django.shortcuts import render
from datetime import datetime
# Create your views here.
def about(request):
    d={"name":"Uzzal Hoshen","age":18,"lst":["cpp","is","the","best","Programmig","Language"],"Today":datetime.now(),"val":"","addValue":80,"addlst":["1","2","3"],"cap":"earthly","cutFilter1":"String with spaces","cutFilter2":"January - February - March", "Distsort":[
   {'name': 'Uzzal', 'age': 19},
   {'name': 'priya', 'age': 21},
   {'name': 'priynaka', 'age': 16},
],"Escape":"<p>You are <em>pretty</em> smart!</p>","FirstFilter":['Apple', 'Mango', 'Orange'],"LastFilter":['Apple', 'Mango', 'Orange'],"LineNum":"cat do horse","TitleFilter":"Django framework","RandomFilter":['Banana', 'Mango', 'Orange'],"SliceFilter":['Banana', 'Mango', 'Orange'],"TimeFilter":datetime.now(),"TimesinceFilter":datetime.now()}
    return render(request,"practiceApp/home.html",context=d)