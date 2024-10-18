def encryption():
    while True:
        lang_choice = input('\033[0mВыберите язык (en/ru): ')
        if ('ru' == lang_choice) or ('en' == lang_choice):
            try:
                password = input("Введите начальный пароль: ")

                key = int(input("Введие ключ смещения: "))
            except ValueError:
                print('\n\033[1;31mНеверный ввод. Повторите заново.')
                continue
            break
        else:
            print('\033[1;31mОшибка. Введен не тот язык. Повторите попытку\n')

    new_pass = []
    lang_value = 26

    lang_low = 'abcdefghijklmnopqrstuvwxyz'
    lang_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ru_alp_up = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    ru_akp_low = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    if lang_choice == 'ru':
        lang_value = 33
        lang_up = ru_alp_up
        lang_low = ru_akp_low
    for element in password:
        if element in lang_up:
            if lang_up.index(element) - key >= 0:
                ind_el = lang_up.index(element) - key
                new_pass.append(lang_up[ind_el])
            else:
                ind_el = lang_value - (key + (lang_value - lang_up.index(element)))
                new_pass.append(lang_up[ind_el])

        elif element in lang_low:
            if lang_low.index(element) - key >= 0:
                ind_el = lang_low.index(element) - key
                new_pass.append(lang_low[ind_el])
            else:
                ind_el = lang_value - (key + (lang_value - lang_low.index(element)))
                new_pass.append(lang_low[ind_el])

        else:
            new_pass.append(element)

    return print('\n\033[1;32mРасшифровка: ',''.join(new_pass))



encryption()