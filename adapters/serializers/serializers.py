from adapters.models.models import Encroachment_table
from rest_framework import serializers

class EncroachmentSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.ListField(child=serializers.CharField())
    encrt_type = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Encroachment_table
        fields = ('id','encrt_id','encrt_type','department', 'status','assigned_to','follow_up_by','resolved_by','audited_on','reject_reason','region','subregion','encrt_size','dist_coa','criticality')
        extra_kwargs = {
            'assigned_to': {'required': False},
            'follow_up_by': {'required': False},
            'resolved_by': {'required': False},
            'audited_on': {'required': False},
            'reject_reason': {'required': False}
        }
        # ['encrt_id', 'department'= fields.MultipleChoiceField(choices=DEPARTMENT_CHOICES),'status', 'region','subregion','encrt_size','dist_coa','criticality']
        
    def validate(self, data):
        data_dict = dict(data)
        data_keys = data.keys()
        status_type= data_dict.get('status')
        
        if status_type == 'assigned' and 'assigned_to' not in data_keys:
            raise serializers.ValidationError('assigned_to required when status_type is assigned.')
        elif status_type == 'assigned':
            val=data_dict.get('assigned_to')
            if val is None or val==[]:
                raise serializers.ValidationError('Must be assigned_to atleast one department')
        if status_type == 'follow_up' and 'follow_up_by' not in data_keys:
            raise serializers.ValidationError('follow_up_by required when status_type is follow_up.')
        elif status_type == 'follow_up':
            val=data_dict.get('follow_up_by')
            if val is None:
                raise serializers.ValidationError('Follow_up percentage must be specified')
        if status_type == 'resolved' and 'resolved_by' not in data_keys:
            raise serializers.ValidationError('resolved_by required when status_type is resolved.')
        elif status_type == 'resolved':
            val=data_dict.get('resolved_by')
            if val is None or val==[]:
                raise serializers.ValidationError('Must be resolved_by atleast one department')
        if status_type == 'audited' and 'audited_on' not in data_keys:
            raise serializers.ValidationError('audited_on required when status_type is audited.')
        if status_type == 'rejected' and 'reject_reason' not in data_keys:
            raise serializers.ValidationError('reject_reason required when status_type is rejected.')
        elif status_type == 'rejected':
            val=data_dict.get('reject_reason')
            if val is None:
                raise serializers.ValidationError('There must be a reason to reject')
            # if val is None or val==[]:
            #     raise serializers.ValidationError('This field can'')
        # if status_type == 'COMPANY' and 'company_name' not in data_keys:
        #     raise serializers.ValidationError('company_name required when account_type is COMPANY.')
        return data

    # def validate_assigned_to(self,value):
    #     if value is None:
    #         raise serializers.ValidationError('Must be assigned_to atleast one department')
    #     return value
        # if len(value) < 1:
        #     raise serializers.ValidationError('Must be assigned_to atleast one department')
        # return value