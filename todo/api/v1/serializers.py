from rest_framework import serializers
from todo.models import Task

class TodoSerializer(serializers.ModelSerializer):
    short_content=serializers.ReadOnlyField(source='get_short_content')
    
    author = serializers.CharField(source="author.username", read_only=True)
    class Meta:
        model = Task
        fields =['id','title', 'author' ,'details' ,'short_content','isCompleted','created_date','updated_date']
        read_only_fields=['author']


    def to_representation(self,instance):
        request=self.context.get('request')
        rep =super().to_representation(instance)
        # print(request.data)
        if request.parser_context.get('kwargs').get('pk'):
            rep.pop('short_content',None)
            
        else:
            rep.pop('details',None)
        return rep
