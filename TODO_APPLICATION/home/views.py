from django.shortcuts import render, HttpResponse
from home.models import Task


def home(request):
    context = {'success': False, 'name':'Bimal'}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        print(title, desc)
        ins = Task(tasktittle=title, taskdesc=desc)
        ins.save()
        context = {'success': True}
    return render(request,'index.html',context)


def tasks(request):
    allTasks = Task.objects.all()
    # print(allTasks)
    # for item in allTasks:
    #     print(item.tasktittle)
    context = {'tasks' : allTasks}
    return render(request,'tasks.html',context)