import IPv4
import tkinter as tk
from tkinter import messagebox


def submit1():
    try:
        net = IPv4.IPAdress(entry_mask.get(), int(entry_number_of_networks.get()), int(entry_number_of_hosts.get()))
    except ValueError:
        messagebox.showerror(message=f'Number_of_networks and number_of_hosts must be numbers!')
    except IPv4.WrongFormat as WF:
        messagebox.showerror(message=WF)
    except IPv4.SpecialAdress as SA:
        messagebox.showerror(message=SA)
    except IPv4.NetworkNotExist as NNE:
        messagebox.showerror(message=NNE)
    else:
        l_output_res = tk.Label(frame_output1, text=f"{net.info()}\n{net.subnet_mask()}")
        l_output_res.grid(column=0, row=0, padx=10, pady=10)

        frame_input2 = tk.Frame(window, bg='green')
        frame_input2.grid(column=0, row=2, sticky='we')

        l_input_concrete_network = tk.Label(frame_input2, text='Enter a concrete subnet:')
        l_input_concrete_network.grid(column=0, row=0, padx=10, pady=10)
        entry_concrete_network = tk.Entry(frame_input2)
        entry_concrete_network.grid(column=1, row=0, padx=10, pady=10)

        l_input_concrete_host = tk.Label(frame_input2, text='Enter a concrete host:')
        l_input_concrete_host.grid(column=0, row=1, padx=10, pady=10)
        entry_concrete_host = tk.Entry(frame_input2)
        entry_concrete_host.grid(column=1, row=1, padx=10, pady=10)

        def submit2():
            frame_output2 = tk.Frame(window, bg='red')
            frame_output2.grid(column=0, row=3, sticky='we')
            try:
                if int(entry_concrete_network.get()) > int(entry_number_of_networks.get()) or \
                        int(entry_concrete_host.get()) > int(entry_number_of_hosts.get()):
                    raise IPv4.WrongNumber

                l_output_res2 = tk.Label(frame_output2, text=net.concrete_adress(int(entry_concrete_network.get()),
                                                                                 int(entry_concrete_host.get())))
            except ValueError:
                messagebox.showerror(message=f'Concrete_subnet and concrete_host must be numbers!')
            except IPv4.WrongNumber as WN:
                messagebox.showerror(message=WN)
            else:
                l_output_res2.grid(column=0, row=0, padx=10, pady=10)

        send_button2 = tk.Button(frame_input2, text='submit2', command=submit2)
        send_button2.grid(column=0, row=2, columnspan=2, padx=10, pady=10)


window = tk.Tk()
window.title('IPv4')
window.resizable(width=False, height=False)

frame_input1 = tk.Frame(window, bg='blue')
frame_output1 = tk.Frame(window, bg='yellow')
frame_input1.grid(column=0, row=0, sticky='we')
frame_output1.grid(column=0, row=1, sticky='we')

l_input_adress = tk.Label(frame_input1, text='Enter the network in the given format X.X.X.X:')
l_input_adress.grid(column=0, row=0, padx=10, pady=10)
entry_mask = tk.Entry(frame_input1)
entry_mask.grid(column=1, row=0, padx=10, pady=10)

l_input_number_of_networks = tk.Label(frame_input1, text='Enter number of subnets:')
l_input_number_of_networks.grid(column=0, row=1, padx=10, pady=10)
entry_number_of_networks = tk.Entry(frame_input1)
entry_number_of_networks.grid(column=1, row=1, padx=10, pady=10)

l_input_number_of_hosts = tk.Label(frame_input1, text='Enter number of hosts:')
l_input_number_of_hosts.grid(column=0, row=2, padx=10, pady=10)
entry_number_of_hosts = tk.Entry(frame_input1)
entry_number_of_hosts.grid(column=1, row=2, padx=10, pady=10)

send_button1 = tk.Button(frame_input1, text='submit', command=submit1)
send_button1.grid(column=0, row=3, columnspan=2, padx=10, pady=10)

window.mainloop()
