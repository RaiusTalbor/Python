import tkinter as tk

def get_selection():
    selected_value = var.get()
    print(f"Ausgewählte Zahl: {selected_value}")

# Anzahl der Radiobuttons festlegen
anzahl = 5  # Zum Beispiel 5

# Tkinter Fenster erstellen
root = tk.Tk()
root.title("Radiobutton Beispiel")
root.geometry("500x500")

# Variable, um die Auswahl zu speichern
var = tk.IntVar()

# Dynamisch Radiobuttons erstellen
for i in range(1, anzahl + 1):
    tk.Radiobutton(root, text=f"Auswahl: {i}", variable=var, value=i).pack()
var.set(1)

# Button, um die Auswahl anzuzeigen
btn = tk.Button(root, text="Auswahl anzeigen", command=get_selection)
btn.pack()

# Fenster starten
root.mainloop()
