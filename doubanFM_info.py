# coding:utf-8

import os,urllib,json,time,csv

# 华语=1 欧美=2 粤语=6 法语=22 日语=17 韩语=18 
# 民谣=8 摇滚=7 爵士=13 古典=27 轻音乐=9 电子=14 R&B=16 说唱=15 电影原声=10 
# 七零=3 八零=4 九零=5 豆瓣音乐人=26 女声=20 动漫=28 NESCAFE=32 
# 乐混翻唱=52 格调卡萨帝=54

channel = 28

def get_list():
	url = 'http://douban.fm/j/mine/playlist?type=n&channel='+str(channel)
	json_get = urllib.urlopen(url)
	json_music = json.load(json_get)

	for i in json_music['song']:
		title = i['title']
		artist = i['artist']
		albumtitle = i['albumtitle']
		album = i['album']
		album_url = 'http://music.douban.com'+album
		url = i['url']
		picture = i['picture']
		try:
			rating_avg = i['rating_avg']
			company = i['company']
			public_time = i['public_time']
		except:
			pass
		sid = i['sid']
		aid = i['aid']

		num_before = len(sid_set)
		sid_set.add(sid)
		num_after = len(sid_set)
	
		title_u = title.encode('utf-8')
		artist_u = artist.encode('utf-8')
		sid_u = sid.encode('utf-8')
		aid_u = aid.encode('utf-8')
		albumtitle_u = albumtitle.encode('utf-8')
		url_u = url.encode('utf-8')

		if (num_before != num_after)&(sid[0:2] != 'da'):
			writer.writerow([title_u,artist_u,sid_u,rating_avg,albumtitle_u,album_url,url_u])

def main():
	global sid_set
	sid_set = set()
	global writer
	writer = csv.writer(file('doubanFM_info_'+str(channel)+'.csv', 'wb'))
	writer.writerow(['title','artist','sid','rating_avg','albumtitle','album_url','url'])
	for i in range(200):
		get_list()
		time.sleep(1)

main()