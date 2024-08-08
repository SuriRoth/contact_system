import json

contacts = []
            
def saveToFile(contacts):
    with open('contacts.txt', 'w') as file:
        json.dump(contacts, file, indent=4)
        
def addContact(newContact):
    contacts.append(newContact)
    print('Contact saved successfully! \n')
        
def updateContact(contacts):
    contactName = input('Which contact would you like to update?')
    for contact in contacts:
        if contact['name'] == contactName:
            contact['phone'] = input('Enter a new phone number: ')
            contact['email'] = input('Enter the new email address: ')
            saveToFile(contacts)
            print('Contact Updated successfully!')
            return
    print('Contact not found. ')
            
def removeContact(contacts):
    contactToDelete = input('Which contact would you like to delete?')
    for contact in contacts:
        if contact['name'] == contactToDelete:
            contacts.remove(contact) 
            print('Contact removed.')
            saveToFile(contacts)
            return
    print('Contact not found')
        
def viewContact(contacts):
    contactToView = input('Which contact would you like to see?')
    for contact in contacts:
        if contact['name'] == contactToView:
            print(contact)
            return 
    print('Contact not found')
    
def loadContactFromFile(contacts):
    with open('contacts.txt', 'r') as file:  
        contacts.clear()   
        contacts.extend(json.load(file))  
        for contact in contacts:
            print (contact, '\n')
        
def newChoice():
    while True:
        choice2 = input('What would you like to do now? \n'
                        '1. Exit \n'
                        '2. Go back to the main menu \n')
        if choice2 == '1':
            return True 
        elif choice2 == '2':
            print('Going back to the main menu...')
            return False
        else: 
            print('Invalid choice. Please choose again')    
           
while True:       
    choice = input('Welcome to the contacts app! Please choose from the following options: \n'
                   '1. Add a new contact \n'
                   '2. Update an existing contact \n'
                   '3. Remove a contact \n'
                   '4. Search and view a contact \n'
                   '5. View all contacts \n')
    
    if choice == '1':
        newContact = {
            'name': input('Enter a name to add to your contacts: \n'),
            'phone': input('Please enter a phone number: \n'),
            'email': input('Please enter an email address: \n')
        }
        addContact(newContact)
        saveToFile(contacts)
        if newChoice():
            break
        
    elif choice == '2':
        updateContact(contacts)
        if newChoice():
            break
        
    elif choice == '3':
        removeContact(contacts)
        if newChoice():
            break
            
    elif choice == '4':
        viewContact(contacts)
        if newChoice():
            break
                
    elif choice == '5':
        loadContactFromFile(contacts)
        if newChoice():
            break
                
    else:
        print('Invalid choice. Exiting app. \n')    
        break
