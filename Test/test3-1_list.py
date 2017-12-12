naver_end_price = [474500, 461500, 501000, 500500, 488500]

print(max(naver_end_price)-min(naver_end_price))

# print(naver_end_price)
# print(naver_end_price[2])

naver_end_date = ['09/07', '09/08', '09/09', '09/10', '09/11']

naver_end_dic = dict(zip(naver_end_date, naver_end_price))
print(naver_end_dic)

print(naver_end_dic['09/10'])
