import requests,json
accessToken=input("輸入access Token")#"EAAFFIVZCgE6wBAAxbaXl60ulx7Jm8R7QIdRCxsyW9zMxZBEUw5M2l11n1HZC5UN8iYv91zDU7F62ILNoBXOdXOA0ZB4r7Otcq95eV3cQyMgNImK7HhkL9OUxhAqwpMeX8Ume5C4yVEjLGmmRFtFxUOk2fEMkZCjtTfp9bnb1fQXhRvkQZBBsRT58ZCj9G8OGC1PQ34JSuSClNNxxNCy7TupM3rohS3cgMMbK2wkku3zOiNEYib3v3dz"
url="https://graph.facebook.com/v13.0/me/posts?access_token="
#access token若過期需重新設定
data=json.loads(requests.get(url+accessToken).text)
print(requests.get(url).text)
message_count=0
for d in data['data']:
    print(d)
    if 'message' in d:
        print("貼文內容為:{}".format(d['message']))
        print("發文時間是:{}".format(d['created_time']))
        print("發佈ID是:{}".format(d['id']))
        print()
        message_count+=1
print("總貼文數為:%d"%message_count)