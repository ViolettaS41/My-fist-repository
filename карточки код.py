from tkinter import *
from tkinter import ttk
import customtkinter
from customtkinter import *
from PIL import Image, ImageTk

root = CTk()
root.title('Карточки по английскому')
root.geometry('530x525+200+200')
customtkinter.set_appearance_mode('light')
root.resizable(False, False)
root.configure(background='#FFEFCD')

root.wm_iconbitmap()
icopath = ImageTk.PhotoImage(file="pngeng icon.png")
root.iconphoto(False, icopath)

def click_a():
    win = Tk()
    win.title('Animals')
    win.geometry('600x400+200+200')
    win.configure(background='#FFEFCD')
    def add_words():
        word1 = entry1.get()
        word2 = entry2.get()
        word3 = entry3.get()

        tree.insert("", "end", values=(word1, word2, word3))

    entry1 = customtkinter.CTkEntry(win)
    entry1.grid(row=0, column=0, padx=10, pady=10)

    entry2 = customtkinter.CTkEntry(win)
    entry2.grid(row=0, column=1, padx=10, pady=10)

    entry3 = customtkinter.CTkEntry(win)
    entry3.grid(row=0, column=2, padx=10, pady=10)

    btn = customtkinter.CTkButton(win, text="Add Words", command=add_words, fg_color='#E09132',
                                  hover_color='#A46B25', font=('Times New Roman', 15), text_color='#FFFFFF')

    btn.grid(row=1, column=1)

    tree = ttk.Treeview(win, columns=('Word', 'translate', 'transcription'), show='headings')

    words = [("Кошка/Кот", "Cat", "[kæt]"), ("Собака","Dog", "[dɒg]"), ("Хомяк","Hamster", "[ˈhæmstə]"), (
        "Морская свинка", 'Guinea pig', "[ˈgɪnɪ pɪg]")]

    tree.heading("Word", text="Word")
    tree.heading("translate", text="Translate")
    tree.heading("transcription", text="Transcription")

    tree.column('#1', stretch=YES, width=150)
    tree.column('#2', stretch=YES, width=100)
    tree.column('#3', stretch=YES, width=100)
    tree.grid(row=2, columnspan=3, padx=10, pady=10)

    for word in words:
        tree.insert('', END, values=word)


def click_fandr():
    win2= Tk()
    win2.title('Family and relationships')
    win2.geometry('600x400+200+200')
    win2.resizable(False, False)
    win2.configure(background='#FFEFCD')

    def add_words():
        word1 = entry1.get()
        word2 = entry2.get()
        word3 = entry3.get()

        tree.insert("", "end", values=(word1, word2, word3))

    entry1 = customtkinter.CTkEntry(win2)
    entry1.grid(row=0, column=0, padx=10, pady=10)

    entry2 = customtkinter.CTkEntry(win2)
    entry2.grid(row=0, column=1, padx=10, pady=10)

    entry3 = customtkinter.CTkEntry(win2)
    entry3.grid(row=0, column=2, padx=10, pady=10)

    btn = customtkinter.CTkButton(win2, text="Add Words", command=add_words, fg_color='#E09132',
                                  hover_color='#A46B25', font=('Times New Roman', 15), text_color='#FFFFFF')

    btn.grid(row=1, column=1)

    tree = ttk.Treeview(win2, columns=('Word', 'translate', 'transcription'), show='headings')

    words = [("Мама", "Mother", "[ˈmʌðə]"), ("Папа", "Father", "[ˈfɑːðə]"), ("Сын", "Son", "[sʌn]"), (
        "Дочь", 'Daughter', "[ˈdɔːtə]")]

    tree.heading("Word", text="Word")
    tree.heading("translate", text="Translate")
    tree.heading("transcription", text="Transcription")

    tree.column('#1', stretch=YES, width=150)
    tree.column('#2', stretch=YES, width=100)
    tree.column('#3', stretch=YES, width=100)
    tree.grid(row=2, columnspan=3, padx=10, pady=10)

    for word in words:
        tree.insert('', END, values=word)


