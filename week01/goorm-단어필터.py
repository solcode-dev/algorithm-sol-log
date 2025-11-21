# 단어필터

n, m = map(int, input().split())
word = input().strip()
text = input().strip()

# word가 text에 없을 때까지 반복
while word in text:
    text = text.replace(word, "")

print(text if text else "EMPTY")
