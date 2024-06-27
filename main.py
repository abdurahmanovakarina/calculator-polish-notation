import tkinter as tk
from tkinter import ttk


def evaluate_rpn(expression):
    stack = []
    operators = ['+', '-', '*', '/', '**']
    result = 0
    for token in expression:
        if token not in operators:
            stack.append(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            elif token == '**':
                result = operand1 ** operand2
            
            stack.append(result)
    try:
        return stack[0]
    except:
        return 'Ошибка!'


def calculate():
    expression = entry.get()
    rpn_expression = expression.split()
    result = evaluate_rpn(rpn_expression)
    result_label.configure(text='Результат: ' + str(result))


root = tk.Tk()
root.title('Калькулятор ОПН')

label = ttk.Label(root, text='Введите выражение в ОПН:',  justify='center')
label.pack(pady=15, )

entry = ttk.Entry(root, width=30)
entry.pack(pady=35)

calculate_button = ttk.Button(root, text='Вычислить', command=calculate)
calculate_button.pack(pady=10)

result_label = ttk.Label(root, text='Результат:')
result_label.pack(pady=20)

root.mainloop()
