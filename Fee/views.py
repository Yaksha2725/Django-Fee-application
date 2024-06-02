from .models import Payment, Fee_details
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import PaymentForm
from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt
def fees(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())


@csrf_exempt
def payment_form(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
        else:
            return HttpResponse(form)
            return render(request, 'myfirst.html', {'form': form})

@csrf_exempt
def success(request):
   paymentstatus = Payment.objects.all().values()
   template = loader.get_template('success.html')
   context = {
       'paymentstatus': paymentstatus
   }
   return HttpResponse(template.render(context, request))
@csrf_exempt
def fee_details(request):
  myfee = Fee_details.objects.all().values()
  template = loader.get_template('myfirst1.html')
  context = {
    'myfee': myfee,
  }
  return HttpResponse(template.render(context, request))


