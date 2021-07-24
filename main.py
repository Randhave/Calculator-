from tkinter import *
from tkinter.messagebox import *
import math

font = ('Vardana', 20, 'bold')
sc_font = ('', 12, 'bold')

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("My Calculator")
        self.window.geometry('450x500')
        self.frame = Frame(self.window)

        # headings
        self.heading_1 = Label(self.window, text='Calculator', font=font)
        self.heading_1.pack(side=TOP, pady=5)  # pack it save what you declared

        self.text_field = Entry(self.window, justify=CENTER, font=font)
        self.text_field.pack(side=TOP, pady=5, fill=X, padx=10)
        self.sc_calci = Scientific_calculator(self.window, self.frame, self.text_field)
 

    def create_frame(self):
      
        self.frame.pack(side=TOP)
 
        self.temp = 1
        for i in range(3):
            for j in range(3):
                self.btn = Button(self.frame, text=str(self.temp), font=font, relief='ridge', width=5,activeforeground='white', activebackground="orange")
                self.btn.grid(row=i, column=j, pady=3, padx=3)
                self.temp = self.temp + 1
                self.btn.bind('<Button-1>', self.click_event) 

    def other_keys(self):
        self.plus_btn = Button(self.frame, text='+', font=font, relief='ridge', width=5, activeforeground='white',activebackground="orange")
        self.plus_btn.grid(row=0, column=4)

        self.minus_btn = Button(self.frame, text='-', font=font, relief='ridge', width=5, activeforeground='white',activebackground="orange")
        self.minus_btn.grid(row=1, column=4)

        self.multi_btn = Button(self.frame, text='x', font=font, relief='ridge', width=5, activeforeground='white',activebackground="orange")
        self.multi_btn.grid(row=2, column=4)

        self.devide_btn = Button(self.frame, text='/', font=font, relief='ridge', width=5, activeforeground='white',activebackground="orange")
        self.devide_btn.grid(row=3, column=4)

        self.zero_btn = Button(self.frame, text='0', font=font, relief='ridge', width=5, activeforeground='white',activebackground="orange")
        self.zero_btn.grid(row=3, column=0)

        self.dot_btn = Button(self.frame, text='.', font=font, relief='ridge', width=5, activeforeground='white',activebackground="orange")
        self.dot_btn.grid(row=3, column=1)

        self.equl_btn = Button(self.frame, text='=', font=font, relief='raised', width=5, activeforeground='white',activebackground="green")
        self.equl_btn.grid(row=3, column=2)

        self.back_btn = Button(self.frame, text='<--', font=font, relief='ridge', width=11, activeforeground='white',activebackground="orange")
        self.back_btn.grid(row=4, column=0, columnspan=2, pady=5)

        self.allclear_btn = Button(self.frame, text='AC', font=font, relief='ridge', width=5, activeforeground='white',activebackground="red")
        self.allclear_btn.grid(row=4, column=2, columnspan=2, pady=5)

        self.exit_btn = Button(self.frame, text='Exit',  font=font, relief='ridge', width=5, activeforeground='white',activebackground="red")
        self.exit_btn.grid(row=4, column=3, columnspan=2, pady=5)

    def binding_functions(self):
        self.plus_btn.bind('<Button-1>', self.click_event)
        self.minus_btn.bind('<Button-1>', self.click_event)
        self.multi_btn.bind('<Button-1>', self.click_event)
        self.devide_btn.bind('<Button-1>', self.click_event)
        self.zero_btn.bind('<Button-1>', self.click_event)
        self.dot_btn.bind('<Button-1>', self.click_event)
        self.equl_btn.bind('<Button-1>', self.click_event)
        self.back_btn.bind('<Button-1>', self.click_event)
        self.allclear_btn.bind('<Button-1>', self.click_event)
        self.exit_btn.bind('<Button-1>', lambda event: self.window.destroy())

    def evalute_query(self):
        global answer
        if self.text == 'x':
            self.text_field.insert(END, '*')
            return

        if self.text == 'AC':
            self.text_field.delete(0, END)
            return

        if self.text == '<--':
            input = self.text_field.get()
            clear_input = input[0:len(input) - 1]
            self.text_field.delete(0, END)
            self.text_field.insert(0, clear_input)
            return clear_input

        if self.text == '=':
            
            try:
                query = self.text_field.get()
                answer = eval(query)
                self.text_field.delete(0, END)
                self.text_field.insert(0, answer)
            except Exception as e:
                showerror("Error", e)

            return answer

        self.text_field.insert(END, self.text)  
    def click_event(self, event):
        self.input = event.widget 
        self.text = self.input['text']
        
        self.evalute_query()

    def run(self):
       
        self.create_frame()
        self.buttons()
        self.other_keys()
        self.binding_functions()
        self.sc_calci.sc_calci_function()
        self.window.mainloop()  
        print("Hello Friends....")

