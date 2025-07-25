import json
import os
import sys
from contact_object import Personal_contact, Business_contact

def show_menu(): 
    print("Smart Contacts Manager".center(50, "="))
    print("1. Add Personal Contact")
    print("2. Add Business Contact")
    print("3. Search Contacts")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
def add_personal_contact(personal_contacts_list): 
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    bithday = input("Birthday (YYYY-MM-DD): ")
    print(f"Personal contact '{name}' added successfully!")
    contact = Personal_contact(name, phone, email, bithday)
    personal_contacts_list.append(contact)

def add_business_contact(business_contacts_list): 
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    company = input("Company: ")
    job_title = input("Job Title (optional): ")
    print(f"Business contact '{name}' added successfully!")
    contact = Business_contact(name, phone, email, company, job_title)
    business_contacts_list.append(contact)

def search_contacts(personal_contacts_list=[], business_contacts_list=[]): 
    search_term = input("Search term:")
    search_contacts = personal_contacts_list + business_contacts_list
    while True: 
        base_search_contacts = search_contacts.copy()
        for contact in search_contacts: 
            if search_term.lower() not in contact.get_name().lower() and search_term.lower() not in contact.get_email().lower() and search_term.lower() not in contact.get_phone().lower():
                search_contacts.remove(contact)
                
        if not search_contacts:
            print("No contacts found with that search term.\nPlease try again.")
            search_term = input("Add another search term or 'quit' searching : ")
            if search_term.lower().strip() == 'quit': 
                return 
            search_contacts = base_search_contacts.copy()
            continue
        
        for i in range(len(search_contacts)):
            contact = search_contacts[i]
            print(f"[{i + 1}]", end=' ')
            contact.show_contact_info()                    
        continue_search = input("Continue searching? (y/n): ") 
        if continue_search.strip().lower() != 'y':
            break
        search_contacts = personal_contacts_list + business_contacts_list
        search_term = input("Add another search term or 'quit' searching : ")
        if search_term.lower().strip() == 'quit':
            return 
        

def update_contact(personal_contacts_list, business_contacts_list): 
    contact_list = input("Which contact list to update? (1 for Personal, 2 for Business): ")
    if contact_list == '1':
        search_contacts(personal_contacts_list)
        index_contact = int(input("Enter the index of the contact to update: ")) 
        contact = personal_contacts_list[index_contact - 1]
        contact.show_contact_info()
        element_to_update = input("What do you want to update? (name, phone, email, birthday): ").split(',')

        for element in element_to_update:
            element = element.strip().lower()
            if element == 'name':
                new_name = input("Enter new name: ")
                contact.change_name(new_name)
            elif element == 'phone':
                new_phone = input("Enter new phone: ")
                contact.change_phone(new_phone)
            elif element == 'email':
                new_email = input("Enter new email: ")
                contact.change_email(new_email)
            elif element == 'birthday':
                new_birthday = input("Enter new birthday (YYYY-MM-DD): ")
                contact.change_birthday(new_birthday)
            else:
                print(f"Invalid field '{element}' to update.")
        print(f"Contact '{contact.get_name()}' updated successfully!")
        contact.show_contact_info()
    else : 
        search_contacts(business_contacts_list)
        index_contact = int(input("Enter the index of the contact to update: "))
        contact = business_contacts_list[index_contact - 1]
        contact.show_contact_info()
        element_to_update = input("What do you want to update? (name, phone, email, company, job title): ").split(',')
        for element in element_to_update.lower().strip():
            if element == 'name':
                new_name = input("Enter new name: ")
                contact.change_name(new_name)
            elif element == 'phone':
                new_phone = input("Enter new phone: ")
                contact.change_phone(new_phone)
            elif element == 'email':
                new_email = input("Enter new email: ")
                contact.change_email(new_email)
            elif element == 'company':
                new_company = input("Enter new company: ")
                contact.change_company(new_company)
            elif element == 'job title':
                new_job_title = input("Enter new job title: ")
                contact.change_job_title(new_job_title)
            else:
                print(f"Invalid field '{element}' to update.")
        print(f"Contact '{contact.get_name()}' updated successfully!")
        contact.show_contact_info()    

def delete_contact(personal_contacts_list, business_contacts_list): 
    contact_list = input("Which contact list to delete from? (1 for Personal, 2 for Business): ")
    if contact_list == '1':
        search_contacts(personal_contacts_list)
        index_contact = int(input("Enter the index of the contact to delete: "))
        del personal_contacts_list[index_contact - 1]
        print("Contact deleted successfully!")
    else:
        search_contacts(business_contacts_list)
        index_contact = int(input("Enter the index of the contact to delete: "))
        del business_contacts_list[index_contact - 1]
        print("Contact deleted successfully!")

def save_personal_contacts(personal_contacts_list, filename='personal_contacts.json'):
    with open("personal_contacts.json", "w") as file: 
        json.dump([contact.to_dict() for contact in personal_contacts_list], file, indent = 4)

def save_business_contacts(business_contacts_list, filename = 'business_contacts.json'):
    with open("business_contacts.json", "w") as file: 
        json.dump([contact.to_dict() for contact in business_contacts_list], file, indent = 4)
        
def load_personal_contacts(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file: 
            data = json.load(file)
        return [Personal_contact.from_dict(item) for item in data]
    else:
        return []

def load_business_contacts(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file: 
            data = json.load(file)  
        return [Business_contact.from_dict(item) for item in data]
    else: 
        return []
    
def main(): 
    business_contacts_list = load_business_contacts("business_contacts.json")
    personal_contacts_list = load_personal_contacts("personal_contacts.json")
    show_menu()
    while True:
        choice = input("Select option (1-6): ")
        if choice == '1':
            add_personal_contact(personal_contacts_list)
        elif choice == '2':
            add_business_contact(business_contacts_list)
        elif choice == '3':
            search_contacts(personal_contacts_list, business_contacts_list)
        elif choice == '4':
            update_contact(personal_contacts_list, business_contacts_list)
        elif choice == '5':
            delete_contact(personal_contacts_list, business_contacts_list)          
        elif choice == '6':
            print("Exiting the Contacts Manager. Goodbye!")
            save_personal_contacts(personal_contacts_list)
            save_business_contacts(business_contacts_list)
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__": 
    main()