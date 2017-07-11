from rest_framework import status, generics

from .models import users, orders, menus, locations, wallets
from .serializers import UserSerializer, OrderSerializer, MenuSerializer, LocationSerializer, WalletSerializer, Menu_User_Srlz
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from corsheaders.defaults import default_methods
from django.core import serializers
from django.db import connection
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

import json



def home(request):
    menu = menus.objects.all()
    user = users.objects.all()
    qs 	 = menus.objects.select_related().order_by("-menu_id")#.filter(menu_id=2)
    context = {'data': menu, 'user': user, 'qs': qs}
    print qs.query
    return render(request, 'index.html', {"context": context})

def supplier_page(request):
    return render(request, 'main_app/supplier.html')

def customer_page(request):
    return render(request, 'main_app/customer.html')

def delivery_page(request):
    return render(request, 'main_app/delivery.html')

def weui_page(request):
    return render(request, 'main_app/weui.html')




class UserList(APIView):
	def get(self, request, format=None):
		queryset = users.objects.all()
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
	def get_object(self, user_id):
		try:
			return users.objects.get(user_id=user_id)
		except users.DoesNotExist:
			raise Http404

	def get(self, request, user_id, format=None):
		profile = self.get_object(user_id)
		serializer = UserSerializer(profile)
		return Response(serializer.data)

	def put(self, request, user_id, format=None):
		profile = self.get_object(user_id)
		serializer = UserSerializer(profile, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, user_id, format=None):
		CORS_ALLOW_METHODS = default_methods
		profile = self.get_object(user_id)
		profile.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)











class MenuList(APIView):
	def get(self, request, format=None):
		queryset = menus.objects.all()
		serializer = MenuSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = MenuSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetail(APIView):
	def get_object(self, menu_id):
		try:
			return menus.objects.get(menu_id=menu_id)
		except menus.DoesNotExist:
			raise Http404

	def get(self, request, menu_id, format=None):
		object = self.get_object(menu_id)
		serializer = MenuSerializer(object)
		return Response(serializer.data)

	def put(self, request, menu_id, format=None):
		object = self.get_object(menu_id)
		serializer = MenuSerializer(object, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, menu_id, format=None):
		CORS_ALLOW_METHODS = default_methods
		object = self.get_object(menu_id)
		object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)









class WalletList(APIView):
	def get(self, request, format=None):
		queryset = wallets.objects.all()
		serializer = WalletSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = WalletSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WalletDetail(APIView):
	def get_object(self, trans_id):
		try:
			return wallets.objects.get(trans_id=trans_id)
		except wallets.DoesNotExist:
			raise Http404

	def get(self, request, trans_id, format=None):
		object = self.get_object(trans_id)
		serializer = WalletSerializer(object)
		return Response(serializer.data)

	def put(self, request, trans_id, format=None):
		object = self.get_object(trans_id)
		serializer = WalletSerializer(object, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, trans_id, format=None):
		CORS_ALLOW_METHODS = default_methods
		object = self.get_object(trans_id)
		object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)









class OrderList(APIView):
	def get(self, request, format=None):
		queryset = orders.objects.all()
		serializer = OrderSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = OrderSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
	def get_object(self, order_id):
		try:
			return orders.objects.get(order_id=order_id)
		except orders.DoesNotExist:
			raise Http404

	def get(self, request, order_id, format=None):
		object = self.get_object(order_id)
		serializer = OrderSerializer(object)
		return Response(serializer.data)

	def put(self, request, order_id, format=None):
		object = self.get_object(order_id)
		serializer = OrderSerializer(object, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, order_id, format=None):
		CORS_ALLOW_METHODS = default_methods
		object = self.get_object(order_id)
		object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)



 


