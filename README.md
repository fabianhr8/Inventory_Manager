# inventoryManager
It's a GUI in python that manages a business inventory on a CSV file.

------------------
INVENTORY MANAGER
------------------

This code is a part of the Small Business Manager Software, it is used to add and substract quantities of the different
items on the inventory to keep track of the stock of each. It can also add new items and substract existing ones, or 
modify them. 

----------------
HOW DOES IT WORK
----------------

- The main window gives you the chance to "Check inventory", to "Modify quantities" or to "Modify items".
- If you choose "Check inventory" it will open another window that displays the actual inventory and the stock on each item.
- If you choose "Modify quantities" it will open another window in where you input the number of the item you want to 
modify, then select if you want to add (If there is new stock) or substract (If the item has been sold).
- If you choose "Modify items" you will have a window with 3 options: "Modify", "Add" or "Substract".
    --- If you choose "Modify" you have to input the number for the item you want to modify, then choose if you want to
    "Change name" or "Change price", the input the new name/price to change it.
    --- If you choose "Add" you will input the name and the price of the new item to add it to the inventory.
    --- If you choose "Delete" you will input the number of the item you want to delete.

- The inventory is stored in a CSV file with the name "inventoryList.csv" that has 5 columns:
1. Item number
2. Item name
3. Item price
4. Quantity of that item added
5. Quantity of that item substracted (if the item is sold)
6. Total quantity in stock for that item
