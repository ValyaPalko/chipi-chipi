import os

class Contact:
    def __init__(self, last_name, first_name, phone_number, description):
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.description = description

    def __str__(self):
        return f"{self.last_name}, {self.first_name}, {self.phone_number}, {self.description}"

def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    last_name, first_name, phone_number, description = line.strip().split(", ")
                    contacts.append(Contact(last_name, first_name, phone_number, description))
    return contacts

def save_contacts(filename, contacts):
    with open(filename, "w", encoding="utf-8") as file:
        for contact in contacts:
            file.write(f"{contact.last_name}, {contact.first_name}, {contact.phone_number}, {contact.description}\n")

def add_contact(contacts, last_name, first_name, phone_number, description):
    contacts.append(Contact(last_name, first_name, phone_number, description))

def search_contact(contacts, search_term):
    results = [contact for contact in contacts if search_term in contact.last_name or search_term in contact.first_name]
    return results

def update_contact(contact, last_name=None, first_name=None, phone_number=None, description=None):
    if last_name:
        contact.last_name = last_name
    if first_name:
        contact.first_name = first_name
    if phone_number:
        contact.phone_number = phone_number
    if description:
        contact.description = description

def delete_contact(contacts, contact):
    contacts.remove(contact)

def main():
    filename = "contacts.txt"
    contacts = load_contacts(filename)
    
    while True:
        print("\nТелефонный справочник")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Сохранить и выйти")
        choice = input("Выберите опцию: ")

        if choice == '1':
            for contact in contacts:
                print(contact)
        elif choice == '2':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            phone_number = input("Введите номер телефона: ")
            description = input("Введите описание: ")
            add_contact(contacts, last_name, first_name, phone_number, description)
        elif choice == '3':
            search_term = input("Введите фамилию или имя для поиска: ")
            results = search_contact(contacts, search_term)
            for result in results:
                print(result)
        elif choice == '4':
            search_term = input("Введите фамилию или имя контакта для изменения: ")
            results = search_contact(contacts, search_term)
            if results:
                contact = results[0]
                print("Контакт найден: ", contact)
                last_name = input("Введите новую фамилию (оставьте пустым, чтобы не менять): ")
                first_name = input("Введите новое имя (оставьте пустым, чтобы не менять): ")
                phone_number = input("Введите новый номер телефона (оставьте пустым, чтобы не менять): ")
                description = input("Введите новое описание (оставьте пустым, чтобы не менять): ")
                update_contact(contact, last_name, first_name, phone_number, description)
            else:
                print("Контакт не найден.")
        elif choice == '5':
            search_term = input("Введите фамилию или имя контакта для удаления: ")
            results = search_contact(contacts, search_term)
            if results:
                contact = results[0]
                print("Контакт найден и удален: ", contact)
                delete_contact(contacts, contact)
            else:
                print("Контакт не найден.")
        elif choice == '6':
            save_contacts(filename, contacts)
            print("Данные сохранены. Выход.")
            break
        else:
            print("Неверная опция. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
