from rest_framework import serializers

from core.models import Category, Transaction, UploadedFile


class UploadedFileSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        if self.partial is True:
            instance.name = validated_data.get('name', instance.name)
            instance.file_type = validated_data.get(
                'file_type', instance.file_type
            )
            instance.save()
            return instance

        if validated_data.get('file'):
            raise serializers.ValidationError(
                {'file': 'O arquivo não pode ser atualizado'}
            )
        return super().update(instance, validated_data)

    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'name', 'file_type']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                {'amount': 'O valor deve ser positivo'}
            )
        return value

    class Meta:
        model = Transaction
        exclude = ['source_file']
