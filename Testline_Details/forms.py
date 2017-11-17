from django import forms
from Testline_Details.models import Testlines
from django.contrib.auth.models import User

class TestlinesForm(forms.ModelForm):
    class Meta():
        model = Testlines
        fields = ('SBTS_ID','Owner','Rack','Hw_config','SBTS_Build','Cell_Info','App_IP_Addr','Active_Alarms','Setup_config','Remote_ip',
        	'Login_details','L2_switch_ip','Port',
        	'Calls','UEs','IMSI','Issues_Investigations','Status_Comments',
                  )
        
        
class UserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput())
     class Meta:
         model = User
         fields =('username','email',"password")        
