from django.http import JsonResponse


def task_list(request):
    tasks = Task.objects.all()
    data = []
    for task in tasks:
        data.append({
            'id': task.id,
            'description': task.description,
            'status': task.status,
        })
    return JsonResponse(data, safe=False)


def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    data = {
        'id': task.id,
        'description': task.description,
        'status': task.status,
    }
    return JsonResponse(data)


def task_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task = Task.objects.create(
            description=data['description'],
            status=data['status'],
        )
        return JsonResponse({
            'id': task.id,
            'description': task.description,
            'status': task.status,
        })


def task_update(request, pk):
    if request.method == 'PUT':
        data = json.loads(request.body)
        task = Task.objects.get(pk=pk)
        task.description = data['description']
        task.status = data['status']
        task.save()
        return JsonResponse({
            'id': task.id,
            'description': task.description,
            'status': task.status,
        })


def task_delete(request, pk):
    if request.method == 'DELETE':
        task = Task.objects.get(pk=pk)
        task.delete()
        return JsonResponse({
            'message': 'Task deleted successfully.'
        })