"""
SSN Format Generator Application

A GUI application built with Python and tkinter that generates valid
Social Security Number format strings for educational purposes.
"""

from random import randint
from typing import Optional
import tkinter as tk


def is_valid_ssn_format(ssn: str) -> bool:
    """
    Validates if a string matches the criteria for a valid SSN format.
    
    Validation rules:
    - Must be exactly 9 digits
    - First digit cannot be 9
    - First three digits cannot be 000 or 666
    - Middle two digits cannot be 00
    - Last four digits cannot be 0000
    
    Args:
        ssn: A string of 9 digits to validate
        
    Returns:
        True if the string matches valid SSN format criteria, False otherwise
    """
    if not isinstance(ssn, str):
        return False
    if len(ssn) != 9:
        return False
    if ssn[0] == '9':
        return False
    if ssn[:3] == '666':
        return False
    if ssn[:3] == '000':
        return False
    if ssn[3:5] == '00':
        return False
    if ssn[5:] == '0000':
        return False
    return True


def generate_ssn_format(output_label: tk.Label, event: Optional[tk.Event] = None) -> None:
    """
    Generates a valid SSN format string and displays it in the GUI.
    
    Continuously generates random 9-digit strings until one passes
    validation, then formats it as XXX-XX-XXXX and displays it.
    
    Args:
        output_label: The tkinter Label widget to display the result
        event: Optional tkinter event (for button binding)
    """
    is_valid = False
    while not is_valid:
        digits = [randint(0, 9) for _ in range(9)]
        ssn_string = ''.join(map(str, digits))
        
        if is_valid_ssn_format(ssn_string):
            is_valid = True
            formatted_ssn = f"{ssn_string[:3]}-{ssn_string[3:5]}-{ssn_string[5:]}"
            output_label.config(text=formatted_ssn)


def create_window() -> tk.Tk:
    """
    Creates and configures the main application window.
    
    Returns:
        Configured tkinter root window
    """
    window = tk.Tk()
    window.title('SSN Format Generator')
    window.config(bg='black')
    
    # Window dimensions
    width = 200
    height = 100
    
    # Center window on screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int(screen_width / 2 - width / 2)
    y = int(screen_height / 2 - height / 2)
    
    window.geometry(f'{width}x{height}+{x}+{y}')
    
    return window


def main() -> None:
    """Main entry point for the application."""
    root = create_window()
    
    # Output label
    output_label = tk.Label(root, text='', fg='red', bg='black')
    output_label.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    
    # Generate button
    generate_button = tk.Button(
        root,
        text='Generate',
        highlightbackground='black',
        bg='black',
        fg='#39ff14'
    )
    generate_button.bind('<Button-1>', lambda e: generate_ssn_format(output_label, e))
    generate_button.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    
    root.mainloop()


if __name__ == '__main__':
    main()
