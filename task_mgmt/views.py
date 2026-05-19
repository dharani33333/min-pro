from django.shortcuts import render, redirect
from django.http import JsonResponse
from task_mgmt.models import Tasks
from django.views.decorators.csrf import csrf_exempt
import json


def TaskView(request):
    if request.method == "POST":
        data = request.POST
        task_name = data.get('task-name')
        due_date = data.get('due-date')
        task = Tasks.objects.create(task_name=task_name, due_date=due_date)
        task.save()
        return redirect("Task-page")
    query = Tasks.objects.all().order_by('due_date')
    return render(request, 'task.html', context={"task": query})


@csrf_exempt
def update_task(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode('utf-8'))
        task = Tasks.objects.filter(id=data.get('task_id'))
        if len(task) == 0:
            return JsonResponse({"status": False, "message": "Task not found"})
        task = task[0]
        if data.get('is_completed') == True:
            task.is_completed = True
        else:
            task.is_completed = False
        task.save()
      
        return JsonResponse({"status": True,
                             "message": "Task updated successfully"
                             })
    else:
        return JsonResponse({"status": False,
                             "message": "Invalid request method"
                             })


@csrf_exempt
def delete_task(request):
    if request.method == "DELETE":
        data = json.loads(request.body.decode('utf-8'))
        task = Tasks.objects.filter(id=data.get('task_id'))
        if len(task) == 0:
            return JsonResponse({"status": False, "message": "Task not found"})
        task[0].delete()

        return JsonResponse({"status": True,
                             "message": "Task deleted successfully"
                             })
    else:
        return JsonResponse({"status": False,
                             "message": "Invalid request method"
                             })
