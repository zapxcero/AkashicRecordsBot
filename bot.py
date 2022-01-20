import praw
from constants import acronyms
import re
import os
from novel import Novel

commented = []


def main():
    reddit = praw.Reddit("bot2")
    subreddit = reddit.subreddit("MartialMemes")

    for submission in subreddit.hot(limit=10):
        search(submission)
        # novel = Novel(title)
        # reply(novel.details())


def search(submission):
    for comment in list(submission.comments):

        pattern = re.compile(r"[A-Z]{2,6}-?[A-Z]*")
        matches = pattern.finditer(comment.body)

        for match in matches:
            comment_id_list = read_file()
            acro = match.group(0)
            if acro in list(acronyms.keys()) and comment.id not in comment_id_list:
                comment_id_list.append(comment.id)
                write_file(comment_id_list)
                title = acronyms[match.group(0)]
                print(acro)
                print(title)
                novel = Novel(title)
                comment.reply(novel.formatted_reply())

            # read commented.txt and get list and
            # if match in acronyms.keys() and match not in

        # regex find matches
        # check if match in acronyms
        # check if comment id in commented
        # if true
        # return a title
        # for reply in comment.replies.list():
        #     print(reply.body.encode("ascii", "ignore"))


# end def


def read_file():
    if not os.path.isfile("commented.txt"):
        pass
    else:
        with open("commented.txt", "r") as f:
            f_list = f.read()
            f_list = f_list.split("\n")
            f_list = list(filter(None, f_list))
            return f_list


# end def


def write_file(commented):
    with open("commented.txt", "w") as f:
        for id in commented:
            f.write(id + "\n")


# end def


if __name__ == "__main__":
    main()


# Todo
# search for title surrounded by <>
# search for replies of comments as well since i have only done the root comments
