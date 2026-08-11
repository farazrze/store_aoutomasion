import sqlite3
my_data=sqlite3.connect("store.db")
store_cursor=my_data.cursor()
store_cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price INTEGER, stock INTEGER)")
store_cursor.execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT)")

class Product:
    def __init__(self,id,pd_name,price,stock):
        self.id=id
        self.pd_name=pd_name
        self.price=price
        self.stock=stock


class Store:

    def add_stock(self):
        pr_id=int(input("enter id of product: "))
        store_cursor.execute(f"SELECT stock FROM products WHERE id={pr_id}")
        num_of_stock=store_cursor.fetchall()
        new_stock=int(input("enter new stock of your product: "))+num_of_stock[0][0]
        store_cursor.execute(f"UPDATE products SET stock={new_stock} WHERE id={pr_id}")

    def add_product(self):
        name=input("enter name of your product: ")
        price=int(input("enter price of product: "))
        stock=int(input("enter first stock of your product: "))
        store_cursor.execute("INSERT OR IGNORE INTO products (name,price,stock) VALUES (?,?,?)",(name,price,stock))
        print("your product succesfully added.")
        my_data.commit()
        my_data.close

    def show_products(self):
        store_cursor.execute("SELECT * FROM products")
        pro=store_cursor.fetchall()
        for i in pro:
            print(i,sep="    ")

    def search_product(self):
        id_serach=int(input("enter id of product: "))
        store_cursor.execute(f"SELECT * FROM products WHERE ID={id_serach}")
        search_pr=store_cursor.fetchall()
        print(search_pr)

    def buy_product(self):
        pass



class Customers:
    def register(self):
        name=input("enter your name: ")
        phone=input("enter your phone number: ")
        store_cursor.execute("INSERT OR IGNORE INTO customers (name,phone) VALUES (?,?)",(name,phone))
        print("seccesfully save! ")
        my_data.commit()
        my_data.close




store=Store()
customers=Customers()


exit=True
while exit:
    info=int(input("1. Add product\n2. Show products\n3. Search product\n4. Add stock\n5. Register customer\n6. Buy product\n7. Exit "))

    if info==1:
        store.add_product()
    elif info==2:
        store.show_products()
    elif info==3:
        store.search_product()
    elif info==4:
        store.add_stock()
    elif info == 5:
        customers.register()
    elif info==6:
        store.buy_product()
    elif info==7:
        exit=False
    else:
        print("invalid input")


my_data.commit()
my_data.close