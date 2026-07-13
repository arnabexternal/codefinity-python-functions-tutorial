def file_exists(file_system, target):
    for name, content in file_system.items():
        if content == 'file' and name == target:
            return True  # File found
        
        if isinstance(content, dict):  # If it's a folder, search deeper
            if file_exists(content, target):
                return True # If the file is found in subdirectories, return `True`
    
    return False  # File not found

# Sample file system
file_system = {
    'home': {
        'user': {
            'documents': {
                'resume.pdf': 'file',
                'notes.txt': 'file'
            },
            'photos': {
                'vacation.jpg': 'file',
                'family.png': 'file'
            }
        }
    },
    'etc': {
        'config.yaml': 'file',
        'hosts': 'file'
    }
}

# Testing the result
file_name = 'family.png'
result = file_exists(file_system, file_name)

print(result)  # Prints `True` if the file is found, otherwise `False`