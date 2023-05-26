from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


monthly_challenges = {

    "january": "This is january",
    "febuary": "This is Febuary",
    "march": "This is March",
    "april": "This is April",
    "may": "This is May",
    "june": "This is June",
    "july": "This is July",
    "august": "This is August",
    "september": "This is September",
    "october": "This is October",
    "november": "This is November",
    "december": "This is December",
}


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
    except:
        return HttpResponseNotFound("This month  is not supported")
    return HttpResponse(challenge_text)
