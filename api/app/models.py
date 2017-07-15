from django.shortcuts import render
from django.db import connection
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
import json, glob, datetime
from rest_framework.response import Response




def get_order_on_hand(request):
	connection.row_factory =  dict_factory
	cursor = connection.cursor()
	sql = "select order_id,menu_id from customer_orders  where store_id_id=? and order_status='paid'"
	cursor.execute(sql, [request.POST.get('store_id')])
	keys=('order_id','menu_id')	
	orders = list(cursor.fetchall())
	json_merge = []
	# print type(orders)
	for order in orders:
		menu_list = (order[1].split(","))
		menu_idx =0	
		order_id = order[0]

		for menu_id in menu_list:
			# print menu_id
			sql2 = '''
					select 
						a.menu_id,
						a.menu_name,
						a.menu_detail,
						a.menu_img,
						a.menu_status,
						a.price,
						b.order_id,
						b.store_id_id as store_id,
						b.customer_id_id as customer_id,
						b.order_status,
						strftime('%Y/%m/%d', b.time_stamp) as date_order,
						b.order_size
					from customer_orders b  inner join customer_menus a on a.owner_id  = b.store_id_id
					where b.store_id_id = ? and  a.menu_id =? and order_status='paid' and order_id = ? and a.menu_status='active'
			'''
			# print sql2
			cursor.execute(sql2, [request.POST.get('store_id'), menu_id, order_id])
			keys= ('menu_id', 'menu_name', 'menu_detail', 'menu_img', 'menu_status', 'price','order_id', 'store_id', 'customer_id', 'order_status', 'date_order', 'order_size')
			row = dictfetchall(cursor, keys)
			# print row
			if(len(row) > 2):
				json_merge.append(row)
				menu_idx+1
	return HttpResponse(json.dumps(json_merge))








def get_supplier_on_hand(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
				ORD.ORDER_ID,
				MN.OWNER_ID,
			    MN.MENU_ID,
			    MN.MENU_NAME,
			    MN.MENU_DETAIL,
				MN.MENU_SIZE,
			    MN.MENU_IMG,
			    MN.MENU_STATUS,
			    MN.PRICE
			FROM FD_MENUS MN INNER JOIN FD_ORDERS ORD ON (MN.MENU_ID = ORD.MENU_ID AND MN.OWNER_ID = ORD.STORE_ID)
			WHERE MN.OWNER_ID = ? AND MN.MENU_STATUS=1 AND ORD.ORDER_STATUS='paid' 
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('OWNER_ID')]) 
	keys = ('ORDER_ID', 'OWNER_ID', 'MENU_ID','MENU_NAME', 'MENU_DETAIL', 'MENU_SIZE', 'MENU_IMG','MENU_STATUS', 'PRICE')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")
	





def get_supplier_on_hand_detail(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
				ORD.ORDER_ID,
				MN.OWNER_ID,
			    MN.MENU_ID,
			    MN.MENU_NAME,
			    MN.MENU_DETAIL,
				MN.MENU_SIZE,
			    MN.MENU_IMG,
			    MN.MENU_STATUS,
			    MN.PRICE,
			    ORD.AMOUNT,
			    ORD.TIME_STAMP
			FROM FD_MENUS MN INNER JOIN FD_ORDERS ORD ON (MN.MENU_ID = ORD.MENU_ID AND MN.OWNER_ID = ORD.STORE_ID)
			WHERE MN.OWNER_ID = ? AND ORD.ORDER_ID=? AND MN.MENU_STATUS=1 AND ORD.ORDER_STATUS='paid'
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('OWNER_ID'), request.POST.get('ORDER_ID')])  
	keys = ('ORDER_ID', 'OWNER_ID', 'MENU_ID','MENU_NAME', 'MENU_DETAIL', 'MENU_SIZE', 'MENU_IMG','MENU_STATUS', 'PRICE','AMOUNT', 'TIME_STAMP')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")
	






