print("Добро пожаловать в калькулятор роста!\n")
height = int(input("Введите ваш рост в см "))
print("\nВаш рост:", height, "см" )
if height <= 0:
    print("Ты к врачу ходил?")
  
elif 0 < height <= 200:
    print("Довльно неплохо!")
  
else:
     print("Ты высокий!")
  