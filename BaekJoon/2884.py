h, m = map(int, input().split())

# m이 45분 이상인 경우 -> 45분 일찍 알람 저장 -> m에서 45를 빼면 된다
# m이 45분 미만인 경우 -> h를 1시간 이전으로 조정, m은 60-(45-m) / 현재 시간이 0시라면 이전 시간은 23시

if m >= 45:
    print(h, m-45)
else:
    if h==0:
        print(23, m+15)
    else:
        print(h-1, m+15)