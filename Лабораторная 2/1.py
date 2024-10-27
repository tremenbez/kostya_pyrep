money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 1.05  # Ежемесячный рост цен
count_ = 1
AllMoney = money_capital

while True:
    if count_ != 1:
        spend *= increase

    AllMoney += salary
    AllMoney -= spend
    count_ += 1

    if AllMoney < spend:
        break

print("Количество месяцев, которое можно протянуть без долгов:", count_)

