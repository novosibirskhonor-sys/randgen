from logic import generate

print("Одно число — от 1 до него. Два числа — от первого до второго.")
print("«пароль» — 8-символьный пароль, «пароль N» — из N символов. Пустой ввод — выход.")

while True:
    text = input("\nВвод: ").strip()
    if not text:
        break
    for line in generate(text):
        print(line)
    print("Источник: криптографический генератор Android через Python secrets. Интернет не нужен.")
