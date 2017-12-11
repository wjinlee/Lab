daum_price = 89000
naver_price = 751000

total = daum_price*100 + naver_price*20
print('total = \ {:,}'.format(total))

daum_price_sub = daum_price*(1-0.05)
naver_price_sub = naver_price*(1-0.10)

total1 = daum_price_sub*100 + naver_price_sub*20
sub = total - total1
print('loss = W {:,}'.format(sub))

