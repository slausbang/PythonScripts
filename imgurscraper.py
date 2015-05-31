from imgurpython import ImgurClient
import wget, time, datetime, os

#gather variables
today = datetime.date.today()
todaystr = today.isoformat()
subreddit = input('Enter subreddit: ')
timeperiod = input('Enter Timeperiod (week/day): ')

#create directories
if not os.path.exists(todaystr):
	print('creating directory..' + todaystr)
	os.mkdir(todaystr)
	os.chdir(todaystr)
elif os.path.exists(todaystr):
	os.chdir(todaystr)

if not os.path.exists(subreddit):
	print ('creating directory..' + subreddit)
	os.mkdir(subreddit)
	os.chdir(subreddit)
elif os.path.exists(subreddit):
	os.chdir(subreddit)

#begin imgur collection section
client_id = '1cd4ab0d955461d'
client_secret = '9ed65fc5d90719d0ab5875ac2f0099cf8c79d0c4'

client = ImgurClient(client_id, client_secret)

items=client.subreddit_gallery(subreddit, sort='time', window=timeperiod)
for item in items:
	wget.download(item.link)
