import os


def get_txt_list(path):
    for x in os.listdir(path):
        tmp = x.endswith('txt')

