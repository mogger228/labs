def calculate(first: float, second: float, operation: str) -> float:
    """Выполняет операцию над двумя числами."""
    if operation == "+":
        return first + second
    if operation == "-":
        return first - second
    if operation == "*":
        return first * second
    if operation == "/":
        if second == 0:
            raise ZeroDivisionError("Деление на ноль")
        return first / second
    raise ValueError("Неизвестная операция")


def main() -> None:
    """Запрашивает числа и операцию, печатает результат."""
    first = float(input("Первое число: "))
    operation = input("Операция (+, -, *, /): ")
    second = float(input("Второе число: "))
    print("Результат:", calculate(first, second, operation))


if __name__ == "__main__":
    main()
