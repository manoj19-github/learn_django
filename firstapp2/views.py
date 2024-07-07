from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
def showcustom(request):
    try:
        # response_data = render_to_string("challenges/challenge.html")
        months = ["january","february","march","april","june","july","august","september","octeber","november","december"]
        return render(request,"challenges/challenge.html",{"text":"hello python developer","months":months})
    except:
        return HttpResponseNotFound("not found55")
                
        