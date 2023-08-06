def Capitalise(f_name, l_name) :
    if f_name == '' or l_name == '' :
        return 'Provide a valid input '
    firstname = (f_name.title())
    lastname = (l_name.title())
    return f'{firstname} {lastname}'
print(Capitalise(input('Enter your first name : '),input('Enter your last name : ')))