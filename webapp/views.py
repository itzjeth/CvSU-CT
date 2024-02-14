from django.http import HttpResponse
from django.shortcuts import render, redirect

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot', read_only=False,logic_adapters=['chatterbot.logic.BestMatch'])

list_to_train = [
    "hi there",
    "What's your name?",
    "I'm Sting",
    "What is your fav food?",
    "I like fish",
    "What is your fav color?",
    "I like black"
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def home_page(request):
    return render(request, 'pages/home.html')


def chatbot_page(request):
    return render(request, 'pages/chatbot.html')

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    chatResponse = str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)















