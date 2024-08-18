from tkinter import Tk, PhotoImage, Label, Frame, Button, Entry
from PIL import Image, ImageTk
from Buttons import back
from products_menu import prd_menu

def open_create_wind(main_wind):
    main_wind.destroy()

    create_wind = Tk()
    create_wind['background'] = '#F5F5DC'
    create_wind.title('S&K Gift Shop-Signin')
    create_wind.geometry('550x650+20+50')

    gap_lab = Label(create_wind, text='\n', bg='#F5F5DC')
    gap_lab.pack()

    # create a frame to manage other frames
    frame1 = Frame(create_wind, highlightbackground="#800000", bg='#F5F5DC', highlightthickness=2)
    frame1.pack()

    img_frame = Frame(frame1, bg='#F5F5DC')
    img_frame.pack(pady=15)

    # set title image
    img = Image.open('GIFT SHOP.png')
    resized_img = img.resize((200, 200))

    # Convert PIL Image to Tkinter PhotoImage
    photo_image = ImageTk.PhotoImage(resized_img)

    # Attach PhotoImage to a persistent object to prevent from garbage collector
    create_wind.photo = photo_image

    # Create a label to display the image
    image_label = Label(img_frame, image=photo_image, bg='#F5F5DC')
    image_label.pack(side='left', padx=5)

    lab1 = Label(img_frame, text="\nReady to elevate your shopping\n experience? Sign up now!",
                 font=('Helvetica', 14, 'bold'), bg='#F5F5DC', fg="#800000")
    lab1.pack(side='right')

    # create frame for username
    frame2 = Frame(frame1, bg='#F5F5DC')
    frame2.pack()

    # create label and entry box for username
    lab2 = Label(frame2, text='Username:', font="Times", bg='#F5F5DC')
    lab2.pack(side='left', padx=10, pady=10)
    entry_username = Entry(frame2, width=30, bg='#F5F5DC')
    entry_username.pack(side='right', padx=10, pady=10)

    # error label, if username is already in use
    error_frame1 = Frame(frame1, bg='#F5F5DC')
    error_frame1.pack()
    name_error_lab = Label(error_frame1, text='Sorry!!! Username Already Exists!', bg='#F5F5DC', fg='red')
    empty_name_error_lab = Label(error_frame1, text='Please, enter your name', bg='#F5F5DC', fg='red')

    # create frame for password
    frame3 = Frame(frame1, bg='#F5F5DC')
    frame3.pack()

    # create label and entry box for password
    lab3 = Label(frame3, text='Password:', font="Times",  bg='#F5F5DC')
    lab3.pack(side='left', padx=10, pady=10)
    entry_password = Entry(frame3, width=30,  bg='#F5F5DC', show="*")
    entry_password.pack(side='right', padx=10, pady=10)

    # error label, if password not meet all the conditions
    error_frame2 = Frame(frame1, bg='#F5F5DC')
    error_frame2.pack()
    pass_len_error_lab = Label(error_frame2, text='password must contain 8 characters', bg='#F5F5DC', fg='red')
    pass_digit_error_lab = Label(error_frame2, text='password must contain at least 1 digit', bg='#F5F5DC', fg='red')
    empty_pass_error_lab = Label(error_frame2, text='Please, enter your password', bg='#F5F5DC', fg='red')

    # create frame for address
    frame4 = Frame(frame1, bg='#F5F5DC')
    frame4.pack()

    # create label and entry box for address
    lab4 = Label(frame4, text='Address:', font="Times", bg='#F5F5DC')
    lab4.pack(side='left', padx=10, pady=10)
    entry_address = Entry(frame4, width=30, bg='#F5F5DC')
    entry_address.pack(side='right', padx=10, pady=10)

    # error label, if address not meet all the conditions
    error_frame3 = Frame(frame1, bg='#F5F5DC')
    error_frame3.pack()
    add_digit_error_lab = Label(error_frame3, text='address must contain house or flat number', bg='#F5F5DC', fg='red')
    add_alpha_error_lab = Label(error_frame3, text='address must contain area name', bg='#F5F5DC', fg='red')
    empty_add_error_lab = Label(error_frame3, text='Please, enter your address', bg='#F5F5DC', fg='red')

    # create frame for contact
    frame5 = Frame(frame1, bg='#F5F5DC')
    frame5.pack()

    # create label and entry box for contact
    lab5 = Label(frame5, text='Contact:', font="Times", bg='#F5F5DC')
    lab5.pack(side='left', padx=10, pady=10)
    entry_contact = Entry(frame5, width=30, bg='#F5F5DC')
    entry_contact.pack(side='right', padx=10, pady=10)

    # error label, if contact not meet all the conditions
    error_frame4 = Frame(frame1, bg='#F5F5DC')
    error_frame4.pack()
    empty_cont_error_lab = Label(error_frame4, text='Please enter your contact number', bg='#F5F5DC', fg='red')
    cont_len_error_lab = Label(error_frame4, text='Please enter correct contact number', bg='#F5F5DC', fg='red')
    cont_alpha_error_lab = Label(error_frame4, text='Contact should only contain digits', bg='#F5F5DC', fg='red')

    # create frame for buttons
    frame6 = Frame(frame1, bg='#F5F5DC')
    frame6.pack()

    # create a button if user wants to signup instead of login
    B1 = Button(frame6, text='Back', relief='raised', font="Times",
                command=lambda: back(create_wind), bg='#F5F5DC')
    B1.pack(side='left', padx=10, pady=10)

    # create a button if user wants to step towards next step
    B2 = Button(frame6, text='Create', relief='raised', font="Times", command=lambda: save_user_info(create_wind,
                name_error_lab, empty_name_error_lab, pass_len_error_lab, pass_digit_error_lab,
                add_digit_error_lab, add_alpha_error_lab, empty_pass_error_lab, empty_add_error_lab,
                empty_cont_error_lab, cont_alpha_error_lab, cont_len_error_lab, entry_username, entry_password,
                entry_address, entry_contact), bg='#F5F5DC')
    B2.pack(side='right', padx=10, pady=10)

    # to run the window
    create_wind.mainloop()

    return (create_wind, name_error_lab, empty_name_error_lab, pass_len_error_lab, pass_digit_error_lab,
            add_digit_error_lab, add_alpha_error_lab, empty_pass_error_lab, empty_add_error_lab, empty_cont_error_lab,
            cont_alpha_error_lab, cont_len_error_lab, entry_username, entry_password, entry_address, entry_contact)


