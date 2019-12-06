from tkinter import *
import csv
import os

inventory_list = 'inventory_list.csv'           # Archivo CSV de inventario

class Main():        # Main Window

    def __init__(self, master):             # Definir configuraciones

        self.master = master
        master.geometry('280x120')
        master.title('Inventory Manager')  # Titulo de la ventana

        self.container = Frame(self.master)                                     # Main layout
        self.container.pack()

        self.what_to_do_label = Label(self.container, text='What do you want to do to inventory?')
        self.what_to_do_label.pack()

        self.check_inv_button = Button(self.container, text='Check inventory', command= lambda:self.Check_inv())    
        self.check_inv_button.pack()
        self.mod_qty_button = Button(self.container, text='Modify quantities', command= lambda:self.Modify_qty())  
        self.mod_qty_button.pack()
        self.mod_items_button = Button(self.container, text='Modify items', command= lambda:self.Modify_items())  
        self.mod_items_button.pack()

    def Check_inv(self):                                                             # Check inventory

        newWindow = Toplevel(self.master)
        app = Window_check_inv(newWindow)
        
    def Modify_qty(self):                                                               # Add/Substract to inventory

        newWindow = Toplevel(self.master)
        app = Window_mod_qty(newWindow)

    def Modify_items(self):                                                               # Change items name/price

        newWindow = Toplevel(self.master)
        app = Window_mod_items(newWindow)


class Window_check_inv(Frame):                                                  # See complete inventory

    def __init__(self, master):

        Frame.__init__(self, master)
        self.master = master
        self.master.title('Inventory')
        #self.master.geometry('%dx%d+%d+%d' % (600, 600, 500, 100))        

        self.frame0 = Frame(self.master)
        self.frame0.grid()

        self.number_label = Label(self.master, text=" Number ")            # Info of products
        self.number_label.grid(row=0, column=0)
        self.name_label = Label(self.master, text=" Name ")
        self.name_label.grid(row=0, column=1)
        self.added_label = Label(self.master, text=" Added ")  
        self.added_label.grid(row=0, column=2)
        self.deleted_label = Label(self.master, text=" Deleted ")  
        self.deleted_label.grid(row=0, column=3)
        self.on_stock_label = Label(self.master, text=" On stock ")  
        self.on_stock_label.grid(row=0, column=4)
        self.separation_label = Label(self.master, text="---------------------------------------------------------")
        self.separation_label.grid(row=1, columnspan=5)

        with open(inventory_list, 'r') as lista_inv:

            self.lista = csv.reader(lista_inv.readlines())
            line_num = 2

            for row in self.lista:                                                        # Display all products
                self.codigo_prod_label = Label(self.master, text=row[0])   
                self.codigo_prod_label.grid(row=line_num, column=0, sticky=W)
                self.nombre_prod_label = Label(self.master, text=row[1])
                self.nombre_prod_label.grid(row=line_num, column=1, sticky=W)
                self.entraron_prod_label = Label(self.master, text=row[3])  
                self.entraron_prod_label.grid(row=line_num, column=2)
                self.salieron_prod_label = Label(self.master, text=row[4])  
                self.salieron_prod_label.grid(row=line_num, column=3)
                self.en_inv__prod_label = Label(self.master, text=row[5])  
                self.en_inv__prod_label.grid(row=line_num, column=4)
                line_num += 1


