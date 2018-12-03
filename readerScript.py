#!/usr/bin/python
import praw
import os
import io

reddit = praw.Reddit('bot1')

# subreddit = reddit.subreddit("learnpython")

# for submission in subreddit.hot(limit=5):
#     print("Title: ", submission.title)
#     print("Text: ", submission.selftext)
#     print("Score: ", submission.score)
#     print("---------------------------------\n")

subreddit = reddit.subreddit("all")

with open("instance.txt","r") as t:
	instance = int(t.read())

Ulimit = 20
for submission in subreddit.hot(limit=Ulimit):
	print("Reading Instance: ",instance, "  - - - - ",Ulimit-instance, "remaining...")

	with io.open("thread_"+str(instance)+".txt",'w',encoding="utf-8") as f:
		f.write(submission.selftext)
		f.write("\n")
		
		submission.comments.replace_more(limit=None)
		comment_queue = submission.comments[:]  # Seed with top-level
		
		while comment_queue:
			comment = comment_queue.pop(0)
			f.write(comment.body)
			comment_queue.extend(comment.replies)

	instance = instance + 1

with open("instance.txt","w") as g:
	g.write(str(instance))
print("Script Completed")