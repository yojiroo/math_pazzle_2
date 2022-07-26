N = 30

def check(num):
    #各数字に必要な光の数
    light = [6,2,5,5,4,5,6,3,7,6]
    s = light[num//10] + light[num%10]
    return s

lights = []
for i in  range(60):
    lights.append(check(i))

cnt = 0
for h in range(24):
    for m in range(60):
        for s in range(60):
            if(lights[h] + lights[m] + lights[s] == N):
                cnt += 1

print(cnt)