class Window_mod_qty(Frame):            # Add to inventory or Substract from inventory

    def __init__(self, master):
        
        Frame.__init__(self, master)
        self.master = master
        self.master.title('Modify inventory')
        self.master.geometry('%dx%d+%d+%d' % (220, 350, 500, 100))     

        menu_mod_qty = Menu(self.master)                           # Top menu
        master.config(menu = menu_mod_qty)
        menu_mod_qty.add_command(label='Check inventory', command = lambda: self.CheckInv())

        self.frame0 = Frame(self.master)          # By putting widgets in the frame we can later restore it to choose another item
        self.frame0.pack()

        self.choose_item_label = Label(self.frame0, text='Which item would you like to modify:')
        self.choose_item_label.pack()
        self.chosen_item_entry = Entry(self.frame0)
        self.chosen_item_entry.pack()
        self.choose_item_button = Button(self.frame0, text='Choose', command = lambda: self.item_chosen())
        self.choose_item_button.pack()

    def item_chosen(self):

        self.chosen_item = int(self.chosen_item_entry.get())
        self.chosen_item_text = 'Item chosed: ' + str(self.chosen_item)

        self.frame1 = Frame(self.master)
        self.frame1.pack()

        self.chosen_item_label = Label(self.frame1, text = self.chosen_item_text)
        self.chosen_item_label.pack()
        self.separation_label = Label(self.frame1, text = '')                    # Empty space
        self.separation_label.pack()
        self.add_or_erase_label = Label(self.frame1, text = 'What to do with that item?')
        self.add_or_erase_label.pack()
        self.add_boton = Button(self.frame1, text = 'Add', command = lambda: self.choose_quantity('A'))
        self.add_boton.pack(side=LEFT)
        self.substract_boton = Button(self.frame1, text = 'Substract', command = lambda: self.choose_quantity('S'))
        self.substract_boton.pack(side=RIGHT)

    def choose_quantity(self, add_or_sub):

        self.if_exists = 0                              # Used to check if item exists in inventory

        with open(inventory_list, 'r') as inv_r:                   # Get info from inventory's CSV file
            self.inv_reader = csv.reader(inv_r.readlines())
            inv_r.close()

            self.frame2 = Frame(self.master)
            self.frame2.pack()

        if add_or_sub == 'A':                                      # If "Add" was chosen
            self.modified_qty_label = Label(self.frame2, text='What quantity will you add?')
            self.modified_qty_label.pack()
            self.modified_qty_entry = Entry(self.frame2)
            self.modified_qty_entry.pack()
            self.modified_qty_button = Button(self.frame2, text='Choose', command = lambda: self.add_qty())
            self.modified_qty_button.pack()

        elif add_or_sub == 'S':                                    # If "Substract" was chosen
            self.modified_qty_label = Label(self.frame2, text='What quantity will you substract?')
            self.modified_qty_label.pack()
            self.modified_qty_entry = Entry(self.frame2)
            self.modified_qty_entry.pack()
            self.modified_qty_button = Button(self.frame2, text='Choose', command = lambda: self.substract_qty())
            self.modified_qty_button.pack()

    def add_qty(self):                                          # If you will add quantity of an item

        self.qty_added = int(self.modified_qty_entry.get())                     # Get quantity that will be added  

        with open(inventory_list, 'w', newline='') as inv_w: 
            inv_writer = csv.writer(inv_w)

            for row in self.inv_reader:
                if int(row[0]) == self.chosen_item:            # When item is found on inventory, make modifications
                    self.if_exists = 1                      
                    new_qty = int(row[3]) + int(self.qty_added)  
                    row[3] = str(new_qty)    
                    row[5] = str(int(row[3]) - int(row[4]))  

                    inv_writer.writerow(row)

                else:

                    inv_writer.writerow(row)       

            inv_w.close()
            self.another_item()

        if self.if_exists == 0:                                     # If item's code doesn't exist
            print('Item does not exist')
            inv_w.close()

    def substract_qty(self):                                        # If you will substract quantity from an item

        self.qty_substracted = int(self.modified_qty_entry.get())           # Get quantity that will be substracted

        with open(inventory_list, 'w', newline='') as inv_w:  
            inv_writer = csv.writer(inv_w)

            for row in self.inv_reader:
                if int(row[0]) == self.chosen_item:            # When item is found on inventory, make modifications
                    self.if_exists = 1    
                    new_qty = int(row[4]) + int(self.qty_substracted)  
                    row[4] = str(new_qty)  
                    row[5] = str(int(row[3]) - int(row[4])) 

                    inv_writer.writerow(row)         

                else:
                    inv_writer.writerow(row)              

            inv_w.close()
            self.another_item()

        if self.if_exists == 0:                                              # If item's code doesn't exist
            print('Item does not exist')
            inv_w.close()

    def another_item(self):                            # If the user wants to modify another item

        self.frame3 = Frame(self.master)
        self.frame3.pack()

        self.confirm_modification_label = Label(self.frame3, text='Done!')
        self.confirm_modification_label.pack()
        self.separation_label = Label(self.frame3, text='')
        self.separation_label.pack()
        self.modify_another_label = Label(self.frame3, text='Modify another item?')
        self.modify_another_label.pack()
        self.yes_modify_another_button = Button(self.frame3, text='Yes', command = lambda: self.select_another())
        self.yes_modify_another_button.pack()
        self.no_modify_another_button = Button(self.frame3, text='No', command = lambda: self.exit_window())
        self.no_modify_another_button.pack()

    def select_another(self):                      # Erase everything and set it up again to modify another item

        self.frame0.destroy()
        self.frame1.destroy()  
        self.frame2.destroy()
        self.frame3.destroy()
        self.__init__(self.master)                  # Launch window again

    def CheckInv(self):                                                             # Check inventory

        newWindow = Toplevel(self.master)
        app = Window_check_inv(newWindow)

    def exit_window(self):                 # Don't modify another item. Close window

        self.after(2000, self.master.destroy())


