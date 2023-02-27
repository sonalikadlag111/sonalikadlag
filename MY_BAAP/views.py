from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("welcome to baap")


def course(request):
    return HttpResponse("<b>this is program</b>")


# int string or slug
def courseDetails(request, course_id):
    return HttpResponse(course_id)


# render html
def homePage(request):
    return render(request, "amy.html")


# send data from view tamplate using dictionary
def homePage(request):
    # data={
    #     'title':'my Home page',
    #     'bdata':'my name is sonali',
    #     'com':'company name is baap',
    #     'clist':['PHP','java','Django'],
    #     'stud_info':[
    #         {'name':'sonali','phone':3434343434},
    #         {'name':'swara','phone':3434343434},
    #         {'name':'namita', 'phone': 3434343434}
    #
    #     ],
    #     # if else condition
    #     'ifelselist':[10,20,30,40,50,60]
    #     # 'ifelselist': [] no data found
    # }
    # return render(request,"index.html",data)
    return render(request, "amy.html")



