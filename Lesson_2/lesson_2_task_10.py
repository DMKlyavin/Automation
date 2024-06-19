def bank(x, y):
    rate = 0.10
    sum_after_y_years = x * (1 + rate) ** y
    return sum_after_y_years


x = float(input("Какую сумму вы хотите внести на депозит? "))
y = int(input("На сколько лет вы хотели бы сохранить свои инвестиции? "))
result = bank(x, y)
print(f"Если вы вносите депозит $ {x} на {
      y} лет, то у вас будет $ {result:.2f} на вашем счету")
