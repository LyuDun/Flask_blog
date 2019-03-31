import requests
import asyncio
import pymysql
import random
import configparser 

cp = configparser.ConfigParser()
cp.read('mysql.cfg')
USER = cp.get('mysql','user')
PASSWORD = cp.get('mysql','password')

conn = pymysql.connect(host='localhost', port=3306, user=USER, passwd=PASSWORD, db='test',charset='utf8') 
cur = conn.cursor()

video_list = []


def LoadUserAgent(uafile):
    uas = []
    with open(uafile,'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1])
    random.shuffle(uas)
    return uas


uas = LoadUserAgent("user_agents.txt")



async def savedb():
    global video_list
    if len(video_list) != 0:
        row = video_list.pop()
        sql = "insert into bilibili values({0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]},{0[6]},{0[7]});".format(row) 
        try:
            ret = cur.execute(sql)
        except:
            conn.rollback()
        finally:
            conn.commit()


async def add_list(url):
    global video_list
    ua = random.choice(uas)
    header = {
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'api.bilibili.com',
        'Origin': 'https://www.bilibili.com',
        # 'Referer': 'https://www.bilibili.com/video/' + str(i) + '?spm_id_from=333.338.recommend_report.3',
        'User-Agent': ua
    }
    try:
        response  =  requests.get(url, headers=header).json()
        data = response['data']
        video = [
            int(data['aid']), data['view'], data['danmaku'],
            data['reply'], data['favorite'], data['coin'], data['share'], data['like']]
        video_list.append(video)
    except:
        pass
async def func(url):
    await add_list(url)
    await savedb()

if __name__ == "__main__":
    avid = 0
    try:
        for i in range(1, 2000):
            elem = (i - 1) * 10000
            urls = ['https://api.bilibili.com/x/web-interface/archive/stat?aid={}'.format(j) for j in 
                    range(elem, elem + 10000)]
            for url in urls:
                tasks = [
                        asyncio.ensure_future(func(url)),
                        ]
                loop = asyncio.get_event_loop()
                loop.run_until_complete(asyncio.wait(tasks))
                print('已爬取av%d'%avid)
                avid +=1
    except KeyboardInterrupt:
        loop.stop()
        loop.run_forever()
    finally:
        conn.close()
        loop.close()
        print('disconnected')
