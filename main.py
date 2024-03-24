from docx import Document

def create_word_file():
    i=1
    while True:
        text = input("Введите текст: ")
        doc = Document()
        doc.add_paragraph(text)
        doc.save(f'file{i}.docx')
        i+=1
        print("Word файл создан")
        task = input('Хотите еще?(Y)(N): ')
        if task == 'N':
            break

if __name__ == "__main__":

    create_word_file()