import random

class PerceptronRosenblatt:
    def __init__(self, num_features, num_classes, learning_rate=0.1):
        """
        Инициализирует новый экземпляр класса.

        Параметры:
            num_features (int): Количество входных признаков.
            num_classes (int): Количество классов.
            learning_rate (float, опционально): Скорость обучения модели. По умолчанию 0.1.
        """
        self.num_features = num_features
        self.num_classes = num_classes
        self.learning_rate = learning_rate
        self.weights = [[0.0] * num_features for _ in range(num_classes)]
        self.biases = [0.0] * num_classes
    
    def predict(self, input_data):
        """
        Прогнозирует метку класса для заданных входных данных.

        Параметры:
            input_data (list): Входные данные для классификации.

        Возвращает:
            int: Предсказанная метка класса.
        """
        net = [0.0] * self.num_classes
        for i in range(self.num_classes):
            for j in range(self.num_features):
                net[i] += self.weights[i][j] * input_data[j]
            net[i] += self.biases[i]
        return net.index(max(net))
    
    def train(self, input_data, target_class):
        """
        Обучает модель, используя переданные входные данные и целевой класс.

        Параметры:
            input_data (list): Входные данные, используемые для обучения модели.
            target_class (int): Целевой класс для входных данных.

        Возвращает:
            None
        """
        predicted_class = self.predict(input_data)
        if predicted_class != target_class:
            for i in range(self.num_features):
                self.weights[target_class][i] += self.learning_rate * input_data[i]
                self.weights[predicted_class][i] -= self.learning_rate * input_data[i]
            self.biases[target_class] += self.learning_rate
            self.biases[predicted_class] -= self.learning_rate

    def do_train(self, training_data, num_epochs):
        """
        Обучает модель с использованием переданных обучающих данных в течение указанного числа эпох.

        Параметры:
            training_data (List[Tuple[Any, Any]]): Список кортежей, 
                содержащих обучающие данные и соответствующие цели.
            num_epochs (int): Количество эпох для обучения модели.

        Возвращает:
            None
        """
        for epoch in range(num_epochs):
            random.shuffle(training_data)
            for data, target in training_data:
                self.train(data, target)
