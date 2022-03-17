import facebook
token="EAAFFIVZCgE6wBAO4hqjiEJqulIT9ZA7YlB9A0wlOOZCwUvZAqEKS5pnZBK72drmx7ZCw5IZB55jspMrLuhpRY51c4yIdLBl8fxbeknuqjbkKUxtlZAgdY5qR6URZBMEbOdZB8em09IAd9nBTCjzgZAkLNhT9dIoLCXOR1XYH259KjHVmo0fvXbpDWqAJeAUvACXZBowAmixjzIhpbQZCdRAD4o0jindwx7vJRDqpd2rYRywxW4zlN8skmXR8I"
graphAPI_module=facebook.GraphAPI(access_token=token,version=3.1)
post=graphAPI_module.get_object(id='1943755399053255_4782024681892965')
# print(post["id"])
if 'message' in post:
    print(post['message'])
else:
    print('message缺失')
    
print()
post2=graphAPI_module.get_object(id='1943755399053255_4782024681892965?fields=message')
print('訊息:{}'.format(post['message']))
post2=graphAPI_module.get_object(id='1943755399053255_4782024681892965?fields=created_time')
print('發布時間:{}'.format(post['created_time']))
print()
pages=graphAPI_module.get_connections(id="me", connection_name="posts")#me 表示自己 post表示關聯類別
posts=pages['data']
for p in posts:
    if 'message' in p:
        print('訊息:{}'.format(p['message']))
        print('貼文日期:{}'.format(p['created_time']))
        print()

