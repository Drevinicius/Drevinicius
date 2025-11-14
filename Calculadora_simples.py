import tkinter as tk

def calcular_resultado():
    valor_atual = entry.get()
    novo_valor = eval(valor_atual)
    limpar_entrada()
    entry.insert(0, novo_valor)

def limpar_entrada():
    entry.delete(0, tk.END)

def adicionar_valor(valor):
    valor_atual = entry.get()
    novo_valor = valor_atual + valor

    limpar_entrada()
    entry.insert(0, novo_valor)

# Projeto inacabado

root = tk.Tk()
root.geometry("400x450")

# Frames
frame_entry = tk.Frame(root)
frame_entry.pack(expand=True, fill='both')

frame_ope = tk.Frame(root)
frame_ope.pack(side='left',expand=True, fill='both')

frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

frame_1 = tk.Frame(root)
frame_1.pack(expand=True, fill='both')

frame_2 = tk.Frame(root)
frame_2.pack(expand=True, fill='both')

frame_3 = tk.Frame(root)
frame_3 .pack(expand=True, fill='both')

# Botões de operacao
mais = tk.Button(frame_ope, text='+', font=('verdana', 20), command=lambda: adicionar_valor('+'))
mais.pack(expand=True, fill='both')

menos = tk.Button(frame_ope, text='-', font=('verdana', 20), command=lambda: adicionar_valor('-'))
menos.pack(expand=True, fill='both')

divi = tk.Button(frame_ope, text='/', font=('verdana', 20), command=lambda: adicionar_valor('/'))
divi.pack(expand=True, fill='both')

mult = tk.Button(frame_ope, text='*', font=('verdana', 20), command=lambda: adicionar_valor('*'))
mult.pack(expand=True, fill='both')

# Botoes de numeros
entry = tk.Entry(frame_entry, font=('verdana', 35))
entry.pack(side='left', expand=True, fill='both')

button1 = tk.Button(frame, text="1", font=('verdana', 20), command=lambda: adicionar_valor('1'))
button1.pack(side='left', expand=True, fill='both')

button2 = tk.Button(frame, text="2", font=('verdana', 20), command=lambda: adicionar_valor('2'))
button2.pack(side='left', expand=True, fill='both')

button3 = tk.Button(frame, text='3', font=('verdana', 20), command=lambda: adicionar_valor('3'))
button3.pack(side = 'left',expand=True, fill='both')

button4 = tk.Button(frame_1, text='4', font=('verdana', 20), command=lambda: adicionar_valor('4'))
button4.pack(side = 'left',expand=True, fill='both')

button5 = tk.Button(frame_1, text='5', font=('verdana', 20), command=lambda: adicionar_valor('5'))
button5.pack(side = 'left',expand=True, fill='both')

button6 = tk.Button(frame_1, text='6', font=('verdana', 20), command=lambda: adicionar_valor('6'))
button6.pack(side = 'left',expand=True, fill='both')

button7 = tk.Button(frame_2, text='7', font=('verdana', 20), command=lambda: adicionar_valor('7'))
button7.pack(side = 'left',expand=True, fill='both')

button8 = tk.Button(frame_2, text='8', font=('verdana', 20), command=lambda: adicionar_valor('8'))
button8.pack(side = 'left',expand=True, fill='both')

button9 = tk.Button(frame_2, text='9', font=('verdana', 20), command=lambda: adicionar_valor('9'))
button9.pack(side = 'left',expand=True, fill='both')

button_ = tk.Button(frame_3, text='0', font=('verdana', 20), command=lambda: adicionar_valor('0'))
button_.pack(side = 'left',expand=True, fill='both')

button_ = tk.Button(root, text='c', font=('verdana', 20), command=limpar_entrada)
button_.pack(side = 'left',expand=True, fill='both')

button_ = tk.Button(root, text='=', font=('verdana', 20), command=calcular_resultado)
button_.pack(side = 'left',expand=True, fill='both')

#Tela principal
root.mainloop()