def click_jandc():
    win3=Tk()
    win3.title('Jobs and careers')
    win3.geometry('600x400+200+200')
    win3.resizable(False, False)
    win3.configure(background='#FFEFCD')

    def add_words():
        word1 = entry1.get()
        word2 = entry2.get()
        word3 = entry3.get()

        tree.insert("", "end", values=(word1, word2, word3))

    entry1 = customtkinter.CTkEntry(win3)
    entry1.grid(row=0, column=0, padx=10, pady=10)

    entry2 = customtkinter.CTkEntry(win3)
    entry2.grid(row=0, column=1, padx=10, pady=10)

    entry3 = customtkinter.CTkEntry(win3)
    entry3.grid(row=0, column=2, padx=10, pady=10)

    btn = customtkinter.CTkButton(win3, text="Add Words", command=add_words, fg_color='#E09132',
                                  hover_color='#A46B25', font=('Times New Roman', 15), text_color='#FFFFFF')

    btn.grid(row=1, column=1)

    tree = ttk.Treeview(win3, columns=('Word', 'translate', 'transcription'), show='headings')

    words = [("Работа", "job", "[wɜːk]"), ("карьера", "career", "[kəˈrɪə]"),
             ("Профессия", "profession", "[prəˈfeʃn]"), (
                 "род занятий", 'occupation', "[ɒkjʊˈpeɪʃn]")]

    tree.heading("Word", text="Word")
    tree.heading("translate", text="Translate")
    tree.heading("transcription", text="Transcription")

    tree.column('#1', stretch=YES, width=150)
    tree.column('#2', stretch=YES, width=100)
    tree.column('#3', stretch=YES, width=100)
    tree.grid(row=2, columnspan=3, padx=10, pady=10)

    for word in words:
        tree.insert('', END, values=word)

def click_eandl():
    win4=Tk()
    win4.title('Education and learning')
    win4.geometry('600x400+200+200')
    win4.resizable(False, False)
    win4.configure(background='#FFEFCD')

    def add_words():
        word1 = entry1.get()
        word2 = entry2.get()
        word3 = entry3.get()

        tree.insert("", "end", values=(word1, word2, word3))

    entry1 = customtkinter.CTkEntry(win4)
    entry1.grid(row=0, column=0, padx=10, pady=10)

    entry2 = customtkinter.CTkEntry(win4)
    entry2.grid(row=0, column=1, padx=10, pady=10)

    entry3 = customtkinter.CTkEntry(win4)
    entry3.grid(row=0, column=2, padx=10, pady=10)

    btn = customtkinter.CTkButton(win4, text="Add Words", command=add_words, fg_color='#E09132',
                                  hover_color='#A46B25', font=('Times New Roman', 15), text_color='#FFFFFF')

    btn.grid(row=1, column=1)

    tree = ttk.Treeview(win4, columns=('Word', 'translate', 'transcription'), show='headings')

    words = [("Изучение", "Learning", "[ˈlɜːrnɪŋ]"), ("Образование", "Education", "[ˌedjʊˈkeɪʃn̩]"),
             ("Школа", "School", "[skuːl]"), (
                 "Университет", 'University', "[ˌjuːnɪˈvɜːrsɪti]")]

    tree.heading("Word", text="Word")
    tree.heading("translate", text="Translate")
    tree.heading("transcription", text="Transcription")

    tree.column('#1', stretch=YES, width=150)
    tree.column('#2', stretch=YES, width=100)
    tree.column('#3', stretch=YES, width=100)
    tree.grid(row=2, columnspan=3, padx=10, pady=10)

    for word in words:
        tree.insert('', END, values=word)


def click_fandd():
    win5=Tk()
    win5.title('Food and Drink')
    win5.geometry('600x400+200+200')
    win5.resizable(False, False)
    win5.configure(background='#FFEFCD')

    def add_words():
        word1 = entry1.get()
        word2 = entry2.get()
        word3 = entry3.get()

        tree.insert("", "end", values=(word1, word2, word3))

    entry1 = customtkinter.CTkEntry(win5)
    entry1.grid(row=0, column=0, padx=10, pady=10)

    entry2 = customtkinter.CTkEntry(win5)
    entry2.grid(row=0, column=1, padx=10, pady=10)

    entry3 = customtkinter.CTkEntry(win5)
    entry3.grid(row=0, column=2, padx=10, pady=10)

    btn = customtkinter.CTkButton(win5, text="Add Words", command=add_words, fg_color='#E09132',
                                  hover_color='#A46B25', font=('Times New Roman', 15), text_color='#FFFFFF')

    btn.grid(row=1, column=1)

    tree = ttk.Treeview(win5, columns=('Word', 'translate', 'transcription'), show='headings')

    words = [('Яблоко',"Apple",  '[ˈæpl]'), ('Банан',"Banana", '[ˌbænəˈnɑ ]'),
             ('Хлеб','Bread', "[bred] "), ('Масло', 'Butter', '[ˈbʌtə ]'), ('Курица', 'Chicken','[ˈʧɪkɪn]' ),
             ('Кофе', 'Coffee','[ˈkɒfi ]')]

    tree.heading("Word", text="Word")
    tree.heading("translate", text="Translate")
    tree.heading("transcription", text="Transcription")

    tree.column('#1', stretch=YES, width=150)
    tree.column('#2', stretch=YES, width=100)
    tree.column('#3', stretch=YES, width=100)
    tree.grid(row=2, columnspan=3, padx=10, pady=10)

    for word in words:
        tree.insert('', END, values=word)

