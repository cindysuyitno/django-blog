import csv
from django.http import HttpResponse
from .models import Post

def save_post(request):
    post = Post.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attatchment; filename="Post.csv"'

    writer = csv.writer(response)
    writer.writerow(['author','title','text','created date','published_date','blog'])

    for p in post:
        writer.writerow([p.author.username,p.title,p.text,p.created_date,p.published_date,p.blog])
    
    return response