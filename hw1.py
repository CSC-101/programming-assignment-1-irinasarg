import data
import math

# Write your functions for each part in the space below.

# Part 1
def vowel_count(str):
    vowel_count = ['a', 'e', 'i', 'o', 'u']
    new_string = str.lower()
    count = 0
    for x in new_string:
        if x in vowel_count:
            count += 1
    return count

# Part 2
def short_lists(lst: list[list[int]]) -> list[list[int]]:
    result = []
    for inside_list in lst:
        if len(inside_list) == 2:
            result.append(inside_list)
    return result

# Part 3
def ascending_pairs(lst: list[list[int]]) -> list[list[int]]:
    result = []
    for inside_list in lst:
        if len(inside_list) == 2:
            if inside_list[0] > inside_list[1]:
                inside_list[0], inside_list[1] = inside_list[1], inside_list[0]
            result.append(inside_list)
    else:
        return result

# Part 4
def add_prices(price1: data.Price, price2: data.Price ) -> data.Price:
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents
    if total_cents >= 100:
        total_dollars += total_cents//100
        total_cents = total_cents % 100
    return data.Price(total_dollars, total_cents)

# Part 5
def rectangle_area(rect: data.Rectangle) -> float:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y
    area = width * height
    if area < 0:
        area = area * -1
    return area

# Part 6
def books_by_author(author_name: str, books: list[data.Book]) -> list[data.Book]:
    wantedbook = []
    for book in books:
        for author in book.authors:
            if author == author_name:
                wantedbook.append(book.title)
    return wantedbook

# Part 7
def circle_bound(rect: data.Rectangle) -> data.Circle:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y
    x = rect.top_left.x + (width / 2)
    y = rect.top_left.y - (height / 2)
    if width < 0:
        width = width * -1
    if height < 0:
        height = height * -1
    if width < height:
        radius = width / 2
    else:
        radius = height / 2
    return data.Circle(data.Point(x, y), radius)

# Part 8
def below_pay_average(lst: list[data.Employee]) -> list[str]:
    pay = 0
    names = []
    for employee in lst:
        pay = pay + employee.pay_rate
    avg = pay / len(lst)
    for employee in lst:
        if employee.pay_rate < avg:
            names.append(employee.name)
    return names



