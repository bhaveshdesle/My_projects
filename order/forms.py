from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Pune', 'Pune'),
		('Nashik', 'Nashik'),
		('Nagpur', 'Nagpur'),
	)

	DISCRICT_CHOICES = (
		('Kolhapur','Kolhapur'), 
		('Sangli','Sangli'),
		('Satara','Satara'),
		('Solapur','Solapur'),
		('Ahmednagar','Ahmednagar'),
		('Dhule','Dhule'),
		('Jalgaon','Jalgaon'),
		('Gadchiroli','Gadchiroli'),
		('Bandhara','Bandhara'),
        ('Jabalpur','Jabalpur'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Phone Pay', 'Phone Pay'),
		('Paytm','Paytm')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
