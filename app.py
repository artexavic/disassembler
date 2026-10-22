import tkinter as tk
import logic

root = tk.Tk()

ds = logic.disasembler()

root.title('Дизассемблер')
root.geometry('1200x600')
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

def on_click():
    output_text.delete("1.0", tk.END)
    hex_code = input_text.get("1.0", tk.END)
    out_text = ds.make_asm_code(hex_code)
    print(out_text)
    output_text.insert("1.0", out_text)


input_text = tk.Text(root, border=5, font=('Consolas', 12), wrap='word')
input_text.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

output_text = tk.Text(root, border=5, font=('Consolas', 12), wrap='word')
output_text.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

button = tk.Button(root, text="Перевести", border=5, font=('Consolas', 16), command=on_click)
button.grid(row=1, columnspan=2, pady=10)


root.mainloop()