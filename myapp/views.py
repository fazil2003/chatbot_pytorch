from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"chatbot.html")

def chatbot_response(request):
    from python_files.pytorch_chatbot.chat import chatbot_function
    text=request.GET['text']
    response=chatbot_function(text)
    bot_response="<p class='message bot_message'><span>Bot:</span><br>"+response+"</p>"
    return HttpResponse(bot_response)