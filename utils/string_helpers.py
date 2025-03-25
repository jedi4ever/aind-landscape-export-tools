def clean_name(name):
    """
    Clean a string to only contain alphanumeric characters in lowercase.
    
    Args:
        name (str): The string to clean
        
    Returns:
        str: The cleaned string in lowercase with only alphanumeric characters
    """
    # remove all non-alphanumeric characters
    # but keep spaces and replace them with underscores
    return ''.join(char for char in name if char.isalnum() or char == ' ').lower().replace(' ', '_') 