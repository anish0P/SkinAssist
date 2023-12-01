
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from .prediction.predict import getPrediction

@csrf_exempt
def detect_skin_disease(request):
    if request.method == 'POST':
        # Assuming your image file input name is 'image'
        uploaded_image = request.FILES.get('image')

        if not uploaded_image:
            return JsonResponse({'error': 'No image file provided'})

        # Save the uploaded image to a temporary location (change as needed)
        with open('temp_image.jpg', 'wb') as destination:
            for chunk in uploaded_image.chunks():
                destination.write(chunk)

        # Use your prediction function to get the result
        prediction_result = getPrediction('temp_image.jpg')

        # Dummy accuracy for testing
        accuracy = 90.5

        # Dummy response for testing
        result = {
            'prediction': prediction_result,
            'accuracy': accuracy,
        }

        return JsonResponse(result)

    # Handle other HTTP methods if needed
    return JsonResponse({'error': 'Invalid request method'})