def get_supplier_order_history(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
				ORD.ORDER_ID,
				MN.OWNER_ID,
			    MN.MENU_ID,
			    MN.MENU_NAME,
			    MN.MENU_DETAIL,
				MN.MENU_SIZE,
			    MN.MENU_IMG,
			    MN.MENU_STATUS,
			    MN.PRICE,
			    ORD.AMOUNT
			FROM FD_MENUS MN INNER JOIN FD_ORDERS ORD ON (MN.MENU_ID = ORD.MENU_ID AND MN.OWNER_ID = ORD.STORE_ID)
			WHERE MN.OWNER_ID = ? AND MN.MENU_STATUS=1 AND (ORD.ORDER_STATUS='picked' OR ORD.ORDER_STATUS='delivered') 
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('OWNER_ID')]) 
	keys = ('ORDER_ID', 'OWNER_ID', 'MENU_ID','MENU_NAME', 'MENU_DETAIL', 'MENU_SIZE', 'MENU_IMG','MENU_STATUS', 'PRICE', 'AMOUNT')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")
	





def get_supplier_order_history_detail(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
				ORD.ORDER_ID,
				MN.OWNER_ID,
			    MN.MENU_ID,
			    MN.MENU_NAME,
			    MN.MENU_DETAIL,
				MN.MENU_SIZE,
			    MN.MENU_IMG,
			    MN.MENU_STATUS,
			    MN.PRICE,
			    ORD.AMOUNT,
			    ORD.TIME_STAMP
			FROM FD_MENUS MN INNER JOIN FD_ORDERS ORD ON (MN.MENU_ID = ORD.MENU_ID AND MN.OWNER_ID = ORD.STORE_ID)
			WHERE MN.OWNER_ID = ? AND ORD.ORDER_ID=? AND MN.MENU_STATUS=1 AND (ORD.ORDER_STATUS='picked' OR ORD.ORDER_STATUS='delivered')
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('OWNER_ID'), request.POST.get('ORDER_ID')])  
	keys = ('ORDER_ID', 'OWNER_ID', 'MENU_ID','MENU_NAME', 'MENU_DETAIL', 'MENU_SIZE', 'MENU_IMG','MENU_STATUS', 'PRICE', 'AMOUNT', 'TIME_STAMP')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")






