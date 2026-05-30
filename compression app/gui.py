# gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from logic import generate_password_core, generate_email_core

class PasswordGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password & Email Generator 🔐")
        self.root.geometry("500x600")
        
        # خلفية لونها حلو
        self.root.configure(bg='#2c3e50')
        
        # Style للعناصر
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TLabel', background='#2c3e50', foreground='white', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10, 'bold'))
        style.configure('TCheckbutton', background='#2c3e50', foreground='white', font=('Arial', 9))
        style.configure('Header.TLabel', font=('Arial', 14, 'bold'), background='#2c3e50', foreground='#3498db')
        
        # متغيرات Password
        self.length_var = tk.IntVar(value=12)
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=False)
        self.password_output = tk.StringVar()
        
        # متغيرات Email
        self.add_numbers_var = tk.BooleanVar(value=True)
        self.email_output = tk.StringVar()
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame رئيسي
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # ═══════════════════════════════════════
        # قسم الـ Password
        # ═══════════════════════════════════════
        password_frame = tk.LabelFrame(main_frame, text=" 🔒 Password Generator ", 
                                       bg='#34495e', fg='#ecf0f1', 
                                       font=('Arial', 12, 'bold'), padx=15, pady=15)
        password_frame.pack(fill='x', pady=(0, 20))
        
        # Length
        length_frame = tk.Frame(password_frame, bg='#34495e')
        length_frame.pack(fill='x', pady=5)
        ttk.Label(length_frame, text="Length:").pack(side='left')
        ttk.Entry(length_frame, textvariable=self.length_var, width=10).pack(side='left', padx=10)
        
        # Checkboxes
        ttk.Checkbutton(password_frame, text="Lowercase (a-z)", variable=self.lower_var).pack(anchor='w', pady=2)
        ttk.Checkbutton(password_frame, text="Uppercase (A-Z)", variable=self.upper_var).pack(anchor='w', pady=2)
        ttk.Checkbutton(password_frame, text="Digits (0-9)", variable=self.digits_var).pack(anchor='w', pady=2)
        ttk.Checkbutton(password_frame, text="Symbols (!@#$...)", variable=self.symbols_var).pack(anchor='w', pady=2)
        
        # Generate Button
        ttk.Button(password_frame, text="🎲 Generate Password", 
                  command=self.generate_password).pack(pady=10)
        
        # Output
        output_frame = tk.Frame(password_frame, bg='#34495e')
        output_frame.pack(fill='x')
        password_entry = ttk.Entry(output_frame, textvariable=self.password_output, 
                                   font=('Courier', 11), width=35)
        password_entry.pack(side='left', fill='x', expand=True)
        ttk.Button(output_frame, text="📋", width=3, 
                  command=lambda: self.copy_to_clipboard(self.password_output.get())).pack(side='left', padx=5)
        
        # ═══════════════════════════════════════
        # قسم الـ Email
        # ═══════════════════════════════════════
        email_frame = tk.LabelFrame(main_frame, text=" 📧 Gmail Generator ", 
                                    bg='#34495e', fg='#ecf0f1', 
                                    font=('Arial', 12, 'bold'), padx=15, pady=15)
        email_frame.pack(fill='x')
        
        # Add Numbers
        ttk.Checkbutton(email_frame, text="Add Numbers", variable=self.add_numbers_var).pack(anchor='w', pady=5)
        
        # Generate Button
        ttk.Button(email_frame, text="🎲 Generate Gmail", 
                  command=self.generate_email).pack(pady=10)
        
        # Output
        email_output_frame = tk.Frame(email_frame, bg='#34495e')
        email_output_frame.pack(fill='x')
        email_entry = ttk.Entry(email_output_frame, textvariable=self.email_output, 
                               font=('Courier', 11), width=35)
        email_entry.pack(side='left', fill='x', expand=True)
        ttk.Button(email_output_frame, text="📋", width=3, 
                  command=lambda: self.copy_to_clipboard(self.email_output.get())).pack(side='left', padx=5)
    
    def generate_password(self):
        try:
            pwd = generate_password_core(
                self.length_var.get(),
                self.lower_var.get(),
                self.upper_var.get(),
                self.digits_var.get(),
                self.symbols_var.get(),
            )
            self.password_output.set(pwd)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def generate_email(self):
        try:
            email = generate_email_core(self.add_numbers_var.get())
            self.email_output.set(email)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def copy_to_clipboard(self, text):
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            messagebox.showinfo("✓", "Copied to clipboard!")
