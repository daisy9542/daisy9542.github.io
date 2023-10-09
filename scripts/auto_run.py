import os


def hexo_commit():
    command = 'hexo clean && hexo g && hexo d'
    flag = -1

    while flag != 0:
        flag = os.system(command)


def new_blog(title):
    command = f'hexo new {title}'
    os.system(command)


hexo_commit()
# new_blog('word2vec')
