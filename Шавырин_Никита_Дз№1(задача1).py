# Задача № 1
"""Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration
в секундах: до минуты: < s > сек; до часа: < m > мин < s > сек; до суток: < h > час < m > мин < s > сек;
*в остальных случаях: < d > дн < h > час < m > мин < s > сек."""

duration = int(input('Введите количество секунд: '))  # ввод пользователя
# в сутках 86400 секунд = 60*60*24

# объявление переменных
second = 1
minute = 60
hour = 3600
day = 86400

total_days = duration // day
# print(total_days)  проверка формулы для количества дней
total_hour = (duration % day) // hour
# print(total_hour)  для часов
total_minute = (duration % hour) // minute
# print(total_minute)  для минут
total_seconds = (duration % minute) // second
# print(total_seconds)  для секунд


if duration == day:
    print(f'{total_days} дн')  # для 86400 ( не знаю, может не стоило)
elif duration > day:
    print(f'{total_days} дн {total_hour} час {total_minute} мин {total_seconds} сек')
elif (duration > hour) and (duration < day):
    print(f'{total_hour} час {total_minute} мин {total_seconds} сек')
elif (duration > minute) and (duration < hour):
    print(f'{total_minute} мин {total_seconds} сек')
elif (duration > second) and (duration < minute):
    print(f'{total_seconds} сек')
else:
    print(f'{total_minute} мин {total_seconds} сек')  # если пользователь ввел 0
