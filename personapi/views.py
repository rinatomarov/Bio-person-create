from .models import Person
from .serializers import DataSerizalizer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import age_calc


class CalculateInn(APIView):
    def post(self, request):
        serializer = DataSerizalizer(data=request.data)
        if serializer.is_valid():
            iin = serializer.data.get('iin')
            if len(iin) < 12:
                return Response({
                    'error': 'Invalid input',
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    result = age_calc.calculate_age(iin)
                    Person.objects.create(iin=iin, age=result)
                    return Response({
                        'Description': 'Successful operation',
                        'iin': iin,
                        'age': result
                    }, status=status.HTTP_201_CREATED)
                except:
                    return Response({
                        'Description': 'Person exists'
                    }, status=status.HTTP_403_FORBIDDEN)

    def get(self, request, iin):
        if len(iin) < 12:
            return Response({
                'Error': 'Invalid input'
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                result = Person.objects.get(iin=iin)
                return Response({
                    'Description': 'Successful operation',
                    'iin': result.iin,
                    'age': result.age
                }, status=status.HTTP_200_OK)
            except:
                return Response({
                    'Description': 'Person not found'
                }, status=status.HTTP_404_NOT_FOUND)