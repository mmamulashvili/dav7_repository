from django.shortcuts import render

def info_view(request):
    context = {
        "name": "თქვენი სახელი",
        "surname": "თქვენი გვარი",
        "age": 17,
        "height": 180,
    }
    return render(request, 'info.html', context)

def hobbies_view(request):
    hobbies = ["coding", "reading", "gaming"]
    grade = 12
    context = {
        "hobbies": hobbies,
        "grade": grade
    }
    return render(request, 'hobbies.html', context)
