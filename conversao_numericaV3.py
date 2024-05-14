from tkinter import Entry, Label, StringVar, Tk, OptionMenu, Button, Text

def converter():
    try:
        base = base_var.get()
        valor = valor_entry.get()
        valor = int(valor)
        
        if base == "Binário":
            binario = bin(valor)
            binario = str(binario)[2:]
            binario = '0b' + binario
            resultado_text.delete(1.0, "end")  # Clear previous result
            resultado_text.insert("end", binario)
        elif base == "Octal":
            octal = oct(valor)
            octal = str(octal)[2:]
            octal = '0o' + octal
            resultado_text.delete(1.0, "end")  # Clear previous result
            resultado_text.insert("end", octal)
        elif base == "Hexadecimal":
            hexadecimal = hex(valor)
            hexadecimal = str(hexadecimal)[2:]
            hexadecimal = '0x' + hexadecimal
            resultado_text.delete(1.0, "end")  # Clear previous result
            resultado_text.insert("end", hexadecimal)
        elif base == "Decimal":
            resultado_text.delete(1.0, "end")  # Clear previous result
            resultado_text.insert("end", str(valor))
        else:
            resultado_text.delete(1.0, "end")  # Clear previous result
    except ValueError:
        resultado_text.delete(1.0, "end")  # Clear previous result
        resultado_text.insert("end", "Valor inválido")

janela = Tk()
janela.title("Conversor de bases")
janela.geometry('500x300')
janela.configure(background='#3E3E3E')

valor_label = Label(janela, text="Valor:", font=('Arial', 14), bg='#3E3E3E', fg='white')
valor_label.pack(pady=10)

valor_entry = Entry(janela, font=('Arial', 14))
valor_entry.pack(pady=5)

base_label = Label(janela, text="Base:", font=('Arial', 14), bg='#3E3E3E', fg='white')
base_label.pack(pady=10)

base_var = StringVar(janela)
base_var.set("Binário")  # Valor padrão para a opção de base

base_options = ["Binário", "Octal", "Hexadecimal", "Decimal"]  # Updated base options
base_menu = OptionMenu(janela, base_var, *base_options)
base_menu.config(font=('Arial', 12))
base_menu.pack(pady=5)

button = Button(janela, text="Converter", command=converter, font=('Arial', 12), bg='#4CAF50', fg='white')
button.pack(pady=20)

resultado_label = Label(janela, text="Resultado:", font=('Arial', 14), bg='#3E3E3E', fg='white')
resultado_label.pack()

resultado_text = Text(janela, font=('Arial', 16), bg='#3E3E3E', fg='white', height=1)
resultado_text.pack()

janela.mainloop()
