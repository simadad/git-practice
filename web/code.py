# -*- coding: utf-8 -*-
import web

urls = (                                                    # controller      URL 控制器
    '/', 'Index',
    '/movie/(\d+)', 'Movie'
)
app = web.application(urls, globals())
db = web.database(dbn='sqlite', db='MovieSite.db')          # #      调用数据库，获取信息
render = web.template.render('templates/')                  # view    调用模版，设置信息显示格式


class Index:                                            # 控制函数 Index
    def __init__(self):
        pass

    def GET(self):
        movies = db.select('movie')
        print ('get')
        return render.index(movies)

    def POST(self):
        data = web.input()
        condition = r'title like "%' + data.title + r'%"'
        movies = db.select('movie', where=condition)
        print ('post')
        return render.index(movies)


class Movie:                                                # 控制函数 Movie
    def __init__(self):
        pass

    def GET(self, movie_id):
        print 1
        movie_id = int(movie_id)
        print movie_id
        movie = db.select('movie', where='id=$movie_id', vars=locals())[0]
        print movie
        return render.movie(movie)
'''
movies = [
    {
        'title': 'Forrest Gump',
        'year': 1994,
    },
    {
        'title': 'Titanic',
        'year':	1997,
    },
]
'''

if __name__ == "__main__":
    app.run()
