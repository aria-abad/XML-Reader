# This program is made to load the XML file and
# convert the Joint ROM (Range of Motion) Result from Radian to Degree
# and show the result on the GUI
# This program is made by Aria Abad

# Importing
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter import messagebox
import os
from math import degrees
from xml.etree import ElementTree

root = Tk()

# Called when an error happen
def error_message():
    messagebox.showerror(title = "Error", message = "Select another XML file")
# Help message
def help_message():
   messagebox.showinfo("About", "HIPT Joint ROM (Range of Motion) Result Reader, REV 0.2")
# Called when the user clicks the open file button
def open_file():
    try:
        # Open File Dialogs to load the XML file
        file = askopenfile(mode ='r', filetypes =[('xml Files', '*.xml')])  
        if file == None:
            return
        
        # Initialing the main window
        Label(content, text='          ', font=("Helvetica", 18)).grid(row=1, column=1, sticky=E)
        Label(content, text='          ', font=("Helvetica", 18)).grid(row=3, column=1, sticky=E)
        Label(content, text='          ', font=("Helvetica", 18)).grid(row=4, column=1, sticky=E)
        Label(content, text='          ', font=("Helvetica", 18)).grid(row=6, column=1, sticky=E)
        Label(content, text='          ', font=("Helvetica", 18)).grid(row=7, column=1, sticky=E)

        #Parse the file
        xml_elements = ElementTree.parse(file)
        # Find only elements with a TestRecord tag
        TestRecord = xml_elements.findall('TestRecord')
        # Use a for loop to find the measured data and convert them and show on main window
        for test_record in TestRecord:
            test_description = test_record.find('Test_Description').text
            if test_description == 'GripRom.pos_rom.dof.8':
                grip_rom = test_record.find('Results').text
                Label(content, text=str(round(degrees(float(grip_rom)), 1)) + " °", font=("Helvetica", 18, "bold")).grid(row=1, column=1, sticky=E)
            if test_description == 'JointRom.pos_rom.dof.6':
                pitch_pos = test_record.find('Results').text
                Label(content, text=str(round(degrees(float(pitch_pos)), 1)) + " °", font=("Helvetica", 18, "bold")).grid(row=3, column=1, sticky=E)
            if test_description == 'JointRom.neg_rom.dof.6':
                pitch_neg = test_record.find('Results').text
                Label(content, text=str(round(degrees(float(pitch_neg)), 1)) + " °", font=("Helvetica", 18, "bold")).grid(row=4, column=1, sticky=E)
            if test_description == 'JointRom.pos_rom.dof.7':
                yaw_pos = test_record.find('Results').text
                Label(content, text=str(round(degrees(float(yaw_pos)), 1)) + " °", font=("Helvetica", 18, "bold")).grid(row=6, column=1, sticky=E)
            if test_description == 'JointRom.neg_rom.dof.7':
                yaw_neg = test_record.find('Results').text
                Label(content, text=str(round(degrees(float(yaw_neg)), 1)) + " °", font=("Helvetica", 18, "bold")).grid(row=7, column=1, sticky=E)

    except:
        error_message()

#Set up the main window
root.title("HIPT")
root.resizable(False, False)
content = Frame(root)

#Set up the menubar
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Open", command = open_file)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = root.destroy)
menubar.add_cascade(label = "File", menu = filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "About...", command = help_message)
menubar.add_cascade(label = "Help", menu = helpmenu)
root.config(menu = menubar)

load_button = Button(content, text='Load File', width=30, command = lambda:open_file())
grip_rom_label = Label(content, text="GRIP ROM", font=("Arial Bold", 9))
seperator1 = Separator(content, orient=HORIZONTAL)
positive_pitch_rom_label = Label(content, text="POSITIVE PITCH ROM", font=("Arial Bold", 9))
negative_pitch_rom_label = Label(content, text="NEGATIVE PITCH ROM", font=("Arial Bold", 9))
seperator2 = Separator(content, orient=HORIZONTAL)
positive_yaw_rom_label = Label(content, text="POSITIVE YAW ROM", font=("Arial Bold", 9))
negative_yaw_rom_label = Label(content, text="NEGATIVE YAW ROM", font=("Arial Bold", 9))
exit_button = Button(content, text='Exit', width=30, command = root.destroy)


content.grid(row=0, column=0, sticky=(N, S, E, W))
load_button.grid(row=0, column=0, columnspan=3)
grip_rom_label.grid(row=1, column=0, sticky=W)
seperator1.grid(row=2, column=0, columnspan=3, sticky=(E, W))
positive_pitch_rom_label.grid(row=3, column=0, sticky=W)
negative_pitch_rom_label.grid(row=4, column=0, sticky=W)
seperator2.grid(row=5, column=0, columnspan=3, sticky=(E, W))
positive_yaw_rom_label.grid(row=6, column=0, sticky=W)
negative_yaw_rom_label.grid(row=7, column=0, sticky=W)
exit_button.grid(row=8, column=0, columnspan=3)

#Put some nice finishing touches on our user interface
for child in content.winfo_children(): child.grid_configure(padx=10, pady=10)

#Tell Tk to enter its event loop, which is needed to make everything run
root.mainloop()