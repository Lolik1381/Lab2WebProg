

class Matrix:

    def __init__(self, string_first, string_second):
        if len(string_first) != len(string_second):
            raise Exception("Size first and second line not equals!")

        self.__matrix = [string_first, string_second]

    def get_determinant(self):
        return self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[0][1] * self.__matrix[1][0]

    def __eq__(self, other):
        return self.get_determinant() == other.get_determinant()

    def __ne__(self, other):
        return self.get_determinant() != other.get_determinant()

    def __lt__(self, other):
        return self.get_determinant() < other.get_determinant()

    def __gt__(self, other):
        return self.get_determinant() > other.get_determinant()

    def __le__(self, other):
        return self.get_determinant() <= other.get_determinant()

    def __ge__(self, other):
        return self.get_determinant() >= other.get_determinant()

    def __add__(self, other):
        length = len(self.__matrix)
        result_matrix = [[0 for i in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                result_matrix[i][j] = self.__matrix[i][j] + other.__matrix[i][j]
        return result_matrix

    def __mul__(self, other):
        length = len(self.__matrix)
        result_matrix = [[0 for i in range(length)] for i in range(length)]
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    result_matrix[i][j] += self.__matrix[i][k] * other.__matrix[k][j]
        return result_matrix

