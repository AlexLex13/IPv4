import IPv4
import tkinter as tk


def submit():
    net = IPv4.IPAdress(entry_mask.get(), int(entry_number_of_networks.get()), int(entry_number_of_hosts.get()))
    print(net.info())
    print(net.subnet_mask())
    l_output_res = tk.Label(frame_output1, text=net.info())
    l_output_res.grid(column=0, row=0, padx=10, pady=10)


window = tk.Tk()
window.title('IPv4')

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

l_input_concrete_network = tk.Label(frame_input1, text='Enter a concrete subnet:')
l_input_concrete_network.grid(column=0, row=3, padx=10, pady=10)
entry_concrete_network = tk.Entry(frame_input1)
entry_concrete_network.grid(column=1, row=3, padx=10, pady=10)

l_input_concrete_host = tk.Label(frame_input1, text='Enter a concrete host:')
l_input_concrete_host.grid(column=0, row=4, padx=10, pady=10)
entry_concrete_host = tk.Entry(frame_input1)
entry_concrete_host.grid(column=1, row=4, padx=10, pady=10)

send_button = tk.Button(frame_input1, text='submit', command=submit)
send_button.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

window.mainloop()
