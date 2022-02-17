import pyperclip


def main():
    myMessage = input('Введите текст, который хотите зашифровать: ')
    myKey = int(input('Введите ключ шифрования: '))

    ciphertext = encryptMessage(myKey, myMessage)
    print(ciphertext + "|")

    #pyperclip.copy(ciphertext)


def encryptMessage(key, message):
    ciphertext = [''] * key

    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]

            currentIndex += key

    return "".join(ciphertext)


if __name__ == '__main__':
    main()
