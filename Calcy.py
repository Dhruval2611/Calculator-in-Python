import tkinter as tk
import math

large_font_style = ("Times New Roman", 40, "bold")
small_font_style = ("Times New Roman", 16)
digit_font_style = ("Times New Roman", 24, "bold")
default_font_style = ("Times New Roman", 20)
off_white = "#F8FAFF"
light_gray = "#F5F5F5"
label_color = "#25265E"
white = "#FFFFFF"
light_blue = "#CCEDFF"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        # self.window.resizable(0, 0)
        self.window.title("Calculator")

        # Labels
        self.total_expression = ""
        self.current_expression = ""

        # Display
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            '.': (4, 1), 0: (4, 2)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        # Buttons
        self.button_frame = self.create_button_frame()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression,
                               anchor=tk.E, bg=light_gray, fg=label_color, padx=24, font=small_font_style)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg=light_gray, fg=label_color, padx=24, font=large_font_style)
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=light_gray)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=white, fg=label_color, font=digit_font_style, borderwidth=0,
                               command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, font=default_font_style,
                               bg=light_blue, fg=label_color, borderwidth=0,
                               command=lambda x=operator: self.add_to_expression(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", font=default_font_style, bg=light_blue, fg=label_color, borderwidth=0,
                           command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.button_frame, text="x²", font=default_font_style, bg=light_blue, fg=label_color, borderwidth=0,
                           command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text="√x", font=default_font_style, bg=light_blue, fg=label_color, borderwidth=0,
                           command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", font=default_font_style, bg=light_blue, fg=label_color, borderwidth=0,
                           command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def format_number(self, number):
        if isinstance(number, float):
            return f"{number:.4f}" if number % 1 != 0 else str(int(number))
        return str(number)

    def square(self):
        try:
            result = eval(self.current_expression)
            self.current_expression = self.format_number(result ** 2)
            self.update_label()
        except Exception as e:
            self.current_expression = "Error"
            self.update_label()

    def sqrt(self):
        try:
            result = eval(self.current_expression)
            self.current_expression = self.format_number(math.sqrt(result))
            self.update_label()
        except Exception as e:
            self.current_expression = "Error"
            self.update_label()

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            result = eval(self.total_expression)
            self.current_expression = self.format_number(result)
            self.total_expression = ""
        except Exception as e:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        for i in range(5):
            frame.rowconfigure(i, weight=1)
            frame.columnconfigure(i, weight=1)
        frame.columnconfigure(0, weight=0)
        frame.columnconfigure(4, weight=1)
        return frame

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
