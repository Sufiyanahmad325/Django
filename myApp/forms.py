from django import forms
from .models import chaiVerity, chaiReview, Store, chaiCertificate


class chaiVerityForm(forms.Form):
    chai_Verity = forms.ModelChoiceField(queryset=chaiVerity.objects.all(), label='Select Chai Verity', empty_label='Select a chai verity') 
    # chai_Verity = forms.CharField() # ye ha pe hamne chai_Verity field ko CharField ke roop me define kiya hai taki user ko ek text input field mile jisme wo chai veriety ka naam type kar sakein
    # chai_verity = forms.CharField()