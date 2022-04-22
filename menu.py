def menu(list, question):
    for item in list:
        print(list.index(item), item)
    while True:
        result = input(question)
        result = int(result)
        return result
