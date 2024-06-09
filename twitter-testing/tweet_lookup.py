import tweepy

class Twitter(object):
    def accessLike(self):


        client = tweepy.Client(
            "Bearer Token AAAAAAAAAAAAAAAAAAAAAALMuAEAAAAAEGSc3XJASrqvdxUgrnzzvBTPGOM%3D3IMveIa3kxoM6TYJkNcQVu4SydyhDsdI8IH1gSSkPHkR9Wor8k")

        output = client.get_liking_users(1799340636799398057,user_auth=False)
        print(output)


t = Twitter()
t.accessLike()