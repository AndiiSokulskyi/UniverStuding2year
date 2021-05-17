from rest_framework import serializers
from .models import ForeignID
from .validators import Validation



class ForeignIDDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ForeignID
        fields = '__all__'

        extra_kwargs = {
            'country_code': {'validators': [Validation.cc_valid]},
            'passport_no': {'validators': [Validation.pn_valid]},
            'first_name': {'validators': [Validation.alfa_valid]},
            'last_name': {'validators': [Validation.alfa_valid]},
            'date_of_birth': {'validators': [Validation.birth_valid]},
            'date_of_issue': {'validators': [Validation.issue_valid('date_of_birth')]},
            'date_of_expire': {'validators': [Validation.expire_valid('date_of_issue')]}
        }
