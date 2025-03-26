"""
Main module for the project.
"""
from typing import List, Dict, Any


def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    return a + b


def get_user_info() -> Dict[str, Any]:
    """Get user information.
    
    Returns:
        Dictionary containing user information
    """
    return {
        "name": "Example User",
        "email": "user@example.com",
        "age": 30,
        "is_active": True
    }


def main() -> None:
    """Main function."""
    result = add_numbers(5, 10)
    print(f"The result is: {result}")
    
    user = get_user_info()
    print(f"User: {user['name']}")


if __name__ == "__main__":
    main()