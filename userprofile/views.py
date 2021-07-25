from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class Users(APIView):


    def post(self,request):
        '''
           API to add the user
        '''

        payload = request.data
        user_seri = UserSerializer(data=payload,partial=True)
        if user_seri.is_valid():
            userobj = user_seri.save()
            userobj.set_password(payload["password"])
            userobj.save()
            return Response('your have registered succesfully!!!',status=201)
        return Response(user_seri.errors,status=400)

    def put(self,request):
        '''
           API to edit the user
        '''

        payload = request.data
        user_id = payload['user_id']
        try:
            userobj = get_user_model().objects.get(pk=user_id)
        except Exception as e:
            return Response(e.__str__(),status=404)

        user_seri = UserSerializer(userobj,data=payload,partial=True)
        if user_seri.is_valid():
            userobj = user_seri.save()
            return Response('your data has been updated succesfully!!!',status=200)
        return Response(user_seri.errors,status=400)

    def delete(self,request):
        '''
           API to delete the user
        '''

        payload = request.data
        user_id = payload['user_id']
        try:
            userobj = get_user_model().objects.get(pk=user_id)
        except Exception as e:
            return Response(e.__str__(),status=404)
        userobj.delete()
        return Response('your data has been deleted succesfully!!!',status=200)


class UserList(APIView):
    def get(self,request):
        '''
        API to get all the user
        '''
        payload = request.query_params
        page_size = payload.get('page_size',10)
        page = payload.get('page',1)
        users = get_user_model().objects.all()
        paginator = Paginator(users,page_size)
        try:
            user_data = paginator.page(page)
        except PageNotAnInteger:
            user_data = paginator.page(1)
        except EmptyPage:
            user_data = paginator.page(paginator.num_pages)
        meta_data = {"total_pages": paginator.num_pages,
                     "current_page ":user_data.number
                     }
        user_seri = UserSerializer(user_data,many=True)
        return Response({'metaData':meta_data,
                         'userList':user_seri.data},status=200)


