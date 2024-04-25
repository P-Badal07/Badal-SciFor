class MyClass:
    def __init__(self):
        self._value = 0
    def get_value(self):
        return self._value
    def set_value(self, value):
        self._value = value
    @property
    def doubled_value(self):
        return self._value * 2

    def add_ten(self, lst):
        return list(map(lambda x: x + 10, lst))
    def generate_squares(self, n):
        for i in range(n):
            yield i ** 2
obj = MyClass()

print("Getter:", obj.get_value())
obj.set_value(6)
print("Getter after setting:", obj.get_value())
print("Doubled value using decorator:", obj.doubled_value)
lst = [1, 2, 3, 4, 5]
print("List after adding 10 to each element:", obj.add_ten(lst))
print("Squares generated using generator:")
for square in obj.generate_squares(5):
    print(square)



import tkinter as tk
class SimpleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Tkinter App")

        # Label to display message
        self.label = tk.Label(root, text="Welcome to Tkinter App!")
        self.label.pack(pady=10)

        # Button to close the app
        self.close_button = tk.Button(root, text="Close", command=root.destroy)
        self.close_button.pack()


root = tk.Tk()
app = SimpleApp(root)
root.mainloop()
