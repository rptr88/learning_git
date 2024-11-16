def calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."

# Contoh penggunaan
result = calculator(10, 5, 'add')
print("Hasil penjumlahan:", result)

result = calculator(10, 5, 'divide')
print("Hasil pembagian:", result)