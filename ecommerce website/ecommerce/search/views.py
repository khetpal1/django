from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView

from products.models import Products


# class Searchproduct_listview(ListView):
#     template_name = "search/search.html"

#     # def get_context_data(self, *args, **kwargs):
#     #     context = super(Searchproduct_listview,
#     #                     self).get_context_data(*args, **kwargs)
#     #     context["query"] = self.request.GET.get("q")
#     #     return context

#     def get_queryset(self, *args, **kwargs):
#         request = self.request
#         # query = request.GET.get("q")
#         # print(query)

#         # if query is not None:
#         return Products.objects.filter(title="shirt")
#         # return Products.objects.all()


def Searchproduct_listview(request):
    query = request.GET["q"]
    lookups = Q(title__icontains=query) | Q(
        description__icontains=query) | Q(producttag__title__icontains=query)
    queryset = Products.objects.filter(lookups).distinct()
    context = {
        "objectslist": queryset

    }

    return render(request, "search/search.html", context)
