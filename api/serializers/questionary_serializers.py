from api.models import Questionary, Question, Option
from rest_framework import serializers

class QuestionaryCreateSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Questionary
        fields = ['name_questionary', 'description', 'Author']
        
class QuestionCreateSerializers(serializers.ModelSerializer):
    questionary_id = serializers.IntegerField()
    class Meta: 
        model = Question
        fields = ['questionary_id','question', 'image_question']

class OptionCreateSerializers(serializers.ModelSerializer):
    question_id = serializers.IntegerField()
    class Meta: 
        model = Option 
        fields = ['question_id','descriptionOp']

class OptionListSerializers(serializers.ModelSerializer):
    question_id = serializers.IntegerField()
    class Meta: 
        model = Option
        fields = ['id_option','question_id', 'descriptionOp']
        read_only_fields = ['id_option']
        
class QuestionListSerializers(serializers.ModelSerializer):
    options = OptionListSerializers(many=True, read_only=True)
    
    class Meta: 
        model = Question
        fields = ['id_question', 'question', 'image_question', 'options']
        read_only_fields = ['id_question']


class QuestionaryListSerializers(serializers.ModelSerializer):
    questions = QuestionListSerializers(many=True, read_only=True)
    class Meta: 
        model = Questionary
        fields = ['id_questionary', 'name_questionary', 'description', 'questions', 'Author']
        read_only_fields = ['id_questionary']