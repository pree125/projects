# methods of function
print(dir('pree'))

email_address = ' proboda_senarathne@berkeley.edu is an email'

pos_at = email_address.find('@')

print(pos_at)

pos_space = email_address.find(' ', pos_at)

print(pos_space)


print(email_address[pos_at+1:pos_space])

str = 'X-DPAM-Confidence: 0.875 '

pos_colon = str.find(':')
number = float(str[pos_colon+1:])
print(number, type(number))



