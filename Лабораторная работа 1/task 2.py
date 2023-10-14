weight_symbol = 4  # Для хранения кода одного символа нужно 4 байта.
count_symbols = 25  # Количество символов в строке - 25.
count_strings = 50  # Число строк на странице - 50.
count_pages = 100  # Количество страниц в книге - 100.
volume_floppy = 1.44  # Информационный объем дискеты равен 1,44 Мб.

# TODO Найдите количество книг, которое можно разместить на дискете
weight_book = weight_symbol * count_symbols * count_strings * count_pages
limited_floppy = volume_floppy * 1024 * 1024 // weight_book
print("Количество книг, помещающихся на дискету:", int(limited_floppy))
