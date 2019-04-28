import os


def get_imlist(path):

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

path=('D:\work\Python_work\shixun_work\Image')
print(get_imlist(path))
