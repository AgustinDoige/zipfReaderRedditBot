#!/usr/bin/python
import praw
import io

print("Program Iniciated")
reddit = praw.Reddit('bot1')
sub = 'all'
subreddit = reddit.subreddit(sub)

instance = 1
cache_list = []
limite = 70

try:
	with open("cache_of_submissions.txt",'r') as f:
		lines = f.readlines()
		for line in lines:
			cache_list.append(line.rstrip())
except Exception:
	pass

for submission in subreddit.top('year',limit=limite):
	print("Opening Instance: ",instance, "  - - - - ",limite-instance, "remaining")

	if (submission.id in cache_list):
		print("Instance ",instance," already read")
	else:
		cache_list.append(submission.id)
		with io.open(sub+"_submission_"+str(instance)+".txt",'w',encoding="utf-8") as f:
			f.write(submission.title+"\n")
			f.write(submission.selftext+"\n")
			submission.comments.replace_more(limit=None)
			comment_queue = submission.comments[:]  # Seed with top-level

			print("Reading Instance: ",instance)
			while comment_queue:
				comment = comment_queue.pop(0)
				f.write("$C: "+comment.body+"\n")
				comment_queue.extend(comment.replies)

		with open("cache_of_submissions.txt",'a') as g:
			g.write(submission.id+"\n") #After comments have been written, it caches the submission

	instance = instance + 1
print("Completed.")