from rest_framework import serializers
from user.models import user
from user.models import clients
from user.models import project


######################################################
class companySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ['user_id','user_name','user_password']

class companyclints(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = clients
        fields = ['company_id','client_name','created_at','created_by']

class companyproject(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = project
        fields = ['project_id','project_name','Time_stand']