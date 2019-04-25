from django import forms
import re #regular exception
from django.contrib.auth.models import User 
from django.core.exceptions import ObjectDoesNotExist #check exists 

class RegistrationFrom(forms.Form):
	"""docstring for RegistrationFrom"""
	username = forms.CharField(label = 'Tài khoản', max_length=30)
	email = forms.CharField(label = 'Email')
	password = forms.CharField(label = 'Mật khẩu', widget=forms.PasswordInput()) #not show pass
	repassword = forms.CharField(label = 'Nhập lại mật khẩu', widget=forms.PasswordInput()) #not show pass

	def clean_repassword(self): #check repassword
		if 'password' in self.cleaned_data:
			password = self.cleaned_data['password']
			repassword = self.cleaned_data['repassword']

			if password == repassword and password: #check continuity space
				return repassword
		raise forms.ValidationError("Mật khẩu không hợp lệ")
	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$', username): #\w: ky tu thuong
			raise forms.ValidationError("Tên tài khoản có ký tự đặc biệt")
		#check user exist
		try:
			User.objects.get(username = username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError("Tên tài khoản đã tồn tại")
	#save
	def save(self):
		User.objects.create_user(username = self.cleaned_data['username'], email = self.cleaned_data['email'],
			password = self.cleaned_data['username']) 