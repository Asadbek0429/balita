from django.shortcuts import render, redirect
from .models import Contact
import telepot
from blog.models import Tag, Post


def contact_view(request):
    if request.method == 'POST':
        data = request.POST
        obj = Contact.objects.create(name=data.get('name'), email=data.get('email'),
                                     phone_number=data.get('phone_number'), message=data.get('message'))
        obj.save()

        telegramBot = telepot.Bot('6601466546:AAFmwhsxCRsEglPR2jBBCZIclWesYZe7HS8')
        text = f'Project: Balita\nName: {data["name"]} \nEmail: {data["email"]} \nMessage: {data["message"]}'
        telegramBot.sendMessage(-1002084571362, text, parse_mode="Markdown")
        return redirect('/contact')

    d = {
        'contact': 'active',
        'popular_posts': Post.objects.filter(is_published=True).order_by('-created_at')[:3],
        'tags': Tag.objects.all(),
    }
    return render(request, 'contact.html', d)
