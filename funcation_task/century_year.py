#https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python

def century(year):
    return int(year / 100 + 1) if year % 100 else year / 100