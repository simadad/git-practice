# coding: utf-8
from django.shortcuts import render
from myblog import models
from math import ceil
from django.db.models import Q
import re
# from django.contrib.auth.decorators import login_required
# Create your views here.


def article_new(request):
    page = int(request.GET.get('page'))
    per_quantity = 6
    page_start = (page-1)*per_quantity+1
    page_end = page_start+per_quantity
    total = len(models.Article.objects.all())
    pages = int(ceil(total//per_quantity))
    articles = models.Article.objects.all().order_by('-Pub_date')[page_start:page_end]
    return render(request, 'search/article_new.html', {
        'page': page,
        'pages': pages,
        'articles': articles,
    })


def article_like(request):
    page = int(request.GET.get('page'))
    per_quantity = 6
    page_start = (page - 1) * per_quantity + 1
    page_end = page_start + per_quantity
    total = len(models.Article.objects.all())
    pages = int(ceil(total // per_quantity))
    articles = models.Article.objects.all().order_by('-Like')[page_start:page_end]
    return render(request, 'search/article_like.html', {
        'page': page,
        'pages': pages,
        'articles': articles,
    })


def article_tag(request):
    page = int(request.GET.get('page'))
    per_quantity = 6
    page_start = (page - 1) * per_quantity + 1
    page_end = page_start + per_quantity
    total = len(models.Tag.objects.all())
    pages = int(ceil(total // per_quantity))
    tag_all = models.Tag.objects.all()
    tag_order = sorted(tag_all, key=lambda x: x.article_quantity)
    tags = tag_order[page_start:page_end]
    return render(request, 'search/article_tag.html', {
        'page': page,
        'pages': pages,
        'tags': tags,
    })

'''
def article_search(request):
    page = int(request.GET.get('page'))
    search = request.GET.get('search')
    per_quantity = 6
    page_start = (page-1)*per_quantity+1
    page_end = page_start+per_quantity
    if search == 'new':
        article_total = len(models.Article.objects.all())
        article_pages = int(ceil(article_total // per_quantity))
        articles_pub = models.Article.objects.all().order_by('-Pub_date')[page_start:page_end]
        return render(request, 'search/search.html', {
            'page': page,
            'pages': article_pages,
            'articles': articles_pub,
            'title': '最新作品'

        })
    elif search == 'like':
        article_total = len(models.Article.objects.all())
        article_pages = int(ceil(article_total // per_quantity))
        articles_like = models.Article.objects.all().order_by('-Like')[page_start:page_end]
        return render(request, 'search/search.html', {
            'page': page,
            'pages': article_pages,
            'articles': articles_like,
            'title': '最赞作品'

        })
    elif search == 'tag':
        tag_total = len(models.Tag.objects.all())
        tag_pages = int(ceil(tag_total//per_quantity))
        tag_article_quantity = models.Tag.objects.all().order_by('-article_quantity')[page_start:page_end]
        return render(request, 'search/search.html', {
            'page': page,
            'pages': tag_pages,
            'articles': tag_article_quantity,
            'title': '标签云'
        })
'''


def search_engine(request):
    info = request.POST['search']
    findings = re.findall(r'\w+', info)
    article_all = models.Article.objects.all()
    blogger_all = models.Blogger.objects.all()
    commenter_all = models.Commenter.objects.all()
    tag_all = models.Tag.objects.all()

    result = {
        'article': {
            'title': [],
            'content': [],
        },
        'blogger': {
            'nickname': [],
            'intro': [],
        },
        'commenter': {
            'author_article': [],
            'content_article': [],
        },
        'tag': {
            'tag': [],
        }
    }
    '''
    for article in article_all:
        if info in article.Title:
            result['article']['title'].append(article)
        elif info in article.Content:
            result['article']['content'].append(article)
        else:
            pass
    for blogger in blogger_all:
        if info in blogger.Nickname:
            result['blogger']['nickname'].append(blogger)
        elif info in blogger.Intro:
            result['blogger']['intro'].append(blogger)
        else:
            pass
    for commenter in commenter_all:
        if info in commenter.Author:
            result['commenter']['author_article'].append(commenter.Article)
        elif info in commenter.Content:
            result['commenter']['content_article'].append(commenter.Article)
        else:
            pass
    for tag in tag_all:
        if info in tag.Tag:
            result['tag']['tag'].append(tag)
        else:
            pass
    '''
    q_article_title = Q()
    q_article_content = Q()
    q_blogger_nickname = Q()
    q_blogger_intro = Q()
    q_commenter_author = Q()
    q_commenter_content = Q()
    q_tag_tag = Q()
    for finding in findings:
        q_article_title = Q(Title__icontains=finding) and q_article_title
        q_article_content = Q(Content__icontains=finding) and q_article_content
        q_blogger_nickname = Q(Nickname__icontains=finding) and q_blogger_nickname
        q_blogger_intro = Q(Intro__icontains=finding) and q_blogger_intro
        q_commenter_author = Q(Author__icontains=finding) and q_commenter_author
        q_commenter_content = Q(Content__icontains=finding) and q_commenter_content
        q_tag_tag = Q(Tag__icontains=finding) and q_tag_tag
        result['article']['title'] = models.Article.objects.filter(q_article_title)
        result['article']['content'] = models.Article.objects.filter(q_article_content)
        result['blogger']['nickname'] = models.Blogger.objects.filter(q_blogger_nickname)
        result['blogger']['intro'] = models.Blogger.objects.filter(q_blogger_intro)
        result['commenter']['author_article'] = models.Commenter.objects.filter(q_commenter_author)
        result['commenter']['content_article'] = models.Commenter.objects.filter(q_commenter_content)
        result['tag']['tag'] = models.Tag.objects.filter(q_tag_tag)
    return render(request, 'search/result.html', {
        'result': result,
    })
