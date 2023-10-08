import tkinter as tk
import PerceptronRosenblatt as Neiron

class DigitDrawingApp:
    def __init__(self, root):
        """
        Инициализирует экземпляр класса с указанным корневым окном.

        Параметры:
            root (tk.Tk): Корневое окно приложения.

        Возвращает:
            None
        """
        self.root = root
        self.root.title("Рисование цифры")
        
        # Установка размера окна
        self.root.geometry("200x200")
        
        # Создание виджетов для рисования
        self.pixel_widgets = []
        for i in range(5):
            row_widgets = []
            for j in range(3):
                pixel = tk.IntVar()
                pixel.set(0) 
                checkbutton = tk.Checkbutton(self.root, variable=pixel, indicatoron=False, width=2, height=1)
                checkbutton.grid(row=i, column=j)
                row_widgets.append(pixel)
            self.pixel_widgets.append(row_widgets)
        
        # Кнопка для анализа рисунка
        analyze_button = tk.Button(self.root, text="Анализировать", command=self.analyze_drawing)
        analyze_button.grid(row=6, columnspan=3)
        
        # Метка для вывода результата анализа
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=7, columnspan=3)
    
    # Функция для отображения результатов анализа рисунка
    def analyze_drawing(self):
        """
        Анализирует рисунок в pixel_widgets и предсказывает распознанную цифру.
        
        Возвращает:
            None
        """
        result = ""
        for i in range(5):
            row = ""
            for j in range(3):
                pixel_value = self.pixel_widgets[i][j].get()
                row += "1" if pixel_value == 1 else "0"
            result += row

        # Обработка результата
        num0 = list('111101101101111')
        num1 = list('001001001001001')
        num2 = list('111001111100111')
        num3 = list('111001111001111')
        num4 = list('101101111001001')
        num5 = list('111100111001111')
        num6 = list('111100111101111')
        num7 = list('111001001001001')
        num8 = list('111101111101111')
        num9 = list('111101111001111')

        num_features = len(num0)
        num_classes = 10
        perceptron = Neiron.PerceptronRosenblatt(num_features, num_classes)

        training_data = [(list(map(int, num)), target) for target, num in enumerate([num0, num1, num2, num3, num4, num5, num6, num7, num8, num9])]
        num_epochs = 100

        perceptron.do_train(training_data, num_epochs)

        input_data = list(map(int, result))
        recognized_digit = perceptron.predict(input_data)

        # Вывод результата.
        self.result_label.config(text=recognized_digit)
