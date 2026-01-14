import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np

from dempster_logic import dempster_rule
from problems import hardware_sources, emergency_sources

# ===== Funcție pentru afișare rezultate =====
def show_result(label, result):
    text = ""
    for k, v in result.items():
        text += f"{set(k)} : {round(v,3)}\n"
    label.config(text=text)

# ===== Fereastra principală =====
root = tk.Tk()
root.title("Regula Dempster–Shafer (5 stări)")
root.geometry("750x650")

tabs = ttk.Notebook(root)
tabs.pack(expand=True, fill="both")

# ================= TAB 1 – Diagnostic hardware =================
tab_hw = ttk.Frame(tabs)
tabs.add(tab_hw, text="Diagnostic hardware")

entries_hw = []
for txt in [
    "Temperatură: DEF_ELECT / DEF_MECH / FUNC / UNC1 / UNC2",
    "Raport de sistem: DEF_ELECT / DEF_MECH / FUNC / UNC1 / UNC2"
]:
    ttk.Label(tab_hw, text=txt).pack(pady=2)
    row = []
    for _ in range(5):  # 5 stări
        e = ttk.Entry(tab_hw, width=10)
        e.pack()
        row.append(e)
    entries_hw.append(row)

hw_result = ttk.Label(tab_hw, text="", justify="left")
hw_result.pack(pady=10)

hw_test_list = tk.Listbox(tab_hw, height=10)
hw_test_list.pack(fill="both", pady=10)

# Funcții pentru hardware
def calc_hw():
    try:
        vals = [float(e.get()) for row in entries_hw for e in row]
        m1, m2 = hardware_sources(*vals)
        res = dempster_rule(m1, m2)
        show_result(hw_result, res)
    except:
        messagebox.showerror("Eroare", "Date invalide")

def add_hw_test():
    try:
        vals = [float(e.get()) for row in entries_hw for e in row]
        m1, m2 = hardware_sources(*vals)
        res = dempster_rule(m1, m2)

        states = ["DEFECT_ELECTRONIC","DEFECT_MECHANIC","FUNCTIONAL",
                  ("DEFECT_ELECTRONIC","DEFECT_MECHANIC"),
                  ("DEFECT_ELECTRONIC","DEFECT_MECHANIC","FUNCTIONAL")]

        values = []
        for s in states:
            if isinstance(s, tuple):
                values.append(round(res.get(frozenset(s),0),3))
            else:
                values.append(round(res.get(frozenset({s}),0),3))

        hw_test_list.insert(tk.END,
            f"DEF_ELECT={values[0]}, DEF_MECH={values[1]}, FUNC={values[2]}, UNC1={values[3]}, UNC2={values[4]}")

    except:
        messagebox.showerror("Eroare", "Date invalide")

def plot_hw_tests():
    if hw_test_list.size() == 0:
        messagebox.showinfo("Info", "Nu există teste adăugate.")
        return

    states = ["DEF_ELECTRONIC","DEFECT_MECHANIC","FUNCTIONAL","UNC1","UNC2"]
    all_tests = []

    for i in range(hw_test_list.size()):
        line = hw_test_list.get(i)
        # extrage valorile din string
        vals = [float(x.split('=')[1]) for x in line.split(',')]
        all_tests.append(vals)

    x = np.arange(len(states))
    width = 0.2
    plt.figure(figsize=(10,6))
    colors = ['red','orange','green','blue','gray']

    for idx, test in enumerate(all_tests):
        plt.bar(x + idx*width, test, width, label=f'Test {idx+1}', alpha=0.7)

    plt.xticks(x + width*(len(all_tests)-1)/2, states)
    plt.ylim(0,1)
    plt.ylabel("Grad de credință")
    plt.title("Comparare teste hardware – Dempster–Shafer")
    plt.legend()
    plt.show()

ttk.Button(tab_hw, text="Calculează un test", command=calc_hw).pack(pady=2)
ttk.Button(tab_hw, text="Adaugă test în listă", command=add_hw_test).pack(pady=2)
ttk.Button(tab_hw, text="Afișează grafic teste", command=plot_hw_tests).pack(pady=2)

# ================= TAB 2 – Situație de urgență =================
tab_em = ttk.Frame(tabs)
tabs.add(tab_em, text="Situație de urgență")

entries_em = []
for txt in [
    "Senzor fum: EM_FIRE / EM_HEAT / NORMAL / UNC1 / UNC2",
    "Senzor temperatură: EM_FIRE / EM_HEAT / NORMAL / UNC1 / UNC2"
]:
    ttk.Label(tab_em, text=txt).pack(pady=2)
    row = []
    for _ in range(5):
        e = ttk.Entry(tab_em, width=10)
        e.pack()
        row.append(e)
    entries_em.append(row)

em_result = ttk.Label(tab_em, text="", justify="left")
em_result.pack(pady=10)

em_test_list = tk.Listbox(tab_em, height=10)
em_test_list.pack(fill="both", pady=10)

# Funcții pentru urgență
def calc_em():
    try:
        vals = [float(e.get()) for row in entries_em for e in row]
        m1, m2 = emergency_sources(*vals)
        res = dempster_rule(m1, m2)
        show_result(em_result, res)
    except:
        messagebox.showerror("Eroare", "Date invalide")

def add_em_test():
    try:
        vals = [float(e.get()) for row in entries_em for e in row]
        m1, m2 = emergency_sources(*vals)
        res = dempster_rule(m1, m2)

        states = ["EMERGENCY_FIRE","EMERGENCY_HEAT","NORMAL",
                  ("EMERGENCY_FIRE","EMERGENCY_HEAT"),
                  ("EMERGENCY_FIRE","EMERGENCY_HEAT","NORMAL")]

        values = []
        for s in states:
            if isinstance(s, tuple):
                values.append(round(res.get(frozenset(s),0),3))
            else:
                values.append(round(res.get(frozenset({s}),0),3))

        em_test_list.insert(tk.END,
            f"EM_FIRE={values[0]}, EM_HEAT={values[1]}, NORMAL={values[2]}, UNC1={values[3]}, UNC2={values[4]}")

    except:
        messagebox.showerror("Eroare", "Date invalide")

def plot_em_tests():
    if em_test_list.size() == 0:
        messagebox.showinfo("Info", "Nu exista teste adaugate.")
        return

    states = ["EMERGENCY_FIRE","EMERGENCY_HEAT","NORMAL","UNC1","UNC2"]
    all_tests = []

    for i in range(em_test_list.size()):
        line = em_test_list.get(i)
        vals = [float(x.split('=')[1]) for x in line.split(',')]
        all_tests.append(vals)

    x = np.arange(len(states))
    width = 0.2
    plt.figure(figsize=(10,6))

    for idx, test in enumerate(all_tests):
        plt.bar(x + idx*width, test, width, label=f'Test {idx+1}', alpha=0.7)

    plt.xticks(x + width*(len(all_tests)-1)/2, states)
    plt.ylim(0,1)
    plt.ylabel("Grad de credintă")
    plt.title("Comparare teste urgentă – Dempster–Shafer")
    plt.legend()
    plt.show()

ttk.Button(tab_em, text="Calculeaza un test", command=calc_em).pack(pady=2)
ttk.Button(tab_em, text="Adauga test in lista", command=add_em_test).pack(pady=2)
ttk.Button(tab_em, text="Afiseaza grafic teste", command=plot_em_tests).pack(pady=2)

root.mainloop()
