# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from models import Article, Blogger, Commenter, Tag

# Create your views here.


def blogger_delete(delete_id):
    deleted_blogger = get_object_or_404(Blogger, id=delete_id)
    deleted_blogger.Status = False
    deleted_blogger.Nickname = '*MISSING*'
    deleted_blogger.Followed.clear()
    deleted_blogger.Followers.clear()
    deleted_blogger.save()


def index(request):
    # article_data = Article.objects.all().filter(Status=True).order_by('-Pub_date')[:5]
    article_data = Article.objects.all().order_by('-Pub_date')[:5]
    print article_data[0].Author.id
    return render(request, 'myblog/index.html', {
        'articles': article_data
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
        elif 'deleted_id' in request.POST:
            deleted_id = request.POST['deleted_id']
            blogger_id = request.POST['blogger_id']
            article_deleted = get_object_or_404(Article, id=deleted_id)
            article_deleted_blogger = get_object_or_404(Blogger, id=blogger_id)
            article_deleted.Status = False
            article_deleted.save()
            return redirect('/blog/blogger/%d' % article_deleted_blogger.id)
    else:
        pass
    return render(request, 'myblog/article.html', {
        'article': article_data
    })


@login_required
def blogger(request, blogger_id):
    blogger_data = get_object_or_404(Blogger, id=blogger_id)
    if request.method == 'POST':
        if 'article_deleted_id' in request.POST:
            article_id = request.POST['article_deleted_id']
            article_deleted = get_object_or_404(Article, id=article_id)
            article_deleted.Status = False
            article_deleted.save()
        elif 'blogger_delete_id' in request.POST:
            blogger_id = request.POST['blogger_delete_id']
            blogger_delete(blogger_id)
            return redirect('/accounts/logout')
        elif 'followed' in request.POST:
            followed = request.POST.getlist('followed')               # 可改进！！！###########################
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
    return render(request, 'myblog/tag.html', {
        'tag': tag_data
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
                    Title=title,
                    Content=content
                )
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
                # delete tags ######################################## 待优化！！！！ #####
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


@login_required
def blogger_editor(request, blogger_id):
    blogger_data = get_object_or_404(Blogger, id=blogger_id)
    if request.method == 'POST':
        blogger_editor_data = request.POST
        nickname = blogger_editor_data['nickname']
        email = blogger_editor_data['email']
        gender = blogger_editor_data['gender']
        age = blogger_editor_data['age']
        # favicon = blogger_editor_data['favicon']
        followed = request.POST.getlist('followed')        # 得到name同为followed的input元素的value的数组
        intro = blogger_editor_data['intro']
        if nickname and email and gender and age and intro:
            blogger_data.Nickname = nickname
            blogger_data.User.email = email
            blogger_data.Gender = gender
            blogger_data.Age = age
            # blogger_data.Favicon = favicon
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
