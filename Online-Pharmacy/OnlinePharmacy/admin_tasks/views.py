from django.shortcuts import render

def admin_tasks(request):
    return render(request, 'admin_tasks.html')
