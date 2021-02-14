import datetime
def calculate_age(iin):
    a_string = iin
    birth_date = []
    century = []
    for index in range(0, 6, 2):
        birth_date.append(a_string[index : index + 2])
    for index in range(6, 7, 2):
        century.append(a_string[index : index + 1])

    cent =''
    if (century[0] == '1' or century[0] =='2'):
        cent = '18'
    elif (century[0] == '3' or century[0] =='4'):
        cent = '19'
    elif (century[0] == '5' or century[0] =='6'):
        cent = '20'

    year_l = cent+birth_date[0]
    month_l = birth_date[1]
    day_l = birth_date[2]
    date_time_str = year_l+'-'+month_l+'-'+day_l
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')

    # print(date_time_obj.date())
    def calc_age(born):
        today = datetime.date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    return calc_age(date_time_obj)

# print(calculate_age('000605550375'))
