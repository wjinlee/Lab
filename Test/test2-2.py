daum_price = 89000
naver_price = 751000
daum_num = 100
naver_num = 20

def total():
    sum0 = (daum_price * daum_num) + (naver_price * naver_num)
    return sum0

total0 = total()
print('total0 = \ {:,}'.format(total0))

daum_price = daum_price * (1-0.05)
naver_price = naver_price * (1-0.10)

total1 = total()
loss = total0 - total1
print('loss = \ {:,}'.format(loss))
