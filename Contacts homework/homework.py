contacts = []

def addContact():
    newContact = {
    'name': input('Enter a name to add to your contacts: \n'),
    'phone': input('Please enter a phone number: \n'),
    'email': input('Please enter an email address: \n')
    }
    contacts.append(newContact)
    saveToFile(contacts)
    
def updateContact():
    input('Enter the name of a contact you would like to update: ')
    
    
def viewContact(contacts):
    for contact in contacts:
        print(contact)
        
def saveToFile(contacts):
    with open('contacts.json', 'w') as file:
        for contact in contacts:
            json.dump(contacts, file, indent=4)
            
def loadContactFromFile(contacts):
    open('contacts.json', 'r')
    for contact in contacts:
        print(contact)
        
            
# loadContactFromFile(contacts)

while True:
    print('1. Add a contact')
    print('2. View contacts')
    print('3. Update contact')
    print('4. Update contact')
    print('5. Remove contact')
        
    choice = input('Enter your choice: \n')
        
    if choice == '1':
        addContact()
    elif choice == '2':
        viewContact(contacts)
    elif choice == '3':
        updateContact(contacts)
    elif choice == '4':
        removeContact(contacts)
    elif choice == '5':
        break
    else:
        print('Invalid choice. Please try again. \n')
        