class LocationList(APIView):
	def get(self, request, format=None):
		queryset = locations.objects.all().order_by('location_id')
		serializer = LocationSerializer(queryset, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = LocationSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationDetail(APIView):
	def get_object(self, location_id):
		try:
			return locations.objects.get(location_id=location_id)
		except locations.DoesNotExist:
			raise Http404

	def get(self, request, location_id, format=None):
		object = self.get_object(location_id)
		serializer = LocationSerializer(object)
		return Response(serializer.data)

	def put(self, request, location_id, format=None):
		object = self.get_object(location_id)
		serializer = LocationSerializer(object, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, location_id, format=None):
		CORS_ALLOW_METHODS = default_methods
		object = self.get_object(location_id)
		object.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)







class TestJoin(APIView):
	def get(self, request, format=None):


		#query join user to  menu
		qset 	 = menus.objects.select_related()
		qs 		 = menus.objects.select_related().order_by("-menu_id").filter(menu_id=2)

		#query join user to order table
		quo = orders.objects.select_related()

		#query join user to location
		qul = locations.objects.select_related()

		# query join user to wallet
		quw = wallets.objects.select_related()

		# usr = users.objects.all().filter(user_id=True).order_by("-user_id")
		# mn  = menus.objects.filter(owner_id__in=usr)
		# data = menus.objects.filter(owner_id=usr)
		# print "\n\n"
		# print mn.query

		# print "\n\n"
		# print qs.query
		# print "\n\n"
		# print json.dumps(qset)

		data = serializers.serialize('json', list(quw))

		# print menus.objects.select_related().query

		
		# serializer = Menu_User_Srlz()#qs, many=True serializer = serializers.UserSerializer(data=self.get_initial_data())


		# serializer.is_valid(raise_exception=True)
		return Response(data)
		# return HttpResponse(qset, content_type='application/json')#Response(serializer.data)




def _TestJoin(self):
	query = 'SELECT * FROM customer_menus'
	sql_raw = menus.objects.raw(query)
	return HttpResponse(sql_raw, content_type='application/json')





	# https: // stackoverflow.com / questions / 7794816 / django - python - raw - sql -
	# with-multiple - tables

	# http: // www.django - rest - framework.org / api - guide / serializers /  # dealing-with-nested-objects
	# https: // stackoverflow.com / questions / 44978045 / serialize - multiple - models - and -send - all - in -one - json - response - django - rest - framewor
	# http: // www.django - rest - framework.org / api - guide / relations /  # writable-nested-serializers
	# https: // stackoverflow.com / questions / 35466300 / django - rest - framework - writable - nested - serializer -
	# with-multiple - nested - objects
	# https: // github.com / beda - software / drf - writable - nested
	# https: // github.com / AltSchool / dynamic - rest / tree / master / dynamic_rest
# http://flaviusim.com/blog/AJAX-Autocomplete-Search-with-Django-and-jQuery/




# filtering
# Entry.objects.all().filter(pub_date__year=2006)  Entry.objects.filter(pub_date__lte='2006-01-01')
# Entry.objects.get(pk=1)
# Entry.objects.all()[5:10] limitation Entry.objects.all()[:5]
# Blog.objects.filter(entry__authors__name='Lennon')
# Blog.objects.filter(entry__headline__contains='Lennon').filter(entry__pub_date__year=2008)




# https://github.com/beda-software/drf-writable-nested





	# roject = Project.objects.get(
	# 	id=request.POST.get("project_id"))
	# entries = request.POST.getlist("entry")
	# team = Team.objects.get(
	# 	id=request.POST.get("team_id"))




	# Members.objects.values('designation').annotate(dcount=Count('designation'))
	# ELECT
	# designation, COUNT(designation)
	# AS
	# dcount
	# FROM
	# members
	# GROUP
	# BY
	# designation






# def save(self):
#     data = self.cleaned_data
#     user = User(email=data['email'], first_name=data['first_name'],
#         last_name=data['last_name'], password1=data['password1'],
#         password2=data['password2'])
#     user.save()
#     userProfile = UserProfile(user=user,gender=data['genger'],
#         year=data['year'], location=data['location'])
#     userProfile.save()

# https://stackoverflow.com/questions/18382796/django-form-save-method/