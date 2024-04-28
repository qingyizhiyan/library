city = ['福州','泉州','厦门','漳州','宁德','龙岩','莆田','三明']
rate = [5.2,4.8,3.1,6.5,8.6,3.8,3.6,1.8]
city.append('南平')
rate.append(5.0)
city_rate = list(zip(city,rate))
print(city_rate)
dic_city_rate = dict(zip(city,rate))
print('厦门2023年的GDP增速（％）为：',dic_city_rate['厦门']})
city_xzq = []
for i in range(len(city)):
  if city[i] in ['厦门','漳州','泉州']:
    city_xzq.append((city[i],rate[i]))
city_xzq.sort(key = lambda x:x[1])
print(f'2023年闽南地区GDP增速从高到低的城市分别是{city_xzq[0][0]}、{city_xzq[1][0]}、{city_xzq[2][0]}')
