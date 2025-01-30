from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_and_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и неукратимый питон')
        collector.set_book_genre('Гарри Поттер и неукратимый питон', 'Ужасы')
        assert collector.get_book_genre('Гарри Поттер и неукратимый питон') == 'Ужасы'

    def test_only_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и неукратимый питон')
        collector.set_book_genre('Гарри Поттер и неукратимый питон', 'Ужасы')
        assert collector.books_genre['Гарри Поттер и неукратимый питон'] == 'Ужасы'

    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        book_titles = [('Гарри Поттер и философский питон', 'Фантастика'), ('Мартин Иден', 'Комедии')]
        for title, genre in book_titles:
            collector.add_new_book(title)
            collector.set_book_genre(title, genre)
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        assert fantasy_books == ['Гарри Поттер и философский питон']

    def test_get_books_genre_returns_complete_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и неукратимый питон')
        collector.set_book_genre('Гарри Поттер и неукратимый питон', 'Ужасы')
        books_genre = collector.get_books_genre()
        assert books_genre == {'Гарри Поттер и неукратимый питон': 'Ужасы'}

    def test_get_books_for_children_returns_correct_children_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и повелитель питонов')
        collector.set_book_genre('Гарри Поттер и повелитель питонов', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        assert children_books == ['Гарри Поттер и повелитель питонов']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мартин Иден')
        collector.add_book_in_favorites('Мартин Иден')
        favorites_books = collector.get_list_of_favorites_books()
        assert favorites_books == ['Мартин Иден']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мартин Иден')
        collector.set_book_genre('Мартин Иден', 'Комедии')
        collector.add_book_in_favorites('Мартин Иден')
        favorites_books = collector.get_list_of_favorites_books()
        assert favorites_books == ['Мартин Иден']

        collector.delete_book_from_favorites('Мартин Иден')
        del_favorites_books = collector.get_list_of_favorites_books()
        assert del_favorites_books == []

    def test_empty_list_of_favorites_books(self):
        collector = BooksCollector()
        empty_favorites = collector.get_list_of_favorites_books()
        assert empty_favorites == []


