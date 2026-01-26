# leetcode 271
# ["Hello", "World", "Yes:Or:No"]

from typing import List


def encode(strs):
    text = ""
    for str in strs:
        text += f"{len(str)}:{str}"  # "5:Hello5:World9:Yes:Or:No"
    return text


def decode(s):
    ls, start = [], 0
    while start < len(s):
        mid = s.find(":", start)
        length = int(s[start:mid])
        ls.append(s[mid + 1 : mid + 1 + length])
        start = mid + 1 + length
    return ls


""" 
  list와 List의 차이
  list: 내장 타입. python 3.9+부터 지원
  List: typing 모듈의 전용 클래스. 
"""
