import operator
def ds(my_dates):
    dic={}
    for i in range(len(my_dates)):
        s = list(my_dates[i])
        s[-3]=''
        string = "".join(s)
        dic[i]=string
    sorted_x = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    ret=[]
    for i in range(10):
        try:
            ret.append(sorted_x[i][0])
        except:
            break
    return ret
# my_dates.sort(reverse=True,key=lambda date: datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z"))
