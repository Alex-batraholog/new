def generate_password(n):
    result = ""

    # Генерация уникальных пар
    pairs = []
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))

    # Проверка кратности и формирование пароля
    for pair in pairs:
        pair_sum = sum(pair)
        if n % pair_sum == 0:  # Проверка кратности
            result += f"{pair[0]}{pair[1]}"

    return result


# Пример использования:
for num in range(3, 21):
    password = generate_password(num)
    print(f"{num} - {password}")