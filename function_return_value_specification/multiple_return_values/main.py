def validate_registration(*validate):
    errors = []
    validation_errors_not_present = True
    if len(validate[0]) < 3:
        errors.append('Username must be at least 3 characters long.')
        validation_errors_not_present = False
    if '@' not in validate[1]:
        errors.append('Invalid email format.')
        validation_errors_not_present = False
    if len(validate[2]) < 6:
        errors.append('Password must be at least 6 characters long.')
        validation_errors_not_present = False

    return validation_errors_not_present, errors

# Testing the result
is_valid, errors = validate_registration('js', 'userexample.com', '123')
print('Validation successful:', is_valid)
print('Errors:', errors)