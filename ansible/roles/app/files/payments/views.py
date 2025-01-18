from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import accpList
from .models import accpSaldo
from .serializers import accpListSerializer
from .serializers import accpSaldoSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class GetAccpListInfoView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        p_accp = request.GET.get("accp")
        queryset = accpList.objects.filter(accp=p_accp)
        serializer_for_queryset = accpListSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)


class GetAccpSaldoInfoView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),
            'auth': str(request.auth),
        }
        p_accp = request.GET.get("accp")
        queryset = accpSaldo.objects.filter(accp=p_accp)
        serializer_for_queryset = accpSaldoSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)




