from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Orders
from .forms import OrderForm

# Create your views here.


def order_lists(request):
    # return render(request, 'order/index.html')
    orders = Orders.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})


def order_add_form(request):
    return JsonResponse({'html_form': render_to_string('order/order_add_form.html', request=request)})



def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()

    context = render_to_string({'form': form})
    return JsonResponse({'context': context})


# def save_order_form(request, form, temp_name):
# 	if request.method == 'POST':
# 		if form.is_valid():
# 			form.save()

# 	context = {'form': form}
# 	html_form = render_to_string(temp_name, context, request=request)
# 	print html_form
# 	# return html_form
#     return JsonResponse({'html_form': html_form})


def order_create_form_ajax(request):
    data = dict()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        status = ''
        if form.is_valid():
            form.save()
            status = 'success'

    else:
        form = OrderForm()
        status = 'failed'
        
    temp_name = 'order/includes/partial_order_create.html'
    context = {'form': form}#, 'is_valid': stat}
    html_form = render_to_string(temp_name, context, request=request)

    order = Orders.objects.all()
    html_book_list = render_to_string(
    			'order/includes/partial_order_list.html', {
                'order': order
    })

    return JsonResponse({'html_form': html_form, 'html_order_list': html_book_list, 'status': status})


def order_update_form_ajax(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=get_object_or_404(Orders, pk=pk))
        status = ''
        if form.is_valid():
            form.save()
            status = 'success'
        	
    else:
        form = OrderForm(instance=get_object_or_404(Orders, pk=pk))
        status = 'failed'
        
    temp_name = 'order/includes/partial_order_update.html'
    context = {'form': form}#, 'is_valid': stat}
    html_form = render_to_string(temp_name, context, request=request)
    
    order = Orders.objects.all()
    html_book_list = render_to_string(
    			'order/includes/partial_order_list.html', {
                'order': order
    })

    return JsonResponse({'html_form': html_form, 'html_order_list': html_book_list, 'status': status})

def order_delete_form_ajax(request, pk):
    order = get_object_or_404(Orders, pk=pk)
    data = dict()
    if request.method == 'POST':
        order.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        order = Orders.objects.all()
        data['html_order_list'] = render_to_string('order/includes/partial_order_list.html', {
            'order': order
        })
    else:
        context = {'order': order}
        data['html_form'] = render_to_string('order/includes/partial_order_delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)