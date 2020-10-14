from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView, DetailView
from cart.models import Create

from .models import Products
# Create your views here.


class productfeaturedetailview(DetailView):
    template_name = "products/featureddetail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Products.objects.featured()


class productfeaturelistview(ListView):
    # queryset=Products.objects.all()
    template_name = r"products/featuredlist.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Products.objects.featured()

    # def getdata(request):
    #     context={
    #         "objecctslist":queryset
    #     }
    #     return render(request, "products/list.html", context)

    # def get_context_data(self, *args, **kwargs):
    #     context=super(product_view, self).get_context_data( *args, **kwargs)


class product_view(ListView):
    queryset = Products.objects.all()
    template_name = r"C:\Users\harshad\Desktop\django\ecommerce website\ecommerce\ecommerce\templates\products\list.html"

    # def getdata(request):
    #     context={
    #         "objecctslist":queryset
    #     }
    #     return render(request, "products/list.html", context)

    # def get_context_data(self, *args, **kwargs):
    #     context=super(product_view, self).get_context_data( *args, **kwargs)

    #     return context


def product_listview(request):
    queryset = Products.objects.all()
    context = {
        "objectslist": queryset
    }

    return render(request, "products/list.html", context)


class article_detail(DetailView):
    queryset = Products.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(article_detail, self).get_context_data(*args, **kwargs)
        cart_obj = Create.objects.new_or_get(self.request)
        context["cart"] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get("slug")
        try:
            instance = Products.objects.filter(slug=slug)
        except Products.DoesNotExist:
            raise Http404("Not avalible.....")
        except Products.MultipleObjectsReturned:
            qs = Products.objects.filter(slug=slug)
            instance = qs.first()
        return instance


class product_detialedview(DetailView):
    # queryset=Products.objects.all()
    template_name = "products/detail.html"

    # try:
    #     model=Products

    # except Products.DoesNotExist:
    #     raise Http404("product does not exists")

    # context_object_name="products"

    # def get_context_data(self, *args, **kwargs):
    #     context= super(product_detialedview, self).get_context_data(*args, **kwargs)
    #     return context
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get("pk")
        instance = Products.objects.get_by_id(pk)
        return instance


def product_detaillistview(request, pk=None, *args, **kwargs):
    # instance= Products.objects.get(pk=pk)

    instance = Products.objects.get_by_id(pk)
    print(instance)

    # instance= get_object_or_404(Products, pk=pk)
    context = {
        "object": instance
    }

    return render(request, "products/detail.html", context)
