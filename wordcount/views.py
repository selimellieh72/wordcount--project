from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request, "home.html")
def count(request):
    text = request.GET["text"]
    textintolist = text.split()
    my_dictionary = {}
    for word in textintolist:
        if word in my_dictionary:
            my_dictionary[word] += 1
        else:
            my_dictionary[word] = 1
    sorted_dic = sorted(my_dictionary.items(), key = lambda x: x[1], reverse= True)
    return render(request, "count.html", {"text" : text, "count": len(textintolist), "my_dictionary": sorted_dic})
def about(request):
    return render(request, "about.html")