#  Scientific_calculator  is main class
class Scientific_calculator:
    def __init__(self, window, frame, text_field):
        self.text_field = text_field
        self.frame = frame
        self.window = window
        self.sc_frame = Frame(self.window)
        self.menubar = Menu(
        self.window)   
        self.mode = Menu(self.menubar, font=sc_font,tearoff=0)  
        self.mode.add_command(label="Scientific Calculator", command=self.show_sc_calci) 
        self.menubar.add_cascade(label="Scientific Calculator", menu=self.mode)   
        self.window.config(menu=self.menubar)  

    def sc_buttons(self):
        self.sqrt_btn = Button(self.sc_frame, text='sqrt', font=font, width=5, relief='ridge',activebackground="orange")
        self.sqrt_btn.grid(row=0, column=0, padx=2, pady=3)

        self.power_btn = Button(self.sc_frame, text='^', font=font, width=5, relief='ridge', activebackground="orange")
        self.power_btn.grid(row=0, column=1, padx=2, pady=3)

        self.fact_btn = Button(self.sc_frame, text='x!', font=font, width=5, relief='ridge', activebackground="orange")
        self.fact_btn.grid(row=0, column=2, padx=2, pady=3)

        self.to_degree = Button(self.sc_frame, text='toDeg', font=font, width=5, relief='ridge', activebackground="orange")
        self.to_degree.grid(row=0, column=3, padx=2, pady=3)

        self.sin_btn = Button(self.sc_frame, text='sin', font=font, width=5, relief='ridge', activebackground="orange")
        self.sin_btn.grid(row=1, column=0, padx=2, pady=3)

        self.cos_btn = Button(self.sc_frame, text='cos', font=font, width=5, relief='ridge', activebackground="orange")
        self.cos_btn.grid(row=1, column=1, padx=2, pady=3)

        self.tan_btn = Button(self.sc_frame, text='tan', font=font, width=5, relief='ridge', activebackground="orange")
        self.tan_btn.grid(row=1, column=2, padx=2, pady=3)

        self.to_redient = Button(self.sc_frame, text='toRed', font=font, width=5, relief='ridge',activebackground="orange")
        self.to_redient.grid(row=1, column=3, padx=2, pady=3)

    
    def binding_sc_functions(self):
        self.sqrt_btn.bind('<Button-1>', self.scientific_click_event)
        self.fact_btn.bind('<Button-1>', self.scientific_click_event)
        self.power_btn.bind('<Button-1>', self.scientific_click_event)
        self.to_degree.bind('<Button-1>', self.scientific_click_event)
        self.sin_btn.bind('<Button-1>', self.scientific_click_event)
        self.cos_btn.bind('<Button-1>', self.scientific_click_event)
        self.tan_btn.bind('<Button-1>', self.scientific_click_event)
        self.to_redient.bind('<Button-1>', self.scientific_click_event)

   
    def scientific_click_event(self, event):
        self.input = event.widget
        self.text = self.input['text']
        self.query = self.text_field.get()
     
        self.answer = ''

        try:
            if self.text == 'toDeg':
                print("choose toDeg")
                self.answer = str(math.degrees(int(self.query)))

            if self.text == 'toRed':
                print("choose toDeg")
                self.answer = str(math.radians(int(self.query)))

            if self.text == 'sqrt':
                print("choose toDeg")
                self.answer = str(math.sqrt(int(self.query)))

            if self.text == 'x!':
                print("choose toDeg")
                self.answer = str(math.factorial(int(self.query)))

            if self.text == '^':
                self.answer = str(math.pow(int(self.query), int(self.query)))

            if self.text == 'sin':
                self.answer = str(math.sin(math.radians(int(self.query))))

            if self.text == 'cos':
                self.answer = str(math.cos(math.radians(int(self.query))))

            if self.text == 'tan':
                self.answer = str(math.tan(math.radians(int(self.query))))

        except Exception as e:
            showerror('Error', e)

        self.text_field.delete(0, END)
        self.text_field.insert(0, self.answer)

    def show_sc_calci(self):

        self.normal_mode = True
        if self.normal_mode:
            self.window.geometry('450x550')
            self.normal_mode = False
            self.frame.pack_forget()
            self.sc_frame.pack(side=TOP)
            self.frame.pack(side=TOP)
        else:
            self.window.geometry('450x500')
            self.sc_frame.pack_forget()
            self.normal_mode = True

    def sc_calci_function(self):
      
        self.sc_buttons()
        self.binding_sc_functions()


if __name__ == '__main__':
    print("Hello Aniket...")
    calci = Calculator()
    calci.run()
