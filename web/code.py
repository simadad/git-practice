# -*- coding: utf-8 -*-
import web

urls = (                                                    # controller      URL 控制器
    '/', 'Index',
    '/movie/(\d+)', 'Movie',
    '/cast/(.*)', 'Cast',
    '/director/(.*)', 'Director'
)
app = web.application(urls, globals())
db = web.database(dbn='sqlite', db='MovieSite.db')          # #      调用数据库，获取信息
render = web.template.render('templates/')                  # view    调用模版，设置信息显示格式


class Index:                                            # 控制函数 Index
    def __init__(self):
        pass

    def GET(self):
        print ('index_get')
        movies = db.select('movie')
        count = db.query('select count(*) as count from movie')[0]['count']
        return render.index(movies, count, None)

    def POST(self):
        print ('index_post')
        data = web.input()
        print type(data)
        print data.title
        condition = r'title like "%' + data.title + r'%"'   # data.title ?????????
        movies = db.select('movie', where=condition)
        count = db.query('select count(*) as count from movie where ' + condition)[0]['count']
        print count
        print type(count)
        return render.index(movies, count, data.title)


class Movie:                                                # 控制函数 Movie
    def __init__(self):
        pass

    def GET(self, movie_id):
        print ('movie_get')
        print movie_id
        movie_id = int(movie_id)
        movies = db.select('movie', where='id=$movie_id', vars=locals())[0]
        return render.movie(movies)


class Director:
    def __init__(self):
        pass

    def GET(self, movie_director):
        print ('director_get')
        print (movie_director)
        condition = r'directors like "%' + movie_director + r'%"'
        movies = db.select('movie', where=condition)
        count = db.query('select count(*) as count from movie where ' + condition)[0]['count']
        return render.index(movies, count, movie_director)


class Cast:
    def __init__(self):
        pass

    def GET(self, movie_cast):
        print ('cast_get')
        print (movie_cast)
        condition = r'casts like "%' + movie_cast + r'%"'
        movies = db.select('movie', where=condition)
        count = db.query('select count(*) as count from movie where ' + condition)[0]['count']
        return render.index(movies, count, movie_cast)

if __name__ == "__main__":
    app.run()


