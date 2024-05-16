import tkinter as tk

class SupermarketSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Supermarket System")
        self.current_page = "main"
        self.cart = []
        self.create_widgets()

    def create_widgets(self):
        if self.current_page == "main":
            self.main_menu()
        elif self.current_page == "shop":
            self.shop_menu()
        elif self.current_page == "category":
            self.category_menu()

    def main_menu(self):
        self.clear_screen()

        self.master.configure(bg="#FFD700")
        tk.Label(self.master, text="HELLO WELCOME TO AISHA GROCERY STORE🤗😊👍🤞", font=("Arial", 16), bg="#FFD700").pack(pady=10)

        tk.Button(self.master, text="Shop", command=self.go_to_shop, width=20, height=2).pack(pady=5)
        tk.Button(self.master, text="Pay", command=self.pay, width=20, height=2).pack(pady=5)
        tk.Button(self.master, text="Cart", command=self.view_cart, width=20, height=2).pack(pady=5)
        tk.Button(self.master, text="Exit", command=self.exit_system, width=20, height=2).pack(pady=5)

    def shop_menu(self):
        self.clear_screen()

        self.master.configure(bg="#90EE90")
        tk.Label(self.master, text="Select a category:", font=("Arial", 16), bg="#90EE90").pack(pady=10)

        tk.Button(self.master, text="Vegetables", command=lambda: self.go_to_category("vegetables"), width=20, height=2).pack(pady=5)
        tk.Button(self.master, text="Fruits", command=lambda: self.go_to_category("fruits"), width=20, height=2).pack(pady=5)
        tk.Button(self.master, text="Snacks", command=lambda: self.go_to_category("snacks"), width=20, height=2).pack(pady=5)
        tk.Button(self.master, text="Drinks", command=lambda: self.go_to_category("drinks"), width=20, height=2).pack(pady=5)
        tk.Button(self.master, text="Exit", command=self.exit_system, width=20, height=2).pack(pady=5)

    def category_menu(self):
        self.clear_screen()

        self.master.configure(bg="#ADD8E6")
        tk.Label(self.master, text=f"Select a product from {self.current_category}:", font=("Arial", 16), bg="#ADD8E6").pack(pady=10)

        products = self.get_products_for_category(self.current_category)
        for product, price in products:
            tk.Button(self.master, text=f"{product} - ${price}", command=lambda p=product, pr=price: self.add_to_cart(p, pr), width=20, height=2).pack(pady=5)

        tk.Button(self.master, text="Back to Shop", command=self.go_to_shop, width=20, height=2).pack(pady=5)
        tk.Button(self.master, text="Exit", command=self.exit_system, width=20, height=2).pack(pady=5)

    def add_to_cart(self, product, price):
        self.cart.append((product, price))
        self.view_cart()

    def view_cart(self):
        self.clear_screen()

        self.master.configure(bg="#FFA07A")
        tk.Label(self.master, text="Your Cart:", font=("Arial", 16), bg="#FFA07A").pack(pady=10)

        total = 0
        for product, price in self.cart:
            tk.Label(self.master, text=f"{product} - ${price}", bg="#FFA07A").pack()
            total += price

        tk.Label(self.master, text=f"Total: ${total}", font=("Arial", 14), bg="#FFA07A").pack()

        tk.Button(self.master, text="Back to Main Menu", command=self.main_menu, width=20, height=2).pack(pady=5)
        tk.Button(self.master, text="Exit", command=self.exit_system, width=20, height=2).pack(pady=5)

    def go_to_shop(self):
        self.current_page = "shop"
        self.create_widgets()

    def go_to_category(self, category):
        self.current_page = "category"
        self.current_category = category
        self.create_widgets()

    def pay(self):
       
        print("Payment functionality not implemented yet")

    def exit_system(self):
        self.clear_screen()
        tk.Label(self.master, text="Buy next time with us!", font=("Arial", 16), bg="#FF6347").pack(pady=10)

    def clear_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def get_products_for_category(self, category):
      
        if category == "vegetables":
            return [("Carrot", 1.5), ("Tomato", 2.0), ("Broccoli", 1.8)]
        elif category == "fruits":
            return [("Apple", 0.5), ("Banana", 0.3), ("Orange", 0.4)]
        elif category == "snacks":
            return [("Chips", 2.5), ("Pringles", 3.0), ("Biscruits", 1.8)]
        elif category == "drinks":
            return [("Water", 1.0), ("Soda", 1.5), ("Juice", 2.0)]

def main():
    root = tk.Tk()
    app = SupermarketSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()
