from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets,status

from django.core import serializers
from .serializers import UserSerializer,UserLoginSerializer,UserDetailsSerializer,TokenSerializer,UserLogoutSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.auth import logout
import json
from django.utils.translation import ugettext_lazy as _
from rest_framework.decorators import api_view, permission_classes
from .models import role_table,rounds_table,canditates
from rest_framework.permissions import IsAuthenticated

class UserLoginAPIView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserLoginSerializer
    serializer_class1 = UserDetailsSerializer
    serializer_class2= UserSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = Token.objects.get_or_create(user=user)
            try:
                user_details = User.objects.get(username=user)
                if user_details.email=="" or user_details.email==None:
                    user_details.email = user_details.username
                    user_details.save()
                print(user_details.email)
                print(user_details.username)

                return Response(
                    data={"username":user_details.username,
                          "Token": TokenSerializer(token).data},
                    status=status.HTTP_200_OK,
                )
            except:
                return Response(
                    data={
                    # "username":user,
                    "Token": TokenSerializer(token).data},
                    status=status.HTTP_200_OK,
                )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

class UserLogoutAPIView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self, request, *args, **kwargs):
        try:
            Token.objects.get(key=request.data['token']).delete()
            logout(request)
            return Response({"msg": "User Logged Out Successfully"})
        except:
            return Response({"msg" : "User Logged Out Successfully"})
    def get(self, request, *args, **kwargs ):
        try:
            logout(request)
        except:
            pass
        return Response({"msg": "User Logged Out Successfully"})


class UserVerifyLoginAPIView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self, request, *args, **kwargs):
        try:
            token = Token.objects.get(key=request.data['token'])
            return Response({"message":"User is active"})
        except:
            return Response({"message": "No user found"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RoleInfo(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self,request, *args, **kwargs):
        data = request.data
        try:
                role_info = role_table.objects.get(role_id=data['role_id'])
                domain_name = role_info.role_name
                no_of_rounds = role_info.rounds
                details = role_info.round_details.split(",")
                return Response(data = {"role_id":data['role_id'],"role_name": domain_name, "no_of_rounds": no_of_rounds, "Rounds_names": details},status=status.HTTP_200_OK,)
        except:
                return Response({"Message": "Invalid role details"})

    def get(self,request):
        role_info= role_table.objects.all()
        user_info=role_info.values()
        for i in range(0, len(user_info)):
            user_info[i]['round_details'] = user_info[i]['round_details'].split(",")
        print(user_info)
        return Response(user_info,status=status.HTTP_200_OK)



class RoleEdit(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    def post(self,request, *args, **kwargs):
        data = request.data

        try:
            role_id = data['role_id']
            change_role = role_table.objects.get(role_id=role_id)
            try:
                change_role.role_name = data['role_name']
                change_role.rounds = len(data['rounds'])
                change_role.round_details = ",".join(data['rounds'])
                change_role.save()
                return Response({"message" : "Data Updated"})
            except:
                return Response({"message" : "Error while changing the data, Not valid input request"})

        except:
            try:
                change_role = role_table()
                change_role.role_name = data['role_name']
                change_role.rounds = len(data['rounds'])
                change_role.round_details = ",".join(data['rounds'])
                change_role.save()
                return Response({"message" : "Data Inserted"})
            except:
                return Response({"message" : "Error while inserting the data, Not valid input request"})

