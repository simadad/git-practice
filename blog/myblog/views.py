# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from models import Article, Blogger, Commenter, Tag
from django import forms
from PIL import Image
from random import randrange
from math import ceil
from django.http import HttpResponse, JsonResponse

# Create your views here.
tag_num = 10


def blogger_delete(delete_id):
    deleted_blogger = get_object_or_404(Blogger, id=delete_id)
    deleted_blogger.Status = False
    deleted_blogger.Nickname = '*MISSING*'
    deleted_blogger.Followed.clear()
    deleted_blogger.Followers.clear()
    deleted_blogger.save()


def index(request):
    article_new = Article.objects.all().order_by('-Pub_date')[:5]
    article_like = Article.objects.all().order_by('-Like')[:5]
    tag_all = Tag.objects.all().order_by('id')
    orders = [randrange(0, len(tag_all)) for i in range(tag_num)]
    tags = map(lambda x: tag_all[x], orders)

    return render(request, 'myblog/index.html', {
        'article_new': article_new,
        'article_like': article_like,
        'tags': tags
    })


def article(request, article_id):
    article_data = get_object_or_404(Article, pk=article_id)
    commenter_data = {}
    if request.method == 'POST':
        if 'commenter' in request.POST:
            global commenter_data
            commenter_data = request.POST
            Commenter.objects.create(
                Author=commenter_data['author'],
                Content=commenter_data['commenter'],
                Article=article_data
            )
        elif 'like' in request.POST:
            article_data.Like += 1
            article_data.save()
            return
        elif 'deleted_id' in request.POST:
            deleted_id = request.POST['deleted_id']
            blogger_id = request.POST['blogger_id']
            article_deleted = get_object_or_404(Article, id=deleted_id)
            article_deleted_blogger = get_object_or_404(Blogger, id=blogger_id)
            article_deleted.Status = False
            article_deleted.save()
            return redirect('/blog/blogger/%d' % article_deleted_blogger.id)
    else:
        # GET ##############
        pass
    original_id = article_data.Original_id
    original_article = get_object_or_404(Article, id=original_id)
    return render(request, 'myblog/article.html', {
        'article': article_data,
        'original': original_article
    })


@login_required
def blogger(request, blogger_id):
    blogger_data = get_object_or_404(Blogger, id=blogger_id)
    if request.method == 'POST':
        if'blogger_delete_id' in request.POST:
            blogger_id = request.POST['blogger_delete_id']
            blogger_delete(blogger_id)
            return redirect('/accounts/logout')
        elif 'followed' in request.POST:
            followed = request.POST.getlist('followed')             # TODO  可改进！！！###########################
            user_id = request.POST['user_id']
            user_data = get_object_or_404(Blogger, id=user_id)
            user_data.Followed = followed
            user_data.save()
        else:
            pass
    else:                     # GET ########################
        if not blogger_data.Status:
            return render(request, 'myblog/missing_blogger.html')
        else:
            pass
    return render(request, 'myblog/blogger.html', {
        'blogger': blogger_data
    })


def tag(request, tag_id):
    tag_data = get_object_or_404(Tag, id=tag_id)
    page = int(request.GET.get('page'))
    per_quantity = 6
    page_start = (page - 1) * per_quantity + 1
    page_end = page_start + per_quantity
    total = len(tag_data.Article.all())
    pages = int(ceil(total // per_quantity))
    articles = tag_data.Article.all().order_by('Author')[page_start:page_end]
    return render(request, 'myblog/tag.html', {
        'page': page,
        'pages': pages,
        'articles': articles,
        'tag': tag_data,
    })


@login_required
def editor(request):
    blogger_id = request.GET.get('user_id')
    article_id = request.GET.get('article_id')
    blogger_data = get_object_or_404(Blogger, id=blogger_id)
    if request.method == 'POST':
        article_data = request.POST
        title = article_data['title']
        content = article_data['content']
        if title and content:
            # article ####################################
            if int(article_id) < 0:
                edited_article = Article.objects.create(
                    Author=blogger_data,
                    Original_id=-1,
                    Title=title,
                    Content=content
                )
                edited_article.Original_id = edited_article.id
                edited_article.save()
            else:
                edited_article = get_object_or_404(Article, id=article_id)
                edited_article.Title = title
                edited_article.Content = content
                edited_article.save()
            # tags #####################################
            new_tag_data = article_data['new_tag_data'].split()
            changed_tag_data = request.POST.getlist('changed_tag_data')
            old_tag_data = edited_article.tag_set.all()
            if old_tag_data:
                # delete tags ##################################### TODO 待优化！！！！ #####
                for j in old_tag_data:
                    if j.Tag in changed_tag_data:
                        pass
                    else:
                        edited_article.tag_set.remove(j)
            else:
                pass
            if new_tag_data:
                # add new tags ################################
                for i in new_tag_data:
                    if Tag.objects.get_or_create(Tag=i):
                        new_tag = Tag.objects.get_or_create(Tag=i)[0]
                    new_tag.save()
                    new_tag.Article.add(edited_article)
            else:
                pass
            tag_all = Tag.objects.get(Tag='ALL')
            tag_all.Article.add(edited_article)
            return redirect('/blog/article/%d' % edited_article.id)
        else:
            pass
    else:
        # GET ###############################
        if int(article_id) < 0:
            # new article ##################################
            return render(request, 'myblog/editor.html', {
                'edited_article': None
            })
        else:
            # edited article ##########################
            edited_article = get_object_or_404(Article, id=article_id)
            return render(request, 'myblog/editor.html', {
                'edited_article': edited_article
            })


class ImgForm(forms.Form):
    favicon = forms.ImageField()


@login_required
def blogger_editor(request, blogger_id):
    blogger_data = get_object_or_404(Blogger, id=blogger_id)
    if request.method == 'POST':
        blogger_editor_data = request.POST
        nickname = blogger_editor_data['nickname']
        email = blogger_editor_data['email']
        gender = blogger_editor_data['gender']
        age = blogger_editor_data['age']
        intro = blogger_editor_data['intro']
        followed = request.POST.getlist('followed')        # 得到name同为followed的input元素的value的数组
        favicon = ImgForm(request.POST, request.FILES)
        if favicon.is_valid():
            favicon = favicon.cleaned_data['favicon']
            img = Image.open(favicon)
            img.save('media/img/favicon/%s.jpg' % blogger_id)
        else:
            favicon = blogger_data.Favicon

        if nickname and gender and age:
            blogger_data.Nickname = nickname
            blogger_data.User.email = email
            blogger_data.Gender = gender
            blogger_data.Age = age
            blogger_data.Favicon = favicon
            blogger_data.Followed = followed
            blogger_data.Intro = intro
            blogger_data.save()
            blogger_data.User.save()
        else:
            pass
    else:
        return render(request, 'myblog/blogger_editor.html', {
            'blogger': blogger_data
        })
    return redirect('/blog/blogger/%d' % int(blogger_id))


@login_required
def reprint(request):                                        # TODO 重复转载问题 ##################
    blogger_id = request.GET.get('user_id')
    article_id = request.GET.get('article_id')
    reprint_blogger = get_object_or_404(Blogger, id=blogger_id)
    original_article = get_object_or_404(Article, id=article_id)
    title = original_article.Title
    content = original_article.Content
    reprint_article = Article.all_objects.create(
        Title=title,
        Content=content,
        Author=reprint_blogger,
        Original_id=article_id
    )

    tag_all = Tag.objects.get(Tag='ALL')
    tag_reprint = Tag.objects.get(Tag='REPRINT')
    tag_all.Article.add(reprint_article)
    tag_reprint.Article.add(reprint_article)
    return redirect('/blog/article/%d' % reprint_article.id)


def ajax_like(request):
    article_id = request.GET.get('article_id')
    article_like = get_object_or_404(Article, id=article_id)
    article_like.Like += 1
    article_like.save()
    return HttpResponse(article_like.Like)
    # return JsonResponse('like', 10)


def ajax_commenter(request):
    comm_nick = request.POST.get('comm_nick')
    comm_cont = request.POST.get('comm_cont')
    comm_arti = request.POST.get('comm_arti')
    print comm_arti
    arti = get_object_or_404(Article, id=comm_arti)
    commenter = Commenter.objects.create(
        Article=arti,
        Author=comm_nick,
        Content=comm_cont,
    )
    # return HttpResponse(commenter.Pub_date)
    return HttpResponse(render(request, 'ajax/commenter.html', {
        'commenter': commenter
    }))


def ajax_tag_cloud(request):
    tag_all = Tag.objects.all().order_by('id')
    orders = [randrange(0, len(tag_all)) for i in range(tag_num)]
    tags = map(lambda x: tag_all[x], orders)
    return HttpResponse(render(request, 'ajax/cloud.html', {
        'tags': tags
    }))


def ajax_article_del(request):
    article_id = request.GET.get('id')
    article_to_del = get_object_or_404(Article, id=article_id)
    article_to_del.Status = False
    article_to_del.save()


def ajax_follow(request):
    user_id = request.GET.get('user_id')
    blogger_id = request.GET.get('blogger_id')
    user_data = get_object_or_404(Blogger, id=user_id)
    blogger_data = get_object_or_404(Blogger, id=blogger_id)
    blogger_data.Followers.add(user_data)
    blogger_data.save()
    return HttpResponse(render(request, 'ajax/follow.html', {
        'blogger': blogger_data
    }))
