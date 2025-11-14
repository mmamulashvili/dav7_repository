from django.shortcuts import render

def info_view(request):
    context = {
        "name": "მარიამი",
        "surname": "მამულაშვილი",
        "age": 14,
        "height": 165,
    }
    return render(request, 'info.html', context)

def hobbies_view(request):
    hobbies = ["coding", "listen to music", "dancing"]
    grade = 9
    context = {
        "hobbies": hobbies,
        "grade": grade
    }
    return render(request, 'hobbies.html', context)
