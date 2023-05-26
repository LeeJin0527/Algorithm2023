def solution(phone_book):

    phone_book.sort()
    check = phone_book[0]
    for phone in range(1, len(phone_book)):
        if check == phone_book[phone][:len(check)]:
            return False
        check = phone_book[phone]
    return True