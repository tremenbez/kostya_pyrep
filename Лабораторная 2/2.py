salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 1.05  # Ежемесячный рост цен
money_capital = 0
AllMoney = 0
HowMuchYouWillNeed = 0

for i in range(1,months + 1):
    if i != 1:
        spend *= increase
    HowMuchYouWillNeed += spend
    AllMoney += salary
money_capital = int(round(HowMuchYouWillNeed - AllMoney))

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")
