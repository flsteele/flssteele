import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel


class App(tk.Tk):
  num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

  def __init__(self):
    super().__init__()
    self.answers = []

    # configure the root window
    self.title('My Multiplication App')
    self.geometry('350x200')
    self.eval("tk::PlaceWindow . center")
    self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # label
    self.label = ttk.Label(self, text='Hello, Let Practice Multiply!')
    self.label.pack()

    # button for practice
    self.buttonPractice = ttk.Button(self, text='Practice')
    self.buttonPractice['command'] = self.practice
    self.buttonPractice.place(relx=0.10, rely=0.64)

    self.input= ttk.Entry(self, justify='center', font=('Courier', 20,'bold'))
    self.input.place(relx=0.35, rely=0.4, relwidth=0.30, relheight=0.20)

    # button for check
    self.buttonCheck = ttk.Button(self, text='Check')
    self.buttonCheck['command'] = lambda: self.check_ans(self.input)
    self.buttonCheck.place(relx=0.65, rely=0.64)

  def practice(self):
      self.input.delete(0, 'end')
      self.num1update = random.choice(self.num)
      self.num2update = random.choice(self.num)
      self.input.focus_set()
      self.newQuestion = ttk.Label(self, text=f"What is {self.num1update}*{self.num2update} ?", font=("Courier", 16))
      self.newQuestion.place(relx=0.16, rely=0.14, relwidth=0.7, relheight=0.23)

  def resultMultiply(self):
      self.practice
      return self.num1update*self.num2update

  def check_ans(self, var1):
      resultAns= self.resultMultiply()
      if var1.get() == str(resultAns):
          self.correct = ttk.Label(self, text='Correct!', font=('Courier', 16))
          self.correct.place(relx=0.16, rely=0.14, relwidth=0.73, relheight=0.23)
      else:
          self.answers.append(f"{self.num1update}*{self.num2update} is {resultAns}")
          self.wrong = ttk.Label(self, text=f"{self.num1update}*{self.num2update} is {resultAns}", font=('Courier', 16))
          self.wrong.place(relx=0.16, rely=0.14, relwidth=0.73, relheight=0.23)

  def save_results(self):
      today = datetime.datetime.now()
      path = os.getcwd()

      filename = f"Results_{today.year}_{today.month}_{today.day}.txt"
      n = 1

      while (os.path.exists(filename)):
          filename = f"Results_{today.year}_{today.month}_{today.day}_{n}.txt"
          n = n + 1

      with open(r'filename', 'w') as fp:
          fp.write('\n'.join(answers))

  def on_closing(self):
    if askokcancel('Quit', 'Do you want to quit?'):
        self.save_results
        self.destroy()


if __name__ == "__main__":
  app = App()
  app.mainloop()
