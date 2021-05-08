import pandas as pd

n = int(input("Введите номер месяца: "))
month = ["0", "Январе", "Феврале", "Марте", "Апреле", "Мае", "Июне", "Июле", "Августе", "Сентябре", "Октябре", "Ноябре", "Декабре"]
for i in range(len(month)):
    mon = month[n]


# 1.68 - киловатт э/э
def electricity(present_testimony, past_testimony):
    amount_electricity = (present_testimony - past_testimony) * 1.68
    return amount_electricity


present_testimony = int(input("Введите новые показания счетчика э/э: "))
past_testimony = int(input("Введите прошлые показания счетчика э/э: "))


# 14.928 - водопостачання, 10.456 - водовідведення
def water(present_water_testimony, past_water_testimony):
    amount_water = (present_water_testimony - past_water_testimony) * 14.928 + (present_water_testimony - past_water_testimony) * 10.356
    return amount_water


present_water_testimony = int(input("Введите новые показания водяного счетчика: "))
past_water_testimony = int(input("Введите старые показания водяного счетчика: "))

# 51.24 - тариф на вывоз мусора
garbage_tarif = 51.24

amount = round(electricity(present_testimony, past_testimony) + water(present_water_testimony, past_water_testimony) + garbage_tarif, 2)

print()
print(f"В {mon} нужно заплатить за электричество:", electricity(present_testimony, past_testimony), "гривны. \n")
print(f"В {mon} нужно заплатить за воду:", water(present_water_testimony, past_water_testimony), "гривны. \n")
print(f"В {mon} нужно заплатить за мусор : {garbage_tarif} гривны. \n")
print(f"Всего нужно заплатить в {mon}: {amount} гривны. \n")

df = pd.DataFrame({'Месяц': [mon],
                   'Показания э/э счетчика': [present_testimony],
                   'Оплачено за э/э': [electricity(present_testimony, past_testimony)],
                   'Показания водяного счетчика': [present_water_testimony],
                   'Оплачено за воду': [water(present_water_testimony, past_water_testimony)],
                   'Всего заплачено': [amount]})

df.to_excel(f'./tables/communal_payments_{mon}.xlsx')