def get_supplier_menu_list(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
			    MENU_ID,
			    MENU_NAME,
			    MENU_DETAIL,
			    MENU_IMG,
			    MENU_STATUS,
				group_concat(
			            MENU_SIZE ||'|'|| PRICE
			        ,',') AS PARCEL_DESC
		    FROM FD_MENUS
			WHERE OWNER_ID = ?
			ORDER BY MENU_ID
	'''
	cursor.execute(sql, [request.POST.get('OWNER_ID')])  
	keys = ('MENU_ID', 'MENU_NAME', 'MENU_DETAIL', 'MENU_IMG', 'MENU_STATUS', 'PARCEL_DESC')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")
		





def confirm_supplier_on_hand(request):
	cursor = connection.cursor()

	sql1 = "update FD_ORDERS set ORDER_STATUS='picked', TIME_STAMP=? WHERE ORDER_ID=?"
	cursor.execute(sql1, [datetime.date.today(), request.POST.get('ORDER_ID')])
	
	keys = ('ORDER_ID')
	
	return HttpResponse(request.POST.get('ORDER_ID'), content_type="application/json")



def update_menu_supplier(request):
	cursor = connection.cursor()

	sql1 = "update FD_MENUS set PRICE=?, MENU_STATUS=? WHERE MENU_ID=? AND MENU_SIZE=?"
	cursor.execute(sql1, [request.POST.get('val'), request.POST.get('status'), request.POST.get('menu_id'), request.POST.get('type')])

	return HttpResponse(request.POST.get('menu_id'), content_type="application/json")

















'''
def get_supplier_order_history(request):
	connection.row_factory =  dict_factory
	cursor = connection.cursor()
	sql = "select order_id,menu_id from customer_orders  where store_id_id=? and (order_status='picked' or order_status='delivered')"
	cursor.execute(sql, [request.POST.get('store_id')])
	keys=('order_id','menu_id')	
	orders = list(cursor.fetchall())
	json_merge = []
	print type(orders)
	for order in orders:
		menu_list = (order[1].split(","))
		menu_idx =0	
		order_id = order[0]

		for menu_id in menu_list:
			# print menu_id
			sql2 = ''
					select 
						a.menu_id,
						a.menu_name,
						a.menu_detail,
						a.menu_img,
						a.menu_status,
						a.price,
						b.order_id,
						b.store_id_id as store_id,
						b.customer_id_id as customer_id,
						b.order_status,
						strftime('%Y/%m/%d', b.time_stamp) as date_order,
						b.order_size
					from customer_orders b  inner join customer_menus a on  (a.owner_id  = b.store_id_id)
					where b.store_id_id = ? and (b.order_status='picked' or b.order_status='delivered') and order_id = ? and a.menu_status='active' --and a.menu_id =?
			''
			# print sql2
			cursor.execute(sql2, [request.POST.get('store_id'), order_id])
			keys= ('menu_id', 'menu_name', 'menu_detail', 'menu_img', 'menu_status', 'price','order_id', 'store_id', 'customer_id', 'order_status', 'date_order', 'order_size')
			row = dictfetchall(cursor, keys)
			print row
			if(len(row) > 2):	
				json_merge.append(row)
				menu_idx+1
			# print json.dumps(json_merge)
	return HttpResponse(json.dumps(json_merge))
'''





def delivery_collect_money(request):
	cursor = connection.cursor()

	sql1 = '''
		SELECT 
		    ORD.ORDER_ID,
			ORD.CUSTOMER_ID,
			ORD.STORE_ID,
			ORD.DELIVERY_ID,
		    SUM(coalesce(ORD.AMOUNT,0) * coalesce(MENU.PRICE,0)) AS TOTAL_PRICE   
		FROM FD_ORDERS ORD
		LEFT JOIN FD_MENUS MENU ON (ORD.MENU_ID = MENU.MENU_ID AND ORD.ORDER_SIZE = MENU.MENU_SIZE)
		where ORD.ORDER_ID = ?
		GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql1, [request.POST.get('order_id')])
	dta = list(cursor.fetchall())
	keys = ('ORDER_ID')
	for dt in dta:
		get_wallet(dt[0], dt[1], dt[2], dt[3], dt[4], "income")

	# keys = ('ORDER_ID')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")




def get_wallet(order_id, cus_id, store_id, del_id, amount, type):
	timeStamp=str(datetime.datetime.now())
	cursor= connection.cursor()
	cursor.execute('''INSERT INTO FD_WALLETS (USER_ID, OUTCOME, TIME_STAMP) VALUES (%s, %s, %s)''',(cus_id, amount, timeStamp))
	cursor.execute('''INSERT INTO FD_WALLETS (USER_ID, INCOME, TIME_STAMP) VALUES (%s, %s, %s)''',(store_id, (amount-5)*0.9, timeStamp))
	cursor.execute('''INSERT INTO FD_WALLETS (USER_ID, INCOME, TIME_STAMP) VALUES (%s, %s, %s)''',(del_id, 5, timeStamp))
	cursor.execute('''INSERT INTO FD_WALLETS (USER_ID, INCOME, TIME_STAMP) VALUES (%s, %s, %s)''',(99, (amount-5)*0.1, timeStamp))

	sql = "update FD_ORDERS set DELIVERY_STATUS='delivered', TIME_STAMP=? where ORDER_ID=?"
	cursor.execute(sql, [datetime.date.today(), order_id])








