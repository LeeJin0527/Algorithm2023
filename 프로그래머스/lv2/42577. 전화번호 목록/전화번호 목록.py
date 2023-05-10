def solution(phone_book):
    answer = True
    book = {}
    for phone in phone_book:
        book[phone] = 1

    for phone_number in book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in book and temp != phone_number:
                return False
    return answer 