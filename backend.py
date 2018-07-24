from cqhttp import CQHttp
from lottery import *
bot = CQHttp(api_root='http://127.0.0.1:5700/',
             access_token='',
             secret='')



# @bot.on_message('group')
# def handle_msg(context):
#     return {'reply': context['message'], 'at_sender': False}
group_id=[]
@bot.on_message('group')
def handle_msg(context):
    if context['group_id'] in group_id :
        # 查看卡牌
        if context['message'] == '查看卡牌':
            inquire_result = inquire_user(context['user_id'])
            if inquire_result:
                print("查看成功")
                bot.send(context, inquire_result)
            else:
                inq_reg = "请指定摩点id或先进行绑定操作"
                bot.send(context, inq_reg)
            

@bot.on_event('group_increase')  # 如果插件版本是 3.x，这里需要使用 @bot.on_event
def handle_group_increase(context):
    bot.send(context, message='欢迎新人～', is_raw=True)  # 发送欢迎新人


@bot.on_request('group', 'friend')
def handle_request(context):
    return {'approve': True}  # 同意所有加群、加好友请求

def threadStart():
    bot.run(host='127.0.0.1', port=8080)

def main():
    bot.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()