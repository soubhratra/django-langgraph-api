from django.shortcuts import render

def index(request):
    return render(request, 'chatbot_app/index.html')

def chatbot1(request):
    return render(request, 'chatbot_app/chatbot1.html')

def chatbot2(request):
    return render(request, 'chatbot_app/chatbot2.html')

