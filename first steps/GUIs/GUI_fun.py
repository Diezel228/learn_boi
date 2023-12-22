import PySimpleGUI as sg

layout = [[sg.Text("Hello from PySimpleGUI")],[sg.Button("OK")]]

#Create the window 
window = sg.Window("Demo", layout)

#Create event loop
while True:
    event, values = window.read()
    #end program if user closes window or
    #presses the OK button
    if event =="OK" or event == sg.WIN_CLOSED:
        break
window.close()
#sg.Window(title="Hello, World!;lkjhgf", layout=[[]], margins=(11, 50)).read()