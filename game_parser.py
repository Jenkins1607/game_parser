import requests
from bs4 import BeautifulSoup

def parse_game_links(product):
    # URL сайта, который мы хотим парсить
    url = f'https://stopgame.ru/search?s={product}'

    # Заголовки для имитации запроса от браузера
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Выполняем GET-запрос
    response = requests.get(url, headers=headers)

    # Проверяем, успешен ли запрос
    if response.status_code == 200:
        # Парсим HTML-код страницы
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все заголовки с ссылками на игры
        news_links = soup.find_all('h2', class_="_title_1fjyn_173")  # Проверьте правильность класса

        # Извлекаем href из каждой ссылки
        for link in news_links:
            a_tag = link.find('a')  # Ищем тег <a> внутри <h2>
            if a_tag:
                href = a_tag.get('href')
                if href:
                    print("https://stopgame.ru" + href)  # Полная ссылка
    else:
        print(f'Ошибка при запросе: {response.status_code}')


if __name__ == '__main__':
    while True:
        product_name = input("Введите название игры для поиска (или 'exit' для выхода): ")
        if product_name.lower() == 'exit':
            break
        parse_game_links(product_name)
