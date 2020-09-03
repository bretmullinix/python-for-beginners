
print ('Primitive Types to Represent Your Application ---->\n')

home_street = '50 Carter Way'
home_city = 'Springfield'
home_state = 'Virginia'
home_zip = '22150'

print('Your home address is the following:')
print('')
print('\t' + home_street)
print('\t' + home_city)
print('\t' + home_state + ', ' + home_zip)

work_street = '125 Independence Lane'
work_city = 'Tysons Corner'
work_state = 'VA'
work_zip = '22102'

print('')

print('Your work address is the following:')
print('')
print('\t' + work_street)
print('\t' + work_city)
print('\t' + work_state + ', ' + work_zip)

print('--------------------------------------------------------------------------------------------------')
from address import Address

print ('OOP to Represent Your Application ---->\n')

print('Your OOP home address is the following:')
print('')
home_address = Address('50 Carter Way', 'Springfield', 'VA', '22150')
print(home_address)

print('')
print('Your OOP work address is the following:')
print('')
work_address = Address('125 Independence Lane', 'Tysons Corner', 'VA', '22102')
print(work_address)