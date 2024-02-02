import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add(request):
    return perform_operation(request, 'add')


@csrf_exempt
def subtract(request):
    return perform_operation(request, 'subtract')


@csrf_exempt
def multiply(request):
    return perform_operation(request, 'multiply')


@csrf_exempt
def divide(request):
    return perform_operation(request, 'divide')


@csrf_exempt
def perform_operation(request, operation):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = int(data.get('A'))
            b = int(data.get('B'))

            if operation == 'add':
                result = a + b
            elif operation == 'subtract':
                result = a - b
            elif operation == 'multiply':
                result = a * b
            elif operation == 'divide':
                if b == 0:
                    return JsonResponse({'error': 'Division by zero!'}, status=400)
                result = a // b
            else:
                return JsonResponse({'error': 'Invalid operation'}, status=400)

            return JsonResponse({'answer': result})
        except (ValueError, KeyError):
            return JsonResponse({'error': 'Invalid data format'}, status=400)
        except ZeroDivisionError:
            return JsonResponse({'error': 'Division by zero!'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
