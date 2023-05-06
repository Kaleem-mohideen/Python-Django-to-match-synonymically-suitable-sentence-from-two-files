from django.shortcuts import render
from .utils import *

# Create your views here.


def index(request):
    # if request.method =="POST":
        # name = request.POST.get('name', '')
        # num = request.POST.get('phone', '')
        # email = request.POST.get('email', '')
        # msg = request.POST.get('msg', '')
        # print(name)

        # contact = Contact(name=name, email=email, phone=num, msg=msg)
        # contact.save()
    return render(request, 'similarString/index.html')

def findsentence(request):
	if request.method =="POST":
		
		sentence1 = request.POST.getlist('your_string', '')
		print(type(request.FILES['inputfile']))
		# with open(request.FILES['inputfile']) as f:
		#     stocks = f.read().splitlines()
		# print(stocks)
		if 'inputfile' in request.FILES:

		    sentence2 = [s.decode('utf8').strip("\t") for s in request.FILES['inputfile'].read().splitlines() if s.decode('utf8').strip("\r\n")]
		    print("sentence2", sentence2)
		    # for line in sentence2:
			   #  print(line.rstrip('\n'))
		# sentence2 = request.POST.get('inputfile', '')
		
		
		print(sentence1)
		print(type(sentence1))
		similarSentence = compare(request, sentence1, sentence2)
		print('similarSentence', similarSentence)


	return render(request, 'similarString/output.html', context={'similarSentence':similarSentence['similarSentence'], 'sentence1':sentence1, 'sentence2': sentence2})