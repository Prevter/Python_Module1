from task import MyData, TimeReader, Translator

def create_prompt() -> MyData:
    time = input('Введіть час (год хв): ')
    locale = input('Введіть мову інтерфейсу: ')
    return MyData(locale, time)


def output_data(data) -> None:
    locale = data.locale
    time = data.time

    lang = Translator.get(locale)
    if lang is None:
        lang = Translator.get('uk') # default language

    print(lang.translate('Мова:'), lang.name)
    print(lang.translate('Час (год хв):'), time)

    parsedTime = TimeReader.read(time)
    if parsedTime is None:
        print(lang.translate('Неправильний час!'))
        return

    print(parsedTime)
    print(lang.translate(parsedTime.daytime()))


def main() -> None:
    result = MyData.read('MyData')
    if result:
        output_data(result)
        return
    
    data = create_prompt()
    data.save('MyData')
    print('Дані збережено в файл MyData')


if __name__ == "__main__":
    main()
