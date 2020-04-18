from django.shortcuts import render
from django.http import HttpResponse
import random
import string
import re

# Create your views here.
def home(request):
	return render(request,'generator/home.html')

def generate_password(request):
	password_chars = ''
	characterz_lowercase = string.ascii_lowercase
	characterz_uppercase = string.ascii_uppercase
	num = ''.join(str(x) for x in range(0,10))
	characterz_special = '@£$%^&*()!'


	#Params from web address
	length = int(request.GET.get('length',12))
	numbers = request.GET.get('numbers')
	uppercase = request.GET.get('uppercase')
	special_characters = request.GET.get('special_characters')

	#http://127.0.0.1:8000/password?length=10&numbers=on&uppercase=on&special_characters=on&Generate=Submit

	password_chars = characterz_lowercase

	if numbers == 'on':
		password_chars = password_chars + num

	if uppercase == 'on':
		password_chars = password_chars + characterz_uppercase 

	if special_characters == 'on':
		password_chars = password_chars + characterz_special

	pwd_generated = ''
	pwd_generated = random_pass_generator(password_chars, length)

	# while True:
	# 	pwd_generated = random_pass_generator(password_chars, length)

	# 	if valid_password(pwd_generated ,numbers, uppercase, special_characters):
	# 		break
	# 	else:
	# 		continue

	return render(request,'generator/password.html', {'password': pwd_generated})

def valid_password(pwd_generated ,numbers, uppercase, special_characters):
	if numbers == 'on':
		if bool(re.search(r'\d', pwd_generated)) == False:
			return False

	if uppercase == 'on':
		if bool(re.search(r'[A-Z]', pwd_generated)) == False:
			return False

	if special_characters == 'on':
		if bool(re.search(r'[@£$%^&*()!]', pwd_generated)) == False:
			return False


def random_pass_generator(password_chars, length):
	pwd_generated =''
	for x in range(length):
		pwd_generated += random.choice(password_chars)

	return pwd_generated