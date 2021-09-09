username=input('pls enter ur username: ')
password=input('enter ur password: ')
print('ur username:',username, 'ur password:',password)

# we can arrive at this in another way, called 'the string format method'
result='username:{} password:{}'.format(username,password)
print(result)

# we can also use another method called 'the string intercollation'
result2= f'username: {username}  password: {password}' 
print(result2)


# to run a test to dictate the criteria for a password
pass_len=len(password)
if pass_len !=5:
    print('password must be 5 characters only')
else:
    print('welcome')
#          or
pass_len=len(password)
if pass_len !=5:
    print('password must be 5 characters only')
else:
    first_five=username[0:5]
    if first_five==password:
        print('registration successfull')
    else:
        print('password must be first 5 characters of username')

# to run a test to dictate criteria for password and username length
pass_len=len(password)
user_len=len(username)
if pass_len !=5 or user_len <5:
    print('ERROR')
    print('username does not meet length criteria(5 characters)')
    print('password must be 5 characters only')
else:
    first_five=username[0:5]
    if first_five==password:
        print('registration successfull')
    else:
        print('password must be first 5 characters of username')

#Another format on achieving the above criteria
username = input("Enter your username: ")
password = input("Enter your password: ")


if len(password) == 5:
    usernameFirstFiveCharater = ""
    for x in username:
        usernameFirstFiveCharater = usernameFirstFiveCharater + x
        if username.index(x) == 4:
            break

    if password == usernameFirstFiveCharater:
        print("GOOD TO GO")
    else:
        print("Password must be the first five characters of username")

else:
    print("Password cannot be more than five charaters")
