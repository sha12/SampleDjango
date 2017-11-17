from django.contrib import admin
from Testline_Details.models import Testlines
from django.contrib.admin.templatetags.admin_modify import prepopulated_fields_js

admin.site.site_header = 'Administration'

class TestlinesAdmin(admin.ModelAdmin):
    #prepopulated_fields={'slug':('SBTS_ID',)}
    list_display = ('SBTS_ID','Owner','Rack','Hw_config','Radio_modules','SBTS_Build','Cell_Info','App_IP_Addr', 'Active_Alarms',
        "Remote_ip","Login_details","L2_switch_ip","Port",
    	"Setup_config",'Calls','Issues_Investigations','Status_Comments','lastmodifiedon','lastmodifiedby')


admin.site.register(Testlines,TestlinesAdmin)
# Register your models here.