def save_user_info(create_wind, name_error_lab, empty_name_error_lab, pass_len_error_lab,
                   pass_digit_error_lab, add_digit_error_lab, add_alpha_error_lab, empty_pass_error_lab,
                   empty_add_error_lab, empty_cont_error_lab, cont_alpha_error_lab, cont_len_error_lab, entry_username,
                   entry_password, entry_address, entry_contact):

    username = entry_username.get()
    password = entry_password.get()
    address = entry_address.get()
    contact = entry_contact.get()

    if not username:
        empty_name_error_lab.pack()
        empty_cont_error_lab.pack_forget()
        empty_add_error_lab.pack_forget()
        empty_pass_error_lab.pack_forget()

    elif not password:
        empty_pass_error_lab.pack()
        empty_name_error_lab.pack_forget()
        empty_cont_error_lab.pack_forget()
        empty_add_error_lab.pack_forget()

    elif not address:
        empty_add_error_lab.pack()
        empty_name_error_lab.pack_forget()
        empty_pass_error_lab.pack_forget()
        empty_cont_error_lab.pack_forget()

    elif not contact:
        empty_cont_error_lab.pack()
        empty_add_error_lab.pack_forget()
        empty_name_error_lab.pack_forget()
        empty_pass_error_lab.pack_forget()

    else:
        with open('user_history.txt', 'a+') as info_file:
            info_file.seek(0)
            usernames = [line.split(',')[0].strip() for line in info_file.readlines()]

            if username in usernames:
                name_error_lab.pack()
                empty_pass_error_lab.pack_forget()
                empty_name_error_lab.pack_forget()
                empty_cont_error_lab.pack_forget()
                empty_add_error_lab.pack_forget()

            else:
                name_error_lab.pack_forget()
                empty_pass_error_lab.pack_forget()

                if len(password) < 8:     # if password is not strong
                    pass_len_error_lab.pack()
                    empty_pass_error_lab.pack_forget()
                    pass_digit_error_lab.pack_forget()
                    empty_name_error_lab.pack_forget()
                    empty_cont_error_lab.pack_forget()
                    empty_add_error_lab.pack_forget()

                elif not any(char.isdigit() for char in password):  # if password is not strong
                    pass_digit_error_lab.pack()
                    pass_len_error_lab.pack_forget()
                    empty_pass_error_lab.pack_forget()
                    empty_name_error_lab.pack_forget()
                    empty_cont_error_lab.pack_forget()
                    empty_add_error_lab.pack_forget()

                else:    # if password is strong enough
                    pass_digit_error_lab.pack_forget()
                    pass_len_error_lab.pack_forget()
                    empty_pass_error_lab.pack_forget()
                    empty_name_error_lab.pack_forget()
                    empty_cont_error_lab.pack_forget()
                    empty_add_error_lab.pack_forget()

                    if not any(char.isalpha() for char in address):   # if address is not strong
                        add_alpha_error_lab.pack()
                        add_digit_error_lab.pack_forget()
                        empty_add_error_lab.pack_forget()

                    elif not any(digit.isdigit() for digit in address):     # if address is not strong
                        add_digit_error_lab.pack()
                        add_alpha_error_lab.pack_forget()
                        empty_add_error_lab.pack_forget()

                    else:       # if address is strong enough
                        add_digit_error_lab.pack_forget()
                        add_alpha_error_lab.pack_forget()
                        empty_add_error_lab.pack_forget()

                        if len(contact) != 11:
                            cont_len_error_lab.pack()
                            empty_cont_error_lab.pack_forget()
                            cont_alpha_error_lab.pack_forget()

                        elif any(char.isalpha() for char in contact):
                            cont_alpha_error_lab.pack()
                            cont_len_error_lab.pack_forget()
                            empty_cont_error_lab.pack_forget()

                        else:
                            cont_alpha_error_lab.pack_forget()
                            cont_len_error_lab.pack_forget()
                            empty_cont_error_lab    .pack_forget()

                            with open('user_history.txt', 'a+') as info:
                                info.write('\n' + username + ',')
                                info.write(' ' + password + ',')
                                info.write(' ' + address + ',')
                                info.write(' ' + contact)

                                prd_menu(username, create_wind)
