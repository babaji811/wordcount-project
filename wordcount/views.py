from django.shortcuts import render
from collections import Counter

def home(request):
    return render(request, 'index.html')

def count(request):
    yourText = request.GET['yourText']
    wordList = yourText.split()
    numberOfWords = len(wordList)
    wordDict = dict(Counter(wordList))
    sortedWordList = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)
    return render(request, 'count.html', {'yourText': yourText, 'numberOfWords': numberOfWords, 'wordDict': sortedWordList})
