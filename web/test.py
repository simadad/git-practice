import web
import urllib2
import json

addrs = [u'1308857', u'1292270', u'3011235', u'1419936', u'1291879', u'10777687', u'1302425', u'1292281', u'1905462', u'5964718', u'1291557', u'1304102', u'1308767', u'10577869', u'1292728', u'1307793', u'1300374', u'2363506', u'1296753', u'25917973', u'1306249', u'1305690', u'1291853', u'4798888', u'11026735', u'1292659', u'1293181', u'2300586', u'3011051', u'3395373', u'1307811', u'1292217', u'1294638', u'6874403', u'1291844', u'1292233', u'1292214', u'1291568', u'1307315', u'1297478', u'1793929', u'2053515', u'1291992', u'24750126', u'3075287', u'6307447', u'1292062', u'1959195', u'1299361', u'1308575', u'1302467', u'1401118', u'1292287', u'1308817', u'1292329', u'4739952', u'3217169', u'1303394', u'1292056', u'1438652', u'1308777', u'3157605', u'1302476', u'1395091', u'2365260', u'1293764', u'1293908', u'1299327', u'6534248', u'1292218', u'1867345', u'1301171', u'1305725', u'1309027', u'4023638', u'25773932', u'1428175', u'1298653', u'25814707', u'3073124', u'6146955', u'1300117', u'5908478', u'1300741', u'1293530', u'1293929', u'1862151', u'1316572', u'1301617', u'1304073', u'1756073', u'4286017']
db = web.database(dbn='sqlite', db='MovieSite.db')


def get(num):
    webs = urllib2.urlopen('https://api.douban.com/v2/movie/subject/%d' % num)
    page = webs.read()
    movie = json.loads(page)
    return movie


def data_insert(movie):
    db.insert(
        'movie',
        id=int(movie['id']),
        title=movie['title'],
        origin=movie['original_title'],
        url=movie['alt'],
        rating=movie['rating']['average'],
        image=movie['images']['large'],
        directors=','.join([d['name'] for d in movie['directors']]),
        casts=','.join([c['name'] for c in movie['casts']]),
        year=movie['year'],
        genres=','.join(movie['genres']),
        countries=','.join(movie['countries']),
        summary=movie['summary'],
    )
a = 0
print type(addrs)

for i in addrs:
    print i
    try:
        movie_info = get(int(i))
    except urllib2.HTTPError:
        print i, 'lost'
        continue
    data_insert(movie_info)
    a += 1
    print a
