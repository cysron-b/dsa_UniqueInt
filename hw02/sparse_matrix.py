class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.elements = {}

    def set_element(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value

    def add(self, other):
        result = SparseMatrix(self.rows, self.cols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.elements.get((row, col), 0) + value)
        return result

    def subtract(self, other):
        result = SparseMatrix(self.rows, self.cols)
        for (row, col), value in self.elements.items():
            result.set_element(row, col, value)
        for (row, col), value in other.elements.items():
            result.set_element(row, col, result.elements.get((row, col), 0) - value)
        return result

    def multiply(self, other):
        result = SparseMatrix(self.rows, other.cols)
        for (row1, col1), value1 in self.elements.items():
            for (row2, col2), value2 in other.elements.items():
                if col1 == row2:
                    result.set_element(row1, col2, result.elements.get((row1, col2), 0) + value1 * value2)
        return result

    def to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f'rows={self.rows}\n')
            f.write(f'cols={self.cols}\n')
            for (row, col), value in sorted(self.elements.items()):
                f.write(f'({row}, {col}, {value})\n')

def read_sparse_matrix(filename):
    with open(filename) as f:
        rows = int(f.readline().strip().split('=')[1])
        cols = int(f.readline().strip().split('=')[1])
        matrix = SparseMatrix(rows, cols)
        for line in f:
            row, col, value = map(int, line.strip().strip('()').split(','))
            matrix.set_element(row, col, value)
        return matrix

def main():
    operation = input("Enter operation (add, subtract, multiply): ").strip().lower()
    file1 = input("Enter filename for matrix 1: ").strip()
    file2 = input("Enter filename for matrix 2: ").strip()
    output_file = input("Enter filename for output: ").strip()

    matrix1 = read_sparse_matrix(file1)
    matrix2 = read_sparse_matrix(file2)

    if operation == 'add':
        result = matrix1.add(matrix2)
    elif operation == 'subtract':
        result = matrix1.subtract(matrix2)
    elif operation == 'multiply':
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid operation")
        return

    result.to_file(output_file)
    print(f"Operation completed. Result saved to {output_file}")

if __name__ == "__main__":
    main()
