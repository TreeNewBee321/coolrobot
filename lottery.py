import random
import requests
import json
import time
import os
import sys
import urllib
import hashlib
import datetime
import pymysql
from itertools import groupby
from collections import defaultdict
from cqhttp import CQHttp
bot = CQHttp(api_root='http://127.0.0.1:5700/',
             access_token='',
             secret='')

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) Appl\
eWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
pro_ids = []
pro_id = ""
group_id = []
name_list = []
money_list = []
# 存储的单位为百分比，从左到右依次是N,R,SR,SP,SSR,UR
rate = [40,30,15,10,3,2]
# 数据库卡列表
card = []
# 抽卡开关
cardswitch = False
# 资金档位列表
backerList = []
# 报图文件夹路径（普通）
normalDir = ""
normalTitle = ""
# 报图文件夹路径（高概率）
highRateDir = ""
highRateTitle = ""
# 高概率开关
highrate_switch = False
# 官托id列表
SpId = []
# 数据库设置
host = ''
port = 3306
user = ''
password = ''
database = ''
charset = ''

context = {
    "time": 1515204254,
    "post_type": "message",
    "message_type": "group",
    "sub_type": "group",
    "message_id": 12,
    "user_id": 701300248,
    "message": "查看卡牌",
    "raw_message": "查看卡牌"
}
def connect_database(host,port,user,password,database,charset):
    mysql_conn = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'db': database,
            'charset': charset
        }
    db = pymysql.connect(**mysql_conn)
    cursor = db.cursor()
    return db

def getSign(ret):
    tuple = sorted(ret.items(), key=lambda e: e[0], reverse=False)
    md5_string = urllib.parse.urlencode(tuple).encode(encoding='utf_8', errors='strict')
    md5_string += b'&p=das41aq6'
    sign = hashlib.md5(md5_string).hexdigest()[5: 21]
    return sign

def project_info(pro_ids):
    url = 'https://wds.modian.com/api/project/detail'
    pro_id = ""
    for _ in range(0,len(pro_ids)):
        if _ != len(pro_ids)-1:
            pro_id += str(pro_ids[_])
            pro_id += ','
        else :
            pro_id += str(pro_ids[_])
    form = {
        'pro_id': pro_id
    }
    sign = getSign(form)
    form['sign'] = sign
    response = requests.post(url, form, headers=header).json()
    project_name = response['data'][0]['pro_name']
    project_money = response['data'][0]['already_raised']
    project_goal = response['data'][0]['goal']
    project_backer = response['data'][0]['backer_count']
    if len(response['data'])>1:
        rival_money = response['data'][1]['already_raised']
    else :
        rival_money = 0
    return project_name,project_money,int(project_goal),project_backer,rival_money

# 生成随机数
def random_card(rate,thresh):
    start = 0
    randnum = random.randint(1, sum(rate))
    for index, item in enumerate(rate):
        if thresh > index:
            break
        start += item
        if randnum <= start:
            break      
    return index

# 引入rate
def getRate(n_rate,r_rate,sr_rate,sp_rate,ssr_rate,ur_rate):
    global rate
    for i in range(0,6):
        if i == 0:
            rate[i] = n_rate
        elif i == 1:
            rate[i] = r_rate
        elif i == 2:
            rate[i] = sr_rate
        elif i == 3:
            rate[i] = sp_rate
        elif i == 4:
            rate[i] = ssr_rate
        elif i == 5:
            rate[i] = ur_rate
    print(rate)        

def getType(tp):
    cardtype = ''
    if tp == 0:
        cardtype="N"
    elif tp == 1:
        cardtype = "R"
    elif tp == 2:
        cardtype = "SR"
    elif tp == 3:
        cardtype = "SP"
    elif tp == 4:
        cardtype = "SSR"
    elif tp == 5:
        cardtype = "UR"
    return cardtype  

#读卡的信息
def read_dir_card(dir):
    list_card = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            list_card.append(filename[0:-4])
    return list_card

# 初始化card
def init_card(level,highRateSwitch):
    BASE_DIR = ''
    if highRateSwitch:
        BASE_DIR = highRateDir
    else :
        BASE_DIR = normalDir
    if level == 0:
        cardpool_n = os.path.join(BASE_DIR, 'N/')
        list_n = read_dir_card(cardpool_n)
        return list_n
    elif level == 1:
        cardpool_r = os.path.join(BASE_DIR, 'R/')
        list_r = read_dir_card(cardpool_r)
        return list_r
    elif level == 2:
        cardpool_sr = os.path.join(BASE_DIR, 'SR/')
        list_sr = read_dir_card(cardpool_sr)
        return list_sr
    elif level == 3:
        cardpool_sp = os.path.join(BASE_DIR, 'SP/')
        list_sp = read_dir_card(cardpool_sp)
        return list_sp
    elif level == 4:
        cardpool_ssr = os.path.join(BASE_DIR, 'SSR/')
        list_ssr = read_dir_card(cardpool_ssr)
        return list_ssr    
    elif level == 5:
        cardpool_ur = os.path.join(BASE_DIR, 'UR/')
        list_ur = read_dir_card(cardpool_ur)
        return list_ur           

