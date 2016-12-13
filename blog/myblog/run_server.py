from myblog import models
import random


def random_char():
    return chr(random.randrange(97, 123))


def random_word(min_chars_pw=1, max_chars_pw=10):
    word = ''
    for i in range(random.randrange(min_chars_pw, max_chars_pw)):
        word += random_char()
    return word


def create_article_line(min_words_pl=5, max_words_pl=30, min_chars_pw=1, max_chars_pw=10):
    line = ''
    for i in range(random.randrange(min_words_pl, max_words_pl)):
        line += random_word(min_chars_pw, max_chars_pw)
        line += ' '
    return line + random_word(min_chars_pw, max_chars_pw)


def create_article(min_lines_pa=10, max_lines_pa=200, min_words_pl=5, max_words_pl=30, min_chars_pw=1, max_chars_pw=10):
    article = ''
    for i in range(random.randrange(min_lines_pa, max_lines_pa)):
        article += create_article_line(min_words_pl, max_words_pl, min_chars_pw, max_chars_pw)
        article += '\n'
    return article + create_article_line(min_words_pl, max_words_pl, min_chars_pw, max_chars_pw)


def add_article(add_authors, min_articles_pb=1, max_articles_pb=20, min_lines_pa=10, max_lines_pa=200, min_words_pl=5, max_words_pl=30, min_chars_pw=1, max_chars_pw=10):
    for author in add_authors:
        for i in range(random.randrange(min_articles_pb, max_articles_pb)):
            article_i = models.Article.objects.create(
                Title=create_article_line(1, 5, 1, 5),
                Author=author,
                Content=create_article(min_lines_pa, max_lines_pa, min_words_pl, max_words_pl, min_chars_pw, max_chars_pw),
                Like=random.randrange(10, 9999)
            )
            article_i.Original_id = article_i.id
            article_i.save()


def add_tag(add_articles, tag_numb=30, min_articles_pt=2, max_articles_pt=30, min_chars_pw=1, max_chars_pw=9):
    tag_all = models.Tag.objects.create(Tag='ALL')
    models.Tag.objects.create(Tag='REPRINT')
    for article in add_articles:
        tag_all.Article.add(article)
    for i in range(tag_numb):
        tag_i = models.Tag.objects.create(
            Tag=random_word(min_chars_pw, max_chars_pw),
        )
        for j in range(random.randrange(min_articles_pt, max_articles_pt)):
            tag_i.Article.add(add_articles[random.randrange(0, len(add_articles))])


if __name__ == '__main__':
    authors = models.Blogger.objects.all()
    add_article(authors)
    articles = models.Article.objects.all()
    add_tag(articles)
