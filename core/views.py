from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# @csrf_exempt
def speech_to_text(voice):
    print('here----------------------------------')
# Instantiates a client
    client = speech.SpeechClient()

    # The name of the audio file to transcribe
    # file_name = os.path.join(
    #     os.path.dirname(__file__),
    #     'output1.flac')
    file_name = '/home/leanagri2/Desktop/project/hackathon/media/' + voice
    print(file_name,'=====================================')

    # Loads the audio into memory
    with io.open(file_name, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)
    x = ""
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
        x = x + " " + str(result.alternatives[0].transcript)
    ans = nlp_function(x)
    print(ans,'111111111111111111111111111111111111111')
    return ans




from google.cloud import language
# from google.cloud.language import enums
# from google.cloud.language import types
import requests
import paralleldots
import paralleldots
def nlp_function(data):
    paralleldots.set_api_key("pwYgvFI30sVIFqTDdbmLM68vbjYwnZ1shoCe8GXGQwk")
    text1=data
    text2="this is rajeev"
    response=paralleldots.similarity(text1,text2)
    print(response)
    return response
    # text1 = 'hello'
    # text2='hello1'
    # api_key = 'pwYgvFI30sVIFqTDdbmLM68vbjYwnZ1shoCe8GXGQwk'
    # url = 'https://apis.paralleldots.com/v4/similarity'
    # from google.cloud.language import types
    # from google.cloud.language import enums
    # # Instantiates a client
    # client = language.LanguageServiceClient()

    # # The text to analyze
    # text = data
    # document = types.Document(
    #     content=text,
    #     type=enums.Document.Type.PLAIN_TEXT)

    # # Detects the sentiment of the text
    # sentiment = client.analyze_sentiment(document=document).document_sentiment

    # print('Text: {}'.format(text))
    # print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

from django.core.files.storage import FileSystemStorage
from core.models import Document
from core.forms import DocumentForm
from django.shortcuts import redirect


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        answer_success = speech_to_text(filename)
        print(answer_success, '2222222222222222222222222222222222222')
        print(answer_success['similarity_score'], '3333333333333333333333333333333333')
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'answer_success': answer_success['similarity_score']
        })
    return render(request, 'core/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
