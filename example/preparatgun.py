"""
preparatgun created by monsherko 29.03.2018
"""
from operator import itemgetter, attrgetter
import glob, os, sys
import config
#def prepare(path_name):

def prepare(dirpath):
    a = [s for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort(key=lambda s: os.path.getmtime(os.path.join(dirpath, s)))
#a - list отсортированных по дате измненения
    for x in range(0, len(a) - config.keep):
        os.remove(dirpath + a[x])
