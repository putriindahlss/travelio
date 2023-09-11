from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Putri Indah Lestari',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)