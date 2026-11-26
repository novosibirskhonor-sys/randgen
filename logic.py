import secrets

def generate(text: str) -> list[str]:
    text = text.strip().lower()
    if not text:
        return []
    parts = text.split(maxsplit=2)

    if parts[0] == "пароль":
        if len(parts) == 1:
            length = 8
        elif len(parts) == 2:
            try:
                length = int(parts[1])
            except ValueError:
                return ["После «пароль» укажи целое число."]
            if length < 1:
                return ["Длина пароля должна быть положительной."]
            if length > 10000:
                return ["Максимальная длина пароля — 10000 символов."]
        else:
            return ["Формат: «пароль» или «пароль N»."]
        return [f"Пароль ({length} симв.): {secrets.token_urlsafe(length)[:length]}"]

    if len(parts) == 1:
        parts.insert(0, "1")
    try:
        low, high = map(int, parts)
    except ValueError:
        return ["Введи одно целое число или две границы через пробел."]
    if low < 0 or low > high:
        return ["Границы: неотрицательные целые, меньшая не больше большей."]
    if low == high:
        return [f"Число: {low}", "Случайность не нужна: в диапазоне только одно число."]
    return [f"Число: {low + secrets.randbelow(high - low + 1)}"]
