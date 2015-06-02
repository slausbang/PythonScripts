from imgurpython import ImgurClient
import wget, time, datetime, os

#declare globals
today = datetime.date.today()
todaystr = today.isoformat()

string_input = input('Enter subreddit(s), separated by spaces: ')
input_list = string_input.split()
input_list = [str(a) for a in input_list]
timeperiod = input('Enter Timeperiod (week/day): ')

#imgur auth data
client_id = '1cd4ab0d955461d'
client_secret = '9ed65fc5d90719d0ab5875ac2f0099cf8c79d0c4'
client = ImgurClient(client_id, client_secret)

#create directory
if not os.path.exists(todaystr):
	print('creating directory..' + todaystr)
	os.mkdir(todaystr)
	os.chdir(todaystr)
elif os.path.exists(todaystr):
	os.chdir(todaystr)

#function to download the items we decide
def downloadItems(subreddit, timep):
	global client
	items=client.subreddit_gallery(subreddit, sort='time', window=timep)
	for item in items:
		wget.download(item.link)


for i in input_list:
	if not os.path.exists(i):
		print('creating directory..' + i)
		os.mkdir(i)
		os.chdir(i)
		downloadItems(i, timeperiod)
	else:
		os.chdir(i)
		downloadItems(i, timeperiod)
	os.chdir('../') #brings us back to the parent directory before starting on the next subreddit
	
	
		
