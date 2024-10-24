import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = "Apple"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_count_2(self):
        input = "U"
        result = hw1.vowel_count(input)
        expected = 1
        self.assertEqual(expected, result)
    # Part 2
    def test_short_lists_1(self):
        input = [ [1,2], [5,6], [3], [4, 5, 6] ]
        result = hw1.short_lists(input)
        expected = [[1,2], [5,6]]
        self.assertEqual(expected, result)

    def test_short_lists_2(self):
        input = [ [], [-1, -2], [0]]
        result = hw1.short_lists(input)
        expected = [[-1,-2]]
        self.assertEqual(expected, result)
    # Part 3
    def test_ascending_pairs_1(self):
        input = [ [2,1], [5,6], [3,7], [4,4]]
        result = hw1.ascending_pairs(input)
        expected = [[1,2], [5,6], [3,7], [4,4]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        input = [ [4,1], [6,-5], [0], [4,10]]
        result = hw1.ascending_pairs(input)
        expected = [[1,4], [-5,6], [4,10]]
        self.assertEqual(expected, result)
    # Part 4
    def test_add_prices_1(self):
        price1 = data.Price(4, 25)
        price2 = data.Price(5, 75)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(10, 0)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        price1 = data.Price(5, 65)
        price2 = data.Price(10, 73)
        result = hw1.add_prices(price1, price2)
        expected = data.Price(16, 38)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_area_1(self):
        rect = data.Rectangle(data.Point(5.0, 10.0), data.Point(4.25, 2))
        result = hw1.rectangle_area(rect)
        expected = 6.0
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        rect = data.Rectangle(data.Point(-7.0, 10.0), data.Point(4, 3.50))
        result = hw1.rectangle_area(rect)
        expected = 71.5
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        author_name = "Irina"
        books = [data.Book(["Irina"], "Fairy Tales")]
        result = hw1.books_by_author(author_name, books)
        expected = ["Fairy Tales"]
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        author_name = "Irina"
        books = [data.Book(["Sarg"], "Fairy Tales")]
        result = hw1.books_by_author(author_name, books)
        expected = []
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_1(self):
        rect = data.Rectangle(data.Point(0, 2), data.Point(4, 0))
        result = hw1.circle_bound(rect)
        expected = data.Circle(data.Point(2,1), 1)
        self.assertEqual(expected, result)

    def test_circle_bound_2(self):
        rect = data.Rectangle(data.Point(0, -2), data.Point(-4, 0))
        result = hw1.circle_bound(rect)
        expected = data.Circle(data.Point(-2.0,-1.0), 1)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average_1(self):
        pay = [data.Employee("Irina", 20), data.Employee("Jack", 16)]
        result = hw1.below_pay_average(pay)
        expected = ["Jack"]
        self.assertEqual(expected, result)

    def test_below_pay_average_2(self):
        pay = [data.Employee("Austin", 0), data.Employee("Phil", 10)]
        result = hw1.below_pay_average(pay)
        expected = ["Austin"]
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()
