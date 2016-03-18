# coding: UTF-8
# Chinese Zodiac

year = int(input("Enter a year: "))

if year % 12 == 8:
	animal = "용"
elif year % 12 == 9:
	animal = "뱀"
elif year % 12 == 10:
	animal = "말"
elif year % 12 == 11:
	animal = "양"
elif year % 12 == 0:
	animal = "원숭이"
elif year % 12 == 1:
	animal = "닭"
elif year % 12 == 2:
	animal = "개"
elif year % 12 == 3:
	animal = "돼지"
elif year % 12 == 4:
	animal = "쥐"
elif year % 12 == 5:
	animal = "소"
elif year % 12 == 6:
	animal = "호랑이"
elif year % 12 == 7:
	animal = "토끼"

print("%d is the year of the %s." % (year, animal))