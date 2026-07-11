users_db = []

def register_user(username, email, age):
    if age < 18:
        return 'Registration failed: age must be 18 or older.'
    
    user = {'username': username, 'email': email, 'age': age}
    users_db.append(user)
    
    return f'User {username} registered successfully!'

# Pass the parameters in any way to register a user
result1 = register_user('a_m','a@b.com',18)

# Testing the result
print(result1)
print(users_db)  # List of registered users
