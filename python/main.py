
import matplotlib.pyplot as plt
import numpy as np


days = [1, 2, 3, 4, 5, 6, 7]
temperature = [12, 15, 14, 17, 19, 18, 21]

plt.figure(figsize=(8, 5))
plt.plot(days, temperature, color='blue', marker='o')

plt.title('Температура воздуха за неделю')
plt.xlabel('День')
plt.ylabel('Температура, °C')
plt.grid(True)

plt.show()



subjects = ['Математика', 'Физика', 'Информатика',
            'Английский язык']
grades = [4.1, 3.8, 4.7, 4.3]

colors = ['red', 'blue', 'green', 'orange']

plt.figure(figsize=(9, 5))
plt.bar(subjects, grades, color=colors)

plt.title('Средняя успеваемость студентов')
plt.xlabel('Предметы')
plt.ylabel('Средняя оценка')
plt.ylim(0, 5)
plt.grid(axis='y')

plt.show()

max_grade = max(grades)
best_subject = subjects[grades.index(max_grade)]

print('Задание 2:')
print('Самая высокая средняя оценка:', best_subject)
print('Средняя оценка:', max_grade)



categories = ['Продукты', 'Транспорт',
              'Коммунальные услуги', 'Связь', 'Прочее']

expenses = [120000, 30000, 45000, 15000, 40000]

plt.figure(figsize=(8, 7))

plt.pie(
    expenses,
    labels=categories,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Структура ежемесячных расходов семьи')
plt.show()

max_expense = max(expenses)
max_category = categories[expenses.index(max_expense)]

print('\nЗадание 3:')
print('Наибольшая статья расходов:', max_category)
print('Сумма:', max_expense, 'тенге')



results = [
    45, 52, 55, 58, 60, 62, 65, 67, 70, 70,
    72, 74, 75, 78, 80, 82, 85, 88, 90, 95
]

plt.figure(figsize=(8, 5))

counts, bins, patches = plt.hist(
    results,
    bins=5,
    color='orange',
    edgecolor='black'
)

plt.title('Распределение результатов тестирования')
plt.xlabel('Количество баллов')
plt.ylabel('Количество студентов')
plt.grid(axis='y')

plt.show()

max_interval = np.argmax(counts)

print('\nЗадание 4:')
print('Большинство результатов находится в диапазоне:',
      bins[max_interval], '-', bins[max_interval + 1])
print('Количество студентов:', int(counts[max_interval]))



hours = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
scores = [48, 52, 55, 60, 65, 70, 73, 78, 84, 90]

plt.figure(figsize=(8, 5))

plt.scatter(hours, scores, color='blue', marker='o')

plt.title('Связь времени подготовки и результата экзамена')
plt.xlabel('Количество часов подготовки')
plt.ylabel('Результат экзамена')

plt.grid(True)
plt.show()

print('\nЗадание 5:')
print('1. Наблюдается положительная связь.')
print('2. Да, с увеличением времени подготовки результат растёт.')
print('3. Нет, график показывает связь, но не доказывает,')
print('   что подготовка является единственной причиной результата.')
