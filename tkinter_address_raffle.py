import random
import tkinter as tk
import time

"""
This script creates a GUI application using Tkinter for conducting an address raffle. 
Users can input a list of addresses, specify the number of winners to be selected, 
and then perform the raffle to display the winners. 
The application logs the process and displays the results on the interface.
"""

def choose_winners(addresses, num_winners):
    if num_winners > len(addresses):
        return "Error: Not enough addresses to choose from"
    return random.sample(addresses, num_winners)

def show_winners():
    print(f"Draw conducted on {time.strftime('%d/%m/%Y')} at {time.strftime('%H:%M:%S')}\n")
    addresses = addresses_entry.get("1.0", tk.END).strip().split('\n')
    print(f"Number of addresses in the draw: {len(addresses)}")
    print(f"{time.strftime('%H:%M:%S')} | User entered addresses :\n\n{addresses}\n")
    num_winners = int(num_winners_entry.get())
    print(f"Number of winners selected: {num_winners}\n")
    winners = choose_winners(addresses, num_winners)
    if isinstance(winners, str):
        result_label.config(text=winners)
    else:
        result_str = '\n'.join(winners)
        if num_winners == 1:
            result_label.config(text=f"The winning address is:\n\n{result_str}\n")
            print(f"{time.strftime('%H:%M:%S')} | The winning address is: {winners}\n")
        else:
            result_label.config(text=f"The winning addresses are:\n\n{result_str}")
            print(f"{time.strftime('%H:%M:%S')} | The winning addresses are: {winners}\n")

root = tk.Tk()
root.title("Address Raffle | By 0x414854")
root.geometry("600x400")

addresses_label = tk.Label(root, text="Enter a copied list of addresses:")
addresses_label.pack()

addresses_entry = tk.Text(root, width=60, height=10)
addresses_entry.pack()

num_winners_label = tk.Label(root, text="How many winning addresses to choose?")
num_winners_label.pack()

num_winners_entry = tk.Entry(root)
num_winners_entry.pack()

draw_button = tk.Button(root, text="Draw", command=show_winners)
draw_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
