from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions
from sushi_rinjin.models.order import Order
from sushi_rinjin.models.order import OrderSerializer
from sushi_rinjin.models.order_list import OrderList
from sushi_rinjin.models.order_list import OrderListEditSerializer


class OrderEdit(APIView):
    queryset = Order.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sushi_rinjin/for_rest/order_edit_rest.html'

    authentication_classes((SessionAuthentication, BasicAuthentication))
    permission_classes((permissions.IsAuthenticated,))

    def get(self, request, id_order):
        order_for_edit = get_object_or_404(Order, id=id_order)
        serializer = OrderSerializer(order_for_edit)
        return Response({'serializer': serializer, 'order': order_for_edit})

    def post(self, request, id_order):
        order_for_edit = get_object_or_404(Order, id=id_order)
        serializer = OrderSerializer(order_for_edit, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'order': order_for_edit})
        if 'edit' in request.POST:
            serializer.save()
        if 'delete' in request.POST:
            order_for_edit.delete()
        return HttpResponseRedirect('/sushi_rinjin/orders/')


class OrderDetailEdit(APIView):
    queryset = OrderList.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sushi_rinjin/for_rest/order_detail_edit_rest.html'

    authentication_classes((SessionAuthentication, BasicAuthentication))
    permission_classes((permissions.IsAuthenticated,))

    def get(self, request, id_order, order_list_id):
        order_list_edit = get_object_or_404(OrderList, id=order_list_id)
        serializer = OrderListEditSerializer(order_list_edit)
        return Response({'serializer': serializer, 'order_list':
                        order_list_edit, 'id_order': id_order})

    def post(self, request, id_order, order_list_id):
        order_list_edit = get_object_or_404(OrderList, id=order_list_id)
        serializer = OrderListEditSerializer(order_list_edit, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'order_list':
                            order_list_edit, 'id_order': id_order})
        if 'edit' in request.POST:
            serializer.save()
        if 'delete' in request.POST:
            order_list_edit.delete()
        return HttpResponseRedirect('/sushi_rinjin/order/' + id_order)
