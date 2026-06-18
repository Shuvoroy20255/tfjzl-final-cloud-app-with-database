from django.shortcuts import render
from django.http import HttpResponse

def submit(request):
    """
    Function to handle exam submission.
    """
    if request.method == 'POST':
        # Add your form submission or database saving logic here
        return HttpResponse("Successfully Submitted!")
        
    return render(request, 'submit.html')  # Change to your actual template name


def show_exam_result(request):
    """
    Function to display the exam results.
    """
    # Add your logic to fetch results here
    context = {
        'result': 'Passed',
        'score': '85%'
    }
    return render(request, 'exam_result.html', context)  # Change to your actual template name