def order_on_hand_confirm(request):
	cursor = connection.cursor()

	sql1 = "update customer_orders set order_status='ready' where order_id=?"
	cursor.execute(sql1, [request.POST.get('order_id')])
	
	keys = ('order_id')
	
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")






def test_new_user(request):
	cursor = connection.cursor()
	cursor.execute(
	    	'''select * from users'''
	)
	keys = ('user_id','type','phone_no')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")




def test_get(request):
	cursor = connection.cursor()
	cursor.execute(
	    	'''select
				a.menu_id,
				a.menu_name,
				a.menu_detail,
				a.menu_img,
				a.menu_status,
				a.owner_id,
				b.type,
				b.mobile_no
			from customer_menus a inner join customer_users b on (a.owner_id = b.user_id)
			order by a.menu_id desc'''
	)
	keys = ('menu_id','menu_name','menu_detail','menu_img','menu_status','owner_id','type','mobile_no')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")






def get_delivery_task_finder(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
			        ORD.ORDER_ID,
			        ORD.ORDER_STATUS,
			        ORD.TIME_STAMP,
			        LOC_CUS.NAME AS CUSTOMER_LOCATION,
			        LOC_CUS.LAT AS CUSTOMER_LAT,
			        LOC_CUS.LONG AS CUSTOMER_LONG,
			        LOC_STORE.NAME AS STORE_LOCATION,
			        LOC_STORE.LAT AS STORE_LAT,
			        LOC_STORE.LONG AS STORE_LONG,
			        group_concat(
			            ORD.ORDER_SIZE ||': '|| ORD.AMOUNT
			        ,',') AS PARCEL_DESC
			FROM 
			FD_ORDERS ORD LEFT JOIN FD_LOCATIONS LOC_CUS ON ORD.CUSTOMER_ID = LOC_CUS.USER_ID
			LEFT JOIN FD_LOCATIONS LOC_STORE ON ORD.STORE_LOCATION_ID = LOC_STORE.ID
			WHERE ORD.DELIVERY_STATUS = 'waiting' AND ORD.DELIVERY_ID = ?
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('order_id')]) 
	keys = ('ORDER_ID','ORDER_STATUS','TIME_STAMP', 'CUSTOMER_LOCATION', 'CUSTOMER_LAT', 'CUSTOMER_LONG','STORE_LOCATION', 'STORE_LAT', 'STORE_LONG', 'PARCEL_DESC')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")








def update_delivery_task_finder(request):
	cursor = connection.cursor()
	sql = "update FD_ORDERS set DELIVERY_STATUS='reserved', TIME_STAMP=? where ORDER_ID=?"
	cursor.execute(sql, [datetime.date.today(), request.POST.get('order_id')])
	keys = ('ORDER_ID')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")















def get_customer_order_history(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
				ORD.ORDER_ID,
			    MN.MENU_ID,
			    MN.MENU_NAME,
			    MN.MENU_DETAIL,
				MN.MENU_SIZE,
			    MN.MENU_IMG,
			    MN.MENU_STATUS,
			    MN.PRICE,
			    ORD.AMOUNT,
			    ORD.TIME_STAMP
			FROM FD_MENUS MN INNER JOIN FD_ORDERS ORD ON (MN.MENU_ID = ORD.MENU_ID AND MN.OWNER_ID = ORD.STORE_ID)
			WHERE ORD.CUSTOMER_ID =? AND MN.MENU_STATUS=1 AND (ORD.ORDER_STATUS='picked' OR ORD.ORDER_STATUS='delivered') 
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('customer_id')]) 
	keys = ('ORDER_ID',  'MENU_ID','MENU_NAME', 'MENU_DETAIL', 'MENU_SIZE', 'MENU_IMG','MENU_STATUS', 'PRICE', 'AMOUNT', 'TIME_STAMP')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")



def get_customer_order_history_detail(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
				ORD.ORDER_ID,
			    MN.MENU_ID,
			    MN.MENU_NAME,
			    MN.MENU_DETAIL,
				MN.MENU_SIZE,
			    MN.MENU_IMG,
			    MN.MENU_STATUS,
			    MN.PRICE,
			    ORD.AMOUNT,
			    ORD.TIME_STAMP
			FROM FD_MENUS MN INNER JOIN FD_ORDERS ORD ON (MN.MENU_ID = ORD.MENU_ID AND MN.OWNER_ID = ORD.STORE_ID)
			WHERE ORD.CUSTOMER_ID =? AND ORD.ORDER_ID=? AND MN.MENU_STATUS=1 AND (ORD.ORDER_STATUS='picked' OR ORD.ORDER_STATUS='delivered') 
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('customer_id'), request.POST.get('order_id')]) 
	keys = ('ORDER_ID',  'MENU_ID','MENU_NAME', 'MENU_DETAIL', 'MENU_SIZE', 'MENU_IMG','MENU_STATUS', 'PRICE', 'AMOUNT', 'TIME_STAMP')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")










def get_delivery_task_on_hand(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
			        ORD.ORDER_ID,
			        ORD.ORDER_STATUS,
			        ORD.TIME_STAMP,
			        LOC_CUS.NAME AS CUSTOMER_LOCATION,
			        LOC_CUS.LAT AS CUSTOMER_LAT,
			        LOC_CUS.LONG AS CUSTOMER_LONG,
			        LOC_STORE.NAME AS STORE_LOCATION,
			        LOC_STORE.LAT AS STORE_LAT,
			        LOC_STORE.LONG AS STORE_LONG,
			        group_concat(
			            ORD.ORDER_SIZE ||': '|| ORD.AMOUNT
			        ,',') AS PARCEL_DESC
			FROM 
			FD_ORDERS ORD LEFT JOIN FD_LOCATIONS LOC_CUS ON ORD.CUSTOMER_ID = LOC_CUS.USER_ID
			LEFT JOIN FD_LOCATIONS LOC_STORE ON ORD.STORE_LOCATION_ID = LOC_STORE.ID
			WHERE ORD.DELIVERY_STATUS = 'reserved' AND ORD.DELIVERY_ID = ?
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('order_id')]) 
	keys = ('ORDER_ID','ORDER_STATUS','TIME_STAMP', 'CUSTOMER_LOCATION', 'CUSTOMER_LAT', 'CUSTOMER_LONG','STORE_LOCATION', 'STORE_LAT', 'STORE_LONG', 'PARCEL_DESC')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")	









def get_customer_order_status(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
			        ORD.ORDER_ID,
			        ORD.ORDER_STATUS,
			        ORD.TIME_STAMP,
			        LOC_CUS.NAME AS CUSTOMER_LOCATION,
					MN.MENU_NAME,
					MN.MENU_IMG,
			        group_concat(
			            ORD.ORDER_SIZE ||': '|| ORD.AMOUNT
			        ,',') AS PARCEL_DESC,
					SUM(coalesce(ORD.AMOUNT,0) * coalesce(MN.PRICE,0)) AS TOTAL_PRICE   
			FROM 
			FD_ORDERS ORD LEFT JOIN FD_LOCATIONS LOC_CUS ON ORD.CUSTOMER_ID = LOC_CUS.USER_ID
			LEFT JOIN FD_LOCATIONS LOC_STORE ON ORD.STORE_LOCATION_ID = LOC_STORE.ID
			LEFT JOIN FD_MENUS MN ON MN.MENU_ID = ORD.MENU_ID
			WHERE ORD.CUSTOMER_ID = ?
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('customer_id')]) 
	keys = ('ORDER_ID','ORDER_STATUS','TIME_STAMP', 'CUSTOMER_LOCATION', 'MENU_NAME','MENU_IMG', 'PARCEL_DESC', 'TOTAL_PRICE')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")	







def get_delivery_task_history(request):
	cursor = connection.cursor()
	sql = '''
			SELECT 
			        ORD.ORDER_ID,
			        ORD.MENU_ID,
					MN.MENU_NAME,
					MN.MENU_DETAIL,
			        ORD.ORDER_STATUS,
			        ORD.TIME_STAMP,
			        LOC_CUS.NAME AS CUSTOMER_LOCATION,
			        LOC_CUS.LAT AS CUSTOMER_LAT,
			        LOC_CUS.LONG AS CUSTOMER_LONG,
			        LOC_STORE.NAME AS STORE_LOCATION,
			        LOC_STORE.LAT AS STORE_LAT,
			        LOC_STORE.LONG AS STORE_LONG
			FROM 
			FD_ORDERS ORD JOIN FD_LOCATIONS LOC_CUS ON ORD.CUSTOMER_ID = LOC_CUS.USER_ID
			JOIN FD_LOCATIONS LOC_STORE ON ORD.STORE_ID = LOC_STORE.USER_ID
			INNER JOIN FD_MENUS MN ON MN.MENU_ID = ORD.MENU_ID
			WHERE ORD.DELIVERY_STATUS = 'delivered' AND ORD.DELIVERY_ID = ?
			GROUP BY ORD.ORDER_ID
	'''
	cursor.execute(sql, [request.POST.get('order_id')]) 
	keys = ('ORDER_ID','MENU_ID', 'MENU_NAME', 'MENU_DETAIL', 'ORDER_STATUS', 'TIME_STAMP','CUSTOMER_LOCATION', 'CUSTOMER_LAT', 'CUSTOMER_LONG','STORE_LOCATION' , 'STORE_LAT', 'STORE_LONG')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")



# http://www.bogotobogo.com/python/python_sqlite_select_update_delete.php
def test_post(request):
	cursor = connection.cursor()

	# with connection.cursor() as cursor:
		
	sql1 = "update customer_users set type=?, mobile_no=? where user_id=?"
	cursor.execute(sql1, [request.POST.get('type'), request.POST.get('mobile_no'), request.POST.get('user_id')])
	

	# sql = "delete from customer_users WHERE user_id =?"
	# cursor.execute(sql, [request.POST.get('user_id')])

	sql2 = "select * from customer_users"# WHERE user_id =?"
	cursor.execute(sql2)#, [request.POST.get('user_id')])
	# "select * from customer_users WHERE type like "%'%s'%" and mobile_no = %s"
	
	keys = ('user_id','mobile_no','type')
	return HttpResponse(dictfetchall(cursor, keys), content_type="application/json")








# DONT DELETE IT!   # DONT DELETE IT!    # DONT DELETE IT!
def dictfetchall(cursor, keys):
	data = cursor.fetchall()
	result = []
	for row in data:
	    result.append(dict(zip(keys,row)))
	return json.dumps(result)
# DONT DELETE IT!   # DONT DELETE IT!    # DONT DELETE IT!


def dict_factory(cursor, row):
	d={}
	for idx, col in enumerate(cursor.description):
		d[col[0]] =row[idx]
	return d

























# cursor = connections['my_db_alias'].cursor()

# with connection.cursor() as cursor:
#         cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
#         cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
#         row = cursor.fetchone()

#     return row



# >>> cursor.execute("SELECT id, parent_id FROM test LIMIT 2");
# >>> cursor.fetchall()
# ((54360982, None), (54360880, None))

# >>> cursor.execute("SELECT id, parent_id FROM test LIMIT 2");
# >>> dictfetchall(cursor)
# [{'parent_id': None, 'id': 54360982}, {'parent_id': None, 'id': 54360880}]

# >>> cursor.execute("SELECT id, parent_id FROM test LIMIT 2");
# >>> results = namedtuplefetchall(cursor)
# >>> results
# [Result(id=54360982, parent_id=None), Result(id=54360880, parent_id=None)]
# >>> results[0].id
# 54360982
# >>> results[0][0]
# 54360982