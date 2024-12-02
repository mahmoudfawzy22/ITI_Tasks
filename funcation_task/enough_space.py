#https://www.codewars.com/kata/5875b200d520904a04000003/train/python

def enough(cap, on, wait):
     return 0 if cap - on - wait >= 0 else -(cap - on - wait)