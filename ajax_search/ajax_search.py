# coding: utf-8
import urllib2
import json
import re


def get_voter(numb):
    # site = 'https://www.zhihu.com/answer/2785210/voters_profile?total=7217&offset=%d' % numb
    site = 'https://www.zhihu.com/answer/49838562/voters_profile?total=23&offset=%d' % numb
    # header = {'Cookie':'d_c0="AEBAHGyIwwqPTn314odGFi6Yg49DvvOvWJQ=|1477700682"; _zap=64bcf9a4-c2cf-41de-8b7a-b36eec4db6fb; q_c1=f742b605414240a98b2b58d9ee066192|1480382203000|1477700679000; a_t="2.0AAAAL0QmAAAXAAAArBNnWAAAAC9EJgAAAEBAHGyIwwoXAAAAYQJVTTyUZlgAAzSx_sawnd80Mp92dvjtryMkI-Joh97prUESAP1oTuIfhAH1Awt_5w=="; _xsrf=afdfb783a04aba27477948345ec1c446; s-t=autocomplete; s-q=%E4%BD%A0%E6%98%AF%E5%A6%82%E4%BD%95%E8%87%AA%E5%AD%A6%20Python%20%E7%9A%84%EF%BC%9F; s-i=1; sid=igpgvgcg; l_n_c=1; login="MDM2NDZjNDY2YWRiNDZhYWIxNjEwMzY3MTk5MDJlY2Y=|1481704427|82bf7626c64807779d3da587163b1a16008d1066"; l_cap_id="NTc1NWMyMDE0NTg3NGRiNmE4NGFlZDdmYTY1ZDE5YjE=|1481704427|382d548db7a552132c162f73523480149dcfd190"; cap_id="ODU4MmE1M2Y2MDQ2NDk4MGI0NmQ3MjE5NmJmY2E0MjY=|1481704427|31e3b397fb260ef4fd860cc3b080424ea310ae12"; r_cap_id="ODhhYjZhOWFiY2E0NDNhMWEzZGVlYTM3M2MwMzM0YzU=|1481704453|b714cc41a64c196c2b5ad2427e56f7200105e87a"; __utmt=1; n_c=1; __utma=51854390.833090728.1481697351.1481699970.1481702269.3; __utmb=51854390.25.9.1481704549146; __utmc=51854390; __utmz=51854390.1481697351.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/org/ying-shi-quan-za-zhi/answers; __utmv=51854390.100-1|2=registration_date=20140217=1^3=entry_date=20140217=1; z_c0=Mi4wQUFBQUwwUW1BQUFBUUVBY2JJakRDaGNBQUFCaEFsVk5LSkY0V0FEOGVCRE5nYVJpQWhBV0N6dmF3cGNqMllPVGV3|1481704552|20bd2e387780d821fe27271647b41407457d84b3'}
    # web = urllib2.Request(site, headers=header)
    web = urllib2.Request(site)
    info = urllib2.urlopen(web)
    info_json = info.read()
    info_dic = json.loads(info_json)
    info_list = info_dic['payload']
    return info_list


order = 0
voter_total = []
while True:
    voter_list = get_voter(order)
    if voter_list:
        for voter in voter_list:
            voter_name = re.search(r'(?<=title=").+?(?=")', voter).group()
            print voter_name
            voter_total.append(voter_name)
    else:
        break
    order += 10
print voter_total