class Window_mod_items(Frame):
######################################### FALTA ADD Y SUBSTRACT PARA AGREGAR O BORRAR OTRO
    def __init__(self, master):
        
        Frame.__init__(self, master)
        self.master = master
        self.master.title('Modify items')
        self.master.geometry('%dx%d+%d+%d' % (300, 550, 500, 80))  # Size and location of window (w,h,x,y)
        
        menu_mod_items = Menu(self.master)                           # Top menu
        master.config(menu = menu_mod_items)
        menu_mod_items.add_command(label='Check inventory', command = lambda: self.CheckInv())

        self.frame0 = Frame(self.master)  
        self.frame0.pack()

        self.choose_action_label = Label(self.frame0, text='What do you wish to do?')
        self.choose_action_label.pack()
        self.mod_item_button = Button(self.frame0, text='Modify', command = lambda: self.choose_item())
        self.mod_item_button.pack()
        self.add_item_button = Button(self.frame0, text='Add', command = lambda: self.add_item())
        self.add_item_button.pack()
        self.del_item_button = Button(self.frame0, text='Delete', command = lambda: self.del_item())
        self.del_item_button.pack()

    def choose_item(self):

        self.frame1 = Frame(self.master)        
        self.frame1.pack()

        self.choose_item_label = Label(self.frame1, text='Select number of file to modify:')
        self.choose_item_label.pack()
        self.chosen_item_entry = Entry(self.frame1)
        self.chosen_item_entry.pack()
        self.choose_item_boton = Button(self.frame1, text='Choose', command = lambda: self.chosen_item())
        self.choose_item_boton.pack()

    def chosen_item(self):

        self.chosen_item_num = int(self.chosen_item_entry.get()) 
        self.chosen_item_text = 'Item: ' + str(self.chosen_item_num)

        with open(inventory_list, 'r') as inv_r:                           # Read inventory's CSV file
            self.inv_reader = csv.reader(inv_r.readlines())
            inv_r.close()

            for row in self.inv_reader:                                             # Obtener el articulo elegido y su precio
                if int(row[0]) == self.chosen_item_num:
                    self.chosen_item_name = 'Item: ' + row[1]
                    self.chosen_item_price = 'Price: $' + row[2]

        self.frame2 = Frame(self.master)                    # Frame2
        self.frame2.pack()

        self.chosen_item_label = Label(self.frame2, text = self.chosen_item_text)
        self.chosen_item_label.pack()
        self.chosen_name_label = Label(self.frame2, text=self.chosen_item_name)
        self.chosen_name_label.pack()
        self.chosen_price_label = Label(self.frame2, text=self.chosen_item_price)
        self.chosen_price_label.pack()
        self.separation_label = Label(self.frame2, text = '')   
        self.separation_label.pack()
        self.price_or_name_label = Label(self.frame2, text = 'What do you wish to do?')
        self.price_or_name_label.pack()
        self.change_name_boton = Button(self.frame2, text = 'Change name', command = lambda: self.change_name())
        self.change_name_boton.pack()
        self.change_price_boton = Button(self.frame2, text='Change price', command = lambda: self.change_price())
        self.change_price_boton.pack()

    def change_name(self):

        self.frame3 = Frame(self.master)
        self.frame3.pack()

        self.new_name_label = Label(self.frame3, text='What would be the new name?')
        self.new_name_label.pack()
        self.new_name_entry = Entry(self.frame3)   
        self.new_name_entry.pack()
        self.new_name_button = Button(self.frame3, text='Choose', command = lambda: self.set_new_name())
        self.new_name_button.pack()

    def set_new_name(self):

        self.new_name = str(self.new_name_entry.get())             # Get new name fro entry

        with open(inventory_list, 'r') as inv_r:
            self.inv_reader = csv.reader(inv_r.readlines())

        with open(inventory_list, 'w', newline='') as inv_w:  
            self.inv_writer = csv.writer(inv_w)

            for row in self.inv_reader:

                if int(row[0]) == self.chosen_item_num:             # Get correct row of item
                    row[1] = self.new_name    
                    self.inv_writer.writerow(row) 

                else:
                    self.inv_writer.writerow(row)               # Write ther rest of the rows in the inventory file

            self.confirm_modification_label = Label(self.frame3, text='Done!')
            self.confirm_modification_label.pack()

            inv_w.close()
            inv_r.close()

            #self.after(2000, self.close_window())
            self.another_item()

    def change_price(self):

        self.frame3 = Frame(self.master)  # Frame3
        self.frame3.pack()

        self.new_price_label = Label(self.frame3, text='What is the new price?')
        self.new_price_label.pack()
        self.new_price_entry = Entry(self.frame3)   
        self.new_price_entry.pack()
        self.new_price_button = Button(self.frame3, text='choose', command = lambda: self.set_new_price())
        self.new_price_button.pack()

    def set_new_price(self):

        self.new_price = int(self.new_price_entry.get())        # Get new price from entry

        with open(inventory_list, 'r') as inv_r:
            self.inv_reader = csv.reader(inv_r.readlines())

        with open(inventory_list, 'w', newline='') as inv_w:  
            self.inv_writer = csv.writer(inv_w)

            for row in self.inv_reader:

                if int(row[0]) == self.chosen_item_num:             # Get correct row of item
                    row[2] = str(self.new_price)  
                    self.inv_writer.writerow(row) 

                else:
                    self.inv_writer.writerow(row)               # Write ther rest of the rows in the inventory file

            inv_w.close()
            inv_r.close()

            self.another_item()

    def add_item(self):

        self.frame1 = Frame(self.master)
        self.frame1.pack()

        self.new_item_name_label = Label(self.frame1, text='Name of new item:')
        self.new_item_name_label.pack()
        self.new_item_name_entry = Entry(self.frame1)
        self.new_item_name_entry.pack()
        self.new_item_price_label = Label(self.frame1, text='Price of new item:')
        self.new_item_price_label.pack()
        self.new_item_price_entry = Entry(self.frame1)
        self.new_item_price_entry.pack()
        self.add_new_item_button = Button(self.frame1, text='Add', command = lambda: self.add_new_item())
        self.add_new_item_button.pack()

    def add_new_item(self):

        self.new_item_name_text = str(self.new_item_name_entry.get())        # Get name and price of new item form entry
        self.new_item_price_text = str(self.new_item_price_entry.get()) 

        counter = 1                                                      # Used to count the number of items on inventory
        new_row = ''

        with open(inventory_list, 'r') as inv_r:
            self.inv_reader = csv.reader(inv_r.readlines())

        with open(inventory_list,'a', newline='') as inv_a:                       # There's no need to erease everything with 'W'
            self.inv_append = csv.writer(inv_a)

            for row in self.inv_reader:                 # Increase counter until it is 1 more that the items of the inv.

                counter += 1

            if counter >= 10:                   # For items number greater than 9

                self.new_item_num_text = '0' + str(counter)

            else:

                self.new_item_num_text = '00' + str(counter)

            new_row = [self.new_item_num_text, self.new_item_name_text, self.new_item_price_text, 0, 0, 0]
            self.inv_append.writerow(new_row)               # Add new row to the end of inventory

            inv_r.close()
            inv_a.close()

            self.another_item_for_add_del()

    def del_item(self):

        self.frame1 = Frame(self.master)
        self.frame1.pack()

        self.item_to_del_label = Label(self.frame1, text='Select code of item that will be deleted:')
        self.item_to_del_label.pack()
        self.item_to_del_entry = Entry(self.frame1)
        self.item_to_del_entry.pack()
        self.item_to_del_button = Button(self.frame1, text='Delete item', command = lambda: self.del_selected_item())
        self.item_to_del_button.pack()

    def del_selected_item(self):

        self.item_to_del = int(self.item_to_del_entry.get())              # Get number of item that will be deleted
        self.item_to_del_text = 'Codigo elegido: ' + str(self.item_to_del)

        counter = 1                             # This will make sure that item's codes will always be consecutive

        with open(inventory_list, 'r') as inv_r:          
            self.inv_reader = csv.reader(inv_r.readlines())

        with open(inventory_list, 'w', newline='') as inv_w: 
            self.inv_writer = csv.writer(inv_w)

            for row in self.inv_reader:            # Write all rows on file, except the one that was deleted

                if int(row[0]) != self.item_to_del:

                    if counter >= 10:                   # For items number greater than 9

                        row[0] = '0' + str(counter)    
                        self.inv_writer.writerow(row)  
                        counter += 1

                    else:

                        row[0] = '00' + str(counter)        # Add to inventory the items from 0 to 9 
                        self.inv_writer.writerow(row)  
                        counter += 1

            inv_r.close()
            inv_w.close()

            self.another_item_for_add_del()

    def CheckInv(self):                                                             # Check inventory

        newWindow = Toplevel(self.master)
        app = Window_check_inv(newWindow)

    def another_item(self):                            # If the user wants to modify another item

        self.frame4 = Frame(self.master)
        self.frame4.pack()

        self.confirm_modification_label = Label(self.frame4, text='Done!')
        self.confirm_modification_label.pack()
        self.separation_label = Label(self.frame4, text='')
        self.separation_label.pack()
        self.modify_another_label = Label(self.frame4, text='Modify another item?')
        self.modify_another_label.pack()
        self.yes_modify_another_button = Button(self.frame4, text='Yes', command = lambda: self.select_another())
        self.yes_modify_another_button.pack()
        self.no_modify_another_button = Button(self.frame4, text='No', command = lambda: self.exit_window())
        self.no_modify_another_button.pack()


    def another_item_for_add_del(self):                            # If the user wants to modify another item

        self.frame2 = Frame(self.master)
        self.frame2.pack()

        self.confirm_modification_label = Label(self.frame2, text='Done!')
        self.confirm_modification_label.pack()
        self.separation_label = Label(self.frame2, text='')
        self.separation_label.pack()
        self.modify_another_label = Label(self.frame2, text='Modify another item?')
        self.modify_another_label.pack()
        self.yes_modify_another_button = Button(self.frame2, text='Yes', command = lambda: self.select_another_for_add_del())
        self.yes_modify_another_button.pack()
        self.no_modify_another_button = Button(self.frame2, text='No', command = lambda: self.exit_window())
        self.no_modify_another_button.pack()

    def select_another(self):                      # Erase everything and set it up again to modify another item

        self.frame0.destroy()
        self.frame1.destroy()  
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()
        self.__init__(self.master)                  # Launch window again

    def select_another_for_add_del(self):                      # Erase everything and set it up again to modify another item

        self.frame0.destroy()
        self.frame1.destroy()  
        self.frame2.destroy()
        self.__init__(self.master)                  # Launch window again

    def exit_window(self):                 # Don't modify another item. Close window

        self.after(2000, self.master.destroy())



root = Tk()                                        # Create root windoe
root.bind("<Escape>", lambda e: root.quit())           # Close root by pressing 'ESC'  
cls = Main(root)
root.mainloop()                             # Start Mainloop