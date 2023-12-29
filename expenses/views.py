from django.shortcuts import render

from django.urls import path
from django.db.models import Sum, Q

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# relative import of forms
from .models import Expense
from .forms import ExpenseForm, CalculateForm

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = { "saved": False }

    # add the dictionary during initialization
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        context["saved"]=True
        exp = form.save()
        context["id"]=exp.id

    context['form'] = form
    return render(request, "create_view.html", context)

def calculate_view(request):
    context = {}
    form = CalculateForm(request.POST or None)
    if form.is_valid():
        my_sum = Expense.objects.filter(day__month=form.data["month"]).aggregate(total=Sum('sum'))['total']
        context["my_sum"]=my_sum

    # add form dictionary to context
    context["form"] = form

    return render(request, "calculate_view.html", context)
def list_view(request):
  # dictionary for initial data with
  # field names as keys
  context = {}

  # add the dictionary during initialization
  context["dataset"] = Expense.objects.all()

  return render(request, "list_view.html", context)

def detail_view(request, id):
  # dictionary for initial data with
  # field names as keys
  context = {}

  # add the dictionary during initialization
  context["data"] = Expense.objects.get(id=id)

  return render(request, "detail_view.html", context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {"saved": False}

    # fetch the object related to passed id
    obj = get_object_or_404(Expense, id=id)

    # pass the object as instance in form
    form = ExpenseForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        context["saved"] = True
        context["id"] = id

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)


# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Expense, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)

def index(request):
    """View function for home page of site."""
    context = {}
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)