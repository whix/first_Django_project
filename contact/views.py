__author__ = 'Administrator'
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from contact.forms import ContactForm
from django.template import RequestContext


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['675766918@qq.com']
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
            form = ContactForm(initial={'subject': 'I love your site!'})
    return render_to_response('contact_form.html', {'form': form},
                              context_instance=RequestContext(request))

def thanks(request):
    return HttpResponse("Thanks for your contact!")