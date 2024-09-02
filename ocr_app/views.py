from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ImageUploadForm
from .models import ExtractedText
import io
from reportlab.pdfgen import canvas
from .ocr import extract_text_from_image  # This function should handle the OCR logic

def home(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            text = extract_text_from_image(image)
            
            # Save the data into db
            extracted_text = ExtractedText.objects.create(
                image=image,
                text=text
            )
            
            return redirect('result', pk=extracted_text.pk)
    else:
        form = ImageUploadForm()
    return render(request, 'home.html', {'form': form})

def result(request, pk):
    extracted_text = ExtractedText.objects.get(pk=pk)
    return render(request, 'result.html', {'text': extracted_text.text})

def download_txt(request):
    text = request.GET.get('text', '')
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="extracted_text.txt"'
    response.write(text)
    return response

def download_pdf(request):
    text = request.GET.get('text', '')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="extracted_text.pdf"'
    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 750, text)
    p.showPage()
    p.save()
    
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


def text_list(request):
    texts = ExtractedText.objects.all()
    return render(request, 'text_list.html',{'texts':texts})