#抽卡
def choose_card(level):
    cardpool = init_card(level,highrate_switch)
    random.shuffle(cardpool)
    return random.choice(cardpool)


# base_std 进入抽卡的最低金额
# backer_money 支持的钱数
def drawLottery(user_id,base_std,backer_money):
    # 判断爸爸此次是否足够富裕可以抽卡
    global rate
    pieces = int(backer_money / base_std[0])
    thresh = 0
    for item in base_std:
        if backer_money > item:
            break
        thresh += 1

    tmp = []
    return_list = []
    type_list = defaultdict(list)
    for i in range(1,pieces+1):
        # 返回结果为rate数组的下标，1为N，2为R，3为SR，4为SP，5为SSR，6为UR
        result = 0
        if user_id not in SpId:
            result = random_card(rate,thresh)
        else :
            result = random_card([0,0,0,0,50,50],len(thresh))
        ### 在指定卡牌种类范围内随机抽取
        card_picked = choose_card(result)
        card = (card_picked,result)
        tmp.append(card)
        type_list[getType(result)].append(card_picked)
        # print("card_picked",card_picked)
        # print("result list",card_list)
    ## 卡牌去重
    for item in set(tmp):
        item = item + (tmp.count(item),)
        return_list.append(item)
    ### 卡牌排序,结果会返回卡牌中最好的一张
    return_list = sorted(return_list,key=lambda return_list:return_list[1],reverse=True)
    print(return_list)
    ### 返回最佳卡牌，卡牌数量，卡牌字典
    return return_list[0],pieces,type_list

     
def Time_format_conversion(dt):
    timeStamp = time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S"))
    return timeStamp

# 查询卡牌
def inquire_card(qqid,user_id):
    db=connect_database(host,port,user,password,database,charset)
    cursor = db.cursor()
    try:
        cursor.execute("SELECT *,sum(card_number) FROM lotteryrecord WHERE user_id=%s group by card_id;", (str(user_id)))
        result = cursor.fetchall()
        msg = "[CQ:at,qq="+str(qqid)+"]\n"
        msg += "当前拥有卡牌如下：\n"
        result_set = list(set(result))
        for item in result:
            msg += "%sx%d\n" %(item[5],item[7])
        return msg
        # db.commit()
    except Exception as e:
        print(e)
        # result_sql = list(map(lambda e: e[5], cursor.fetchall()))
        # result_set = list(set(result_sql))
        # for item in result_set:
        #     msg += "%sx%d  " % (item, result_sql.count(item))
        # return msg
    finally:
        db.close()

# 查询用户
def inquire_user(qqid, uid=None):
    db=connect_database(host,port,user,password,database,charset)
    cursor = db.cursor()
    if not uid:
        try:
            cursor.execute("SELECT * FROM qqids WHERE qq=%s",(str(qqid)))
        except Exception as e:
            print(e)
        else:
            result = cursor.fetchall()
        # ids中绑定过了qq
            if result:
                return inquire_card(qqid,result[0][1])
            else:
                return False
    # 有user_id，查询卡片
    else:
        return inquire_cardqqid,(uid)  

# qq绑定user_id
def bind_qq(qq, uid):
    if qq and uid:
        db=connect_database(host,port,user,password,database,charset)
        cursor = db.cursor()
        try:
            if inquire_user(qq):
                cursor.execute("UPDATE qqids set user_id=%s where qq=%s", (str(uid), str(qq)))
            else:
                cursor.execute("INSERT INTO qqids VALUES(NULL,%s,%s,NULL);", (str(uid), str(qq)))
        except Exception as e:
            db.rollback()
            print(e)
            return False
        else:
            db.commit()
            return True
        finally:
            db.close()
    else:
        return False

def getMessage():
    bot.run(host='127.0.0.1', port=8080)             
# 订单播报（带抽卡开关）
def getModianMessages(pro_ids,pro_id,url,switch_cards,backerStandard,cursor,db):
    page = 1
    form = {
        'page': page,
        'pro_id': pro_id
    }
    sign = getSign(form)
    form['sign'] = sign
    curr_datas = []
    for _ in range(0,1):
        response = requests.post(url, form, headers=header).json()
        # page = 1
        form['page'] = page
        for record in response['data']:
            curr_datas.append(record)
    msg=''
    total = 0
    for data in curr_datas:
        orderTime = Time_format_conversion(data['pay_time'])
        user_id = data['user_id']
        nickname = data['nickname']
        backer_money = data['backer_money']
        pay_time = data['pay_time']
        try:
            cursor.execute("INSERT INTO record VALUES (%s,%s,%s,%s,%s)", (pay_time,nickname,user_id,backer_money,pro_ids[0]))
            db.commit()
            msg += str(pay_time)
            msg += '\n'
            msg += "感谢【"+nickname+"】爸爸为本项目支持了【"+str(backer_money)+"】元！\n"
            total += 1
            
            db.commit()
        except Exception as e:
            db.rollback()
            continue 
        # 抽卡设置
        cursor.execute("SELECT * FROM lotteryRecord WHERE pay_time = %s",(pay_time))
        results = cursor.fetchall() 
        msg_card = []              
        if cardswitch and len(results) == 0:
            if float(data['backer_money']) >= float(backerStandard[0]): 
                best_card,pieces,card_list = drawLottery(user_id,backerStandard,data['backer_money'])
                if highrate_switch:                   
                    msg += "[CQ:image,file=%s\\%s\\%s.jpg]\n" %(highRateTitle,getType(best_card[1]),best_card[0]) 
                else:
                    msg += "[CQ:image,file=%s\\%s\\%s.jpg]\n" %(normalTitle,getType(best_card[1]),best_card[0])
                msg += "【"+nickname+"】当前共获得卡牌【"+str(pieces)+"】张。\n"
                for item in card_list:
                    msg += item+"卡有【"+str(len(card_list[item]))+"】张\n"
                    for card in set(card_list[item]):
                        msg += card+":"+str(card_list[item].count(card))+"张\n"
                        # 写入数据库
                        try:
                            cursor.execute("INSERT INTO lotteryRecord VALUES (%s,%s,%s,%s,%s,%s,%s)", (pay_time,nickname,user_id,pro_ids[0],item,card,str(card_list[item].count(card))))        
                            db.commit()
                        except Exception as e:
                            db.rollback()
                            print("This is error",e) 

    if total == 0:
        return msg  
    else :
        # 返回当前的项目名称，目标，已筹金额，支持人数，以及差距
        # 高亮：project_info的参数是所有待查询的项目的list
        project_name,project_raised,project_goal,project_backer,rival_money = project_info(pro_ids)
        msg += "\n"
        msg += str(project_name)
        msg += "\n"
        msg += " 当前参与人数为【"+str(project_backer)+"】人，已支持【"+str(project_raised)+"】元，距离完成目标还有【"+str(str(float(project_goal)-project_raised))+"】元\n"
        print(msg)
    return msg

def getOrders(pro_ids,group_id,cardswitch,backerList):
    # 初始化数据库
    db=connect_database(host,port,user,password,database,charset)
    cursor = db.cursor()
    # 初始化数据库表:订单表
    try:
        cursor.execute("""
            CREATE TABLE `sys`.`new_table` (
            `pay_time` DATETIME NOT NULL,
            `nickname` VARCHAR(45) NULL,
            `user_id` VARCHAR(45) NULL,
            `backer_money` VARCHAR(45) NULL,
            `pro_id` VARCHAR(45) NULL,
            PRIMARY KEY (`pay_time`))
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8;
        """)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
    # 初始化数据库表：抽卡记录表
    try:
        cursor.execute("""
            CREATE TABLE `sys`.`lotteryrecord` (
            `pay_time` DATETIME NOT NULL,
            `user_id` VARCHAR(45) NULL,
            `nickname` VARCHAR(45) NULL,
            `pro_id` VARCHAR(45) NULL,
            `card_type` VARCHAR(45) NULL,
            `card_id` VARCHAR(45) NULL,
            `card_number` VARCHAR(45) NULL,
            PRIMARY KEY (`pay_time`))
            ENGINE = InnoDB
            DEFAULT CHARACTER SET = utf8;
        """)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e) 
    # 初始化绑定信息表
    try: 
        cursor.execute("""
        CREATE TABLE `htt`.`qqids` (
        `qq` VARCHAR(45) NOT NULL,
        `user_id` VARCHAR(45) NULL,
        PRIMARY KEY (`qq`))
        ENGINE = InnoDB
        DEFAULT CHARACTER SET = utf8;
        """)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e) 
    # 开始实时拉取
    print('正在获取数据.....'+'\n')
    url = 'https://wds.modian.com/api/project/orders'
    # 上一次取得数据集
    # 起始页码
    page = 1
    # 对摩点id开始切片
    pro_id = ""
    for _ in range(0,len(pro_ids)):
        if _ != len(pro_ids)-1:
            pro_id += str(pro_ids[_])
            pro_id += ','
        else :
            pro_id += str(pro_ids[_])
   
    while True:
        msgs = getModianMessages(pro_ids,pro_id,url,cardswitch,backerList,cursor,db)
        print("Current msg:",msgs)
        for group in group_id:
            bot.send_group_msg_async(
                            group_id=group, message=msgs, auto_escape=False) 
        time.sleep(0.5)

def main():
    pass

if __name__ == '__main__':
    main()