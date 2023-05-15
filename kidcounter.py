import tkinter as tk
from tkinter import messagebox
import csv
import os



def open_csv_file():
    if os.path.exists(os.getcwd()+'\\data.csv'):
        try:
            path = os.getcwd()+'\\data.csv'
            #print(path)
            os.startfile(path)
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "The CSV file cannot be found.")

    else:
        messagebox.showinfo("File Not Found", "The CSV file does not exist yet.")



def validate_entries(*args):
    if entry1.get() and entry2.get() and entry3.get():
        button.config(state=tk.NORMAL)  
    else:
        button.config(state=tk.DISABLED)
        
        
def update_csv_file(sorted_number_list):
    with open(os.getcwd()+'\\data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['Number', 'Name', 'Prize'])
        writer.writeheader()
        #writer.writerows(sorted_number_list.keys())
        
        writer.writerows(sorted_number_list)
        


def delete_row():
    global number_list
    number = entry1.get()
    if not number.isdigit():
        messagebox.showerror("Invalid Input", "Number must be an integer.")
        return

    number = int(number)
    new_list = []
    doneflag = 0
    for item in number_list:
        if int(item['Number'])==number:
            doneflag = 1
        else:
            new_list.append(item)
            
    number_list = new_list
    
    if doneflag == 1:
        messagebox.showinfo("Row Deleted", "Row with number {} has been deleted.".format(number))
        sorted_number_list = sorted(number_list,key=lambda d: int(d['Number']))
        update_csv_file(sorted_number_list) 
    elif doneflag == 0:
        messagebox.showinfo("Row Not Found", "Row with number {} does not exist.".format(number))


        
        
def check_values():
    global number_list
    number = entry1.get()
    name = entry2.get()
    prize = entry3.get()

    if not number.isdigit():
        messagebox.showerror("Invalid Input", "Number must be an integer.")
        return

    if not all([name, prize]):
        messagebox.showerror("Incomplete Input", "Please fill all the values.")
        return

    number = int(number)
    print('items')
    for item in number_list:
        print(item)

    if any(int(item['Number']) == number for item in number_list):
        messagebox.showinfo("Number Exists", "Number {} already exists.".format(number))
    else:
        values = {'Number': number, 'Name': name, 'Prize': prize}
        #number_list.append(values)
        number_list.append(values)

        # Sort the dictionary based on the keys
        sorted_number_list = sorted(number_list,key=lambda d: int(d['Number']))
        print(sorted_number_list)
        update_csv_file(sorted_number_list)

        #with open(os.getcwd()+'\\data.csv', 'a', newline='') as csvfile:
        #    writer = csv.DictWriter(csvfile, fieldnames=['Number', 'Name', 'Prize'])
                        # Check if the CSV file is empty and write the header row if necessary
        #    if csvfile.tell() == 0:
        #        writer.writeheader()

        #    writer.writerow(values)
            

        messagebox.showinfo("Values Added", "Values have been added to the CSV file.")
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)

global number_list
number_list = []


# Read existing CSV file and populate the number_list dictionary
if os.path.exists(os.getcwd()+'\\data.csv'):
    with open(os.getcwd()+'\\data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile,restkey="Number",restval=['Name', 'Prize'])
        for row in reader:
            print(row)
            number_list.append(row)

        #number_list = dict(data)
    
print('starting gui')
window = tk.Tk()
window.geometry('250x280')
window.title("Prize Checker")

entry1 = tk.Entry(window)
entry1.pack(pady=5)
tk.Label(text='^ enter ticket number ^').pack()


entry2 = tk.Entry(window)
entry2.pack(pady=5)
tk.Label(text='^ enter student name ^').pack()

entry3 = tk.Entry(window)
entry3.pack(pady=5)
tk.Label(text='^ enter prize won ^').pack()

button = tk.Button(window, text="Add Winner + Prize to file", command= check_values, state=tk.DISABLED)
button.pack(pady=5)



open_button = tk.Button(window, text="Open file", command=open_csv_file)
open_button.pack(pady=5)

delbutton = tk.Button(window, text="< DELETE STUDENT/PRIZE from file> ", command= delete_row)
delbutton.pack(pady=10)



entry1.bind('<KeyRelease>', validate_entries)
entry2.bind('<KeyRelease>', validate_entries)
entry3.bind('<KeyRelease>', validate_entries)

window.mainloop()