def click_candf():
    win6=Tk()
    win6.title('Add your own topic')
    win6.geometry('600x400+200+200')
    win6.resizable(False, False)
    win6.configure(background='#FFEFCD')

    def add_words():
        word1 = entry1.get()
        word2 = entry2.get()
        word3 = entry3.get()

        tree.insert("", "end", values=(word1, word2, word3))

    entry1 = customtkinter.CTkEntry(win6)
    entry1.grid(row=0, column=0, padx=10, pady=10)

    entry2 = customtkinter.CTkEntry(win6)
    entry2.grid(row=0, column=1, padx=10, pady=10)

    entry3 = customtkinter.CTkEntry(win6)
    entry3.grid( row=0, column=2, padx=10, pady=10)

    btn = customtkinter.CTkButton(win6, text="Add Words", command=add_words, fg_color='#E09132',
                                  hover_color='#A46B25', font= ('Times New Roman', 15), text_color='#FFFFFF')

    btn.grid(row=1, column=1)

    tree = ttk.Treeview(win6, columns=("Word", "translate", "transcription"))
    #tree.heading("#0", text="Index")
    tree.heading("Word", text="Word")
    tree.heading("translate", text="Translate")
    tree.heading("transcription", text="Transcription")

    tree.column('#1', stretch=YES, width=150)
    tree.column('#2', stretch=YES, width=100)
    tree.column('#3', stretch=YES, width=100)
    tree.grid(row=2, columnspan=3, padx=10, pady=10)


def click_pr():
    second_window = Toplevel(root)
    image = Image.open("местоимения.png")  # Путь к вашему изображению
    photo = ImageTk.PhotoImage(image)
    label = Label(second_window, image=photo)
    label.image = photo
    label.pack()


def click_tm():
    second_window = Toplevel(root)
    image = Image.open("времена.jpg")  # Путь к вашему изображению
    photo = ImageTk.PhotoImage(image)
    label = Label(second_window, image=photo)
    label.image = photo
    label.pack()


btn_animals = customtkinter.CTkButton(root, text='Animals and pets', width=150, height=150, fg_color='#E09132',
                                      hover_color='#A46B25', font=('Times New Roman', 15), text_color='#FFFFFF', command=click_a)
btn_animals.grid(row=0, column=1, padx=10, pady=10)

btn_fandr = customtkinter.CTkButton(root, text='Family and relationships', width=150, height=150, fg_color='#E09132',
                                    hover_color='#A46B25', font=('Times New Roman', 15), text_color='#FFFFFF',
                                    command=click_fandr)
btn_fandr.grid(row=0, column=2, padx=10, pady=10)

btn_jandc = customtkinter.CTkButton(root, text='Jobs and careers', width=150, height=150, fg_color='#E09132',
                                    hover_color='#A46B25', font= ('Times New Roman', 15), text_color='#FFFFFF',
                                    command=click_jandc)
btn_jandc.grid(row=0, column=3, padx=10, pady=10)

btn_eandl = customtkinter.CTkButton(root, text='Education and learning', width=150, height=150, fg_color='#E09132',
                                    command=click_eandl, font= ('Times New Roman', 15), text_color='#FFFFFF',
                                    hover_color='#A46B25')
btn_eandl.grid(row=1, column=1, padx=10, pady=10)

btn_fandd= customtkinter.CTkButton(root, text='Food and Drink', width=150, height=150, fg_color='#E09132',
                                    hover_color='#A46B25', font= ('Times New Roman', 15), text_color='#FFFFFF', command=click_fandd)
btn_fandd.grid(row=1, column=2, padx=10, pady=10)

btn_candf= customtkinter.CTkButton(root, text='Add your own topic', width=150, height=150, fg_color='#E09132',
                                    hover_color='#A46B25', font= ('Times New Roman', 15), text_color='#FFFFFF', command=click_candf)
btn_candf.grid(row=1, column=3, padx=10, pady=10)

btn_im=customtkinter.CTkButton(root, text='Pronouns', width=150, height=150, fg_color='#E09132',
                                    hover_color='#A46B25', font= ('Times New Roman', 15), text_color='#FFFFFF', command=click_pr)
btn_im.grid(row=2, column=1, padx=10, pady=10)

btn_im=customtkinter.CTkButton(root, text='Times', width=150, height=150, fg_color='#E09132',
                                    hover_color='#A46B25', font= ('Times New Roman', 15), text_color='#FFFFFF', command=click_tm)
btn_im.grid(row=2, column=3, padx=10, pady=10)

label = customtkinter.CTkLabel(root, text='Choose a topic to study',  text_color='#424530',
                               font=('Times New Roman', 17))
label.grid(row=2, column=2, padx=10, pady=10)

root.mainloop()