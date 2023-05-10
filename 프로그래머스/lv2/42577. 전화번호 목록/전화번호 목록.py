def solution(phone_book):
    answer = True
    phone_book.sort()
    for index in range(len(phone_book)-1):
        k = len(phone_book[index])
        if phone_book[index] == phone_book[index+1][:k]:
            return False
    return answer