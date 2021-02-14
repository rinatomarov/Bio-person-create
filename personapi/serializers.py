from rest_framework import serializers

class DataSerizalizer(serializers.Serializer):
    iin = serializers.CharField(max_length=12)
