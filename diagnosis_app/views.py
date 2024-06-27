from django.shortcuts import render, redirect
from .forms import UploadImageForm, ReportForm
from .models import Prediction
from .utils import predict_disease
from .models import Report
from .forms import ReportForm
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, 'home.html')


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            probabilities = predict_disease(image.image.path)

            prediction = Prediction(image=image)
            prediction.CNV = round(float(probabilities['CNV']), 3)
            prediction.DME = round(float(probabilities['DME']), 3)
            prediction.DRUSEN = round(float(probabilities['DRUSEN']), 3)
            prediction.NORMAL = round(float(probabilities['NORMAL']), 3)

            prediction.confidence = round(float(max(probabilities.values())), 3)
            prediction.save()


            # Identify the predicted disease
            predicted_disease = max(probabilities, key=probabilities.get)

            # Subtract 0.001 from the predicted disease probability
            probabilities[predicted_disease] = round(float(probabilities[predicted_disease]) - 0.001, 3)


            # Store rounded probabilities in the session
            request.session['probabilities'] = {k: round(float(v), 3) for k, v in probabilities.items()}

            return redirect('predictions')  # Redirect to the predictions view
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form})


def upload_success(request):
    predictions = Prediction.objects.all()
    return render(request, 'upload_success.html', {'predictions': predictions})


def predictions(request):
    probabilities = request.session.get('probabilities', {})
    return render(request, 'predictions.html', {'predictions': probabilities})

def create_report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            new_report = form.save()
            return redirect('view_report', report_id=new_report.id)
    else:
        form = ReportForm()
    return render(request, 'create_report.html', {'form': form})

# def view_report(request, report_id):
#     report = get_object_or_404(Report, id=report_id)
#     return render(request, 'view_report.html', {'report': report})

def list_reports(request):
    reports = Report.objects.all()
    return render(request, 'list_reports.html', {'reports': reports})