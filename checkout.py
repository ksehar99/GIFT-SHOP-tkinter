import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sys

def Check_out():
    def read_cart_items():
        items = []
        try:
            with open('temporary cart.txt', 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(' Pkr ')
                        if len(parts) == 2:
                            name_quantity, price_quantity = parts
                            price_quantity_parts = price_quantity.split(': ')
                            if len(price_quantity_parts) == 2:
                                total_price = int(price_quantity_parts[0].strip())
                                quantity = int(price_quantity_parts[1].strip())
                                name = name_quantity.strip()
                                unit_price = get_price(name)

                                items.append({
                                    "name": name,
                                    "quantity": quantity,
                                    "unit_price": unit_price,
                                    "total_price": total_price
                                })
            return items
        except FileNotFoundError:
            messagebox.showerror("Error", "Cart file not found.")
            return []
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return []

    def get_price(product_name):
        products = {
            'Smoky': 3000, 'Acorn': 3000, 'Musk': 2400, 'Dusk': 1200, 'Dawn': 2500,
            'Jeans': 5000, 'Shirt': 6000, 'Shoes': 7000, 'Joggers': 4000,
            'Denim': 9000,
            'Blue Crystal': 5000, 'Round Clock': 6000, 'Big Bang': 7000, 'Big Ben': 4000,
            'Pluto': 9000,
            'Bracelets': 5000, 'Amulets': 6000, 'Chains': 7000,
            'Rings': 4000, 'Silver Ring': 9000,
            'Vase': 5000, 'Abstract': 6000, 'Elevase': 7000, 'Glow': 4000,
            'Blue Bird': 9000,
            'Gone with the Wind': 5000, 'Sherlock Holmes': 6000, 'The Shadow of the Wind': 7000, 'Harry Potter Series': 4000,
            'Jane Eyre': 9000,
            'Pencil Box': 5000, 'Highlighters Set': 6000, 'Glue': 7000, 'Erasers': 4000,
            'Correction Pen': 9000,
            'Sneakers': 5000, 'Sandals': 6000, 'Customized Notebooks': 7000, 'Gift Baskets': 4000, 'Customized T-Shirts': 9000
        }
        return products.get(product_name, 0)

    def show_checkout(username):
        window = tk.Tk()
        window.title("Checkout")
        window.geometry('800x600+350+100')
        window.configure(bg="#f8f9fa")  # Light background color

        # Display current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        datetime_label = tk.Label(window, text=f"Date & Time:\n{current_datetime}", font=("Arial", 16, "bold"),
                                  bg="#f8f9fa", fg="#007bff")  # Stylish font and color
        datetime_label.pack(pady=20)

        # Create a frame for the checkout items
        checkout_frame = tk.Frame(window, bg="#f8f9fa")
        checkout_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Read the cart items and display them in a simplified format
        cart_items = read_cart_items()
        if not cart_items:
            empty_message = tk.Label(checkout_frame, text="Your cart is empty.", bg="#f8f9fa", font=("Arial", 14, "italic"))
            empty_message.pack(pady=20)
        else:
            total_price = 0.0
            for item in cart_items:
                item_label = tk.Label(checkout_frame, text=f"{item['name']} - Quantity: {item['quantity']} - Price: {item['unit_price']} - Total: {item['total_price']}",
                                      bg="#f8f9fa", font=("Arial", 12))
                item_label.pack(anchor='w', pady=5)
                total_price += item['total_price']

            payment_method_label = tk.Label(window, text="Payment Method: Cash on Delivery", font=("Arial", 14, "bold"), bg="#f8f9fa")
            payment_method_label.pack(pady=10)

            # Label to display the total price
            total_label = tk.Label(window, text=f"Total: Pkr {total_price}", font=("Arial", 16, "bold"), bg="#f8f9fa")
            total_label.pack(pady=20)

            # Confirm purchase button
            confirm_button = tk.Button(window, text="Confirm Purchase", command=lambda: confirm_purchase(cart_items, username, total_price),
                                       bg="#28a745", fg="white", font=("Arial", 14, "bold"), relief="raised")
            confirm_button.pack(pady=10)

        window.mainloop()

    # Confirm the purchase and save details to a file
    def confirm_purchase(cart_items, username, total_price):
        try:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            filename = f"{username}_{current_datetime}.txt"
            with open(filename, 'a') as file:
                file.write(f"Date & Time: {current_datetime}\n")
                file.write(f"{'Item':<30}{'Quantity':<10}{'Unit Price':<15}{'Total Price':<15}\n")
                file.write(f"{'-' * 70}\n")
                for item in cart_items:
                    file.write(f"{item['name']:<30}{item['quantity']:<10}{item['unit_price']:<15}{item['total_price']:<15}\n")
                file.write(f"\n{'Total':<55}{total_price:<15}\n")
                file.write("\n")
        except Exception as e:
            messagebox.showerror("Error", str(e))

        # Display thank you window
        display_thank_you_window()

    # Display a thank you window after purchase
    def display_thank_you_window():
        thank_you_window = tk.Tk()
        thank_you_window.title("Thank You")
        thank_you_window.geometry('400x200+500+300')
        thank_you_window.configure(bg="#f8f9fa")  # Light background color

        # Set window icon
        try:
            icon_img = tk.PhotoImage(file='icon.png')  # Load the icon image
            thank_you_window.iconphoto(True, icon_img)  # Set the icon for the window
        except Exception:
            pass

        # Customize the background and foreground of the labels
        thank_you_label = tk.Label(thank_you_window, text="Thank you for shopping!", font=("Arial", 24, "bold"),
                                   bg="#f8f9fa", fg="#007bff")
        thank_you_label.pack(pady=20)

        def safe_destroy():
            if thank_you_window.winfo_exists():
                thank_you_window.destroy()
                sys.exit()

        # Schedule the window to close after 3 seconds (3000 milliseconds)
        thank_you_window.after(3000, safe_destroy)
        thank_you_window.mainloop()

    # Call the show_checkout function with a username
    username = "example_user"
    show_checkout(username)
