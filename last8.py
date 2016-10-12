import shutil

for i in range(8):
    shutil.copy2('/Users/bubble/Desktop/script.py', '/Users/bubble/Desktop/pics/script{}.py'.format(i))
