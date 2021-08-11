#列出程式數量
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        #if count % 1000 == 0:
            #print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

#print(data[0])


#文字計數
wc = {}   #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1  #新增新的key進wc字典
for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print('一共有' ,len(wc), '個英文單字')

while True:
    word = input('請問你想查詢甚麼單字:')
    if word == 'q':
        print('感謝您使用本查詢功能')
        break
    if word in wc:
        print(word,'出現過的次數為', wc[word])
    else:
        print('這個字沒有出現過喔!')


#------------------------------------
sum_len = 0  #目前的總數(長度)
for d in data:  #每一個d就是一個留言
    sum_len = sum_len + len(d)
print('留言的平均長度是', sum_len/len(data))

#算出平均

#------------------------------------
new = []
for d in data:   #每一個d是一個留言
    if len(d) < 100:
        new.append(d)
print('一共有', len(new),'筆留言長度小於100')
print('第一筆資料:',data[0])

#篩選字數低於100的資料
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有',len(good), '筆留言提到good')
print(good[0])

# #------------------------------1. = 2.
#2.
#good = [d for d in data if 'good' in d]
#最前面的d是append後面括號裡面的d，是一整個留言的意思
#如果改為1，那麼會變成:留言中有good的話，就存1僅去清單中
#若為'bad' in d，則變成:d(留言)中有bad這個字的話，就做判斷(true 或 false)，印出來都是true 或 false