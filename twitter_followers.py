import requests
import tweepy

def get_followers_count(account_url):
    auth = tweepy.AppAuthHandler("3rJOl1ODzm9yZy63FACdg", "5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8")
    api = tweepy.API(auth)

    account_name = account_url.rsplit('/', 1)[-1]

    follower_count = api.get_user(account_name).followers_count

    return account_name, follower_count

if __name__ == '__main__':
    print("Please enter Twitter profile URL:")
    name, count = get_followers_count(input())
    print("User {} has {} followers".format(name, count))