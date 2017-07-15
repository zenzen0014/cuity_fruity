--deliver task finder
select 
        ord.order_id,
        ord.menu_id,
        ord.order_status,
        ord.time_stamp,
        loc_cus.location_name as customer_location,
        loc_cus.lat as customer_lat,
        loc_cus.lng as customer_long,
        loc_store.location_name as store_location,
        loc_store.lat as store_lat,
        loc_store.lng as store_long
from 
customer_orders ord join customer_locations loc_cus on ord.customer_id_id = loc_cus.l_user_id_id
join customer_locations loc_store on ord.store_id_id = loc_store.l_user_id_id
where ord.delivery_status = 'waiting'

--deliver task on hand
select 
        ord.order_id,
        ord.menu_id,
        ord.order_status,
        ord.time_stamp,
        loc_cus.location_name as customer_location,
        loc_cus.lat as customer_lat,
        loc_cus.lng as customer_long,
        loc_store.location_name as store_location,
        loc_store.lat as store_lat,
        loc_store.lng as store_long
from 
customer_orders ord join customer_locations loc_cus on ord.customer_id_id = loc_cus.l_user_id_id
join customer_locations loc_store on ord.store_id_id = loc_store.l_user_id_id
where ord.delivery_id = 1 and ord.delivery_status = 'reserved'

--deliver task history
select 
        ord.order_id,
        ord.menu_id,
        ord.order_status,
        ord.time_stamp,
        loc_cus.location_name as customer_location,
        loc_cus.lat as customer_lat,
        loc_cus.lng as customer_long,
        loc_store.location_name as store_location,
        loc_store.lat as store_lat,
        loc_store.lng as store_long
from 
customer_orders ord join customer_locations loc_cus on ord.customer_id_id = loc_cus.l_user_id_id
join customer_locations loc_store on ord.store_id_id = loc_store.l_user_id_id
where ord.delivery_id = 1 and ord.delivery_status = 'reserved' and ord.order_status = 'delivered'

--Supplier Menu management
select 
    menu_id,
    menu_name,
    menu_detail,
    menu_img,
    menu_status,
    price
from customer_menus
where owner_id = 5

--customer shopping
select
    menu_id,
    menu_name,
    menu_detail,
    menu_img,
    menu_status,
    price,
    owner_id
from customer_menus

--customer history
select
    order_id,
    menu_id,
    order_status,
    time_stamp,
    store_id_id as store_id,
    order_size    
from customer_orders
where 
customer_id_id = 1
and
order_status = 'delivered'