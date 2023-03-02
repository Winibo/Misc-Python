from tkinter import *
from tkinter import ttk


# put init stuff here
root = Tk()

strength = StringVar()
dexterity = StringVar()
constitution = StringVar()
intelligence = StringVar()
wisdom = StringVar()
charisma = StringVar()

tab_frame = ttk.Frame(root)
tab_frame.grid(column=0, row=0)
stats = ttk.Frame(tab_frame)
stats.grid(column=0, row=0)

# Set up Stat Input Block
strength_input = ttk.Entry(stats, textvariable=strength, width=2)
dexterity_input = ttk.Entry(stats, textvariable=dexterity, width=2)
constitution_input = ttk.Entry(stats, textvariable=constitution, width=2)
intelligence_input = ttk.Entry(stats, textvariable=intelligence, width=2)
wisdom_input = ttk.Entry(stats, textvariable=wisdom, width=2)
charisma_input = ttk.Entry(stats, textvariable=charisma, width=2)

strength_input.grid(column=0, row=0)
dexterity_input.grid(column=1, row=0)
constitution_input.grid(column=2, row=0)
intelligence_input.grid(column=3, row=0)
wisdom_input.grid(column=4, row=0)
charisma_input.grid(column=5, row=0)

# Set up stat labels
strength_label = ttk.Label(stats, text="Str")
dexterity_label = ttk.Label(stats, text="Dex")
constitution_label = ttk.Label(stats, text="Con")
intelligence_label = ttk.Label(stats, text="Int")
wisdom_label = ttk.Label(stats, text="Wis")
charisma_label = ttk.Label(stats, text="Cha")

strength_label.grid(column=0, row=1)
dexterity_label.grid(column=1, row=1)
constitution_label.grid(column=2, row=1)
intelligence_label.grid(column=3, row=1)
wisdom_label.grid(column=4, row=1)
charisma_label.grid(column=5, row=1)

# Set Up Class List
chosen_class = StringVar()
class_list = ttk.Combobox(stats, textvariable=chosen_class,
                          values=["Barbarian", "Bard", "Cleric", "Druid", "Fighter",
                                  "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer",
                                  "Warlock", "Wizard"], state="readonly")
class_list.grid(column=2, row=2, columnspan=4)
class_label = ttk.Label(stats, text="Class:")
class_label.grid(column=0, row=2, columnspan=2)

roll_button = ttk.Button(stats, text="roll")
chosen_roll = StringVar()
roll_option = ttk.Combobox(stats, textvariable=chosen_roll, values=[])

for child in stats.winfo_children():
    child.grid_configure(padx=5, pady=5)
# Opens Window and Initializes program
root.mainloop()
