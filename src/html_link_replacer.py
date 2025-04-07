import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import re
from pathlib import Path
import os
import urllib.parse
import platform

class HTMLLinkReplacer:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML Link Replacer")
        self.root.geometry("800x600")
        self.root.minsize(800, 600)
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure("TButton", padding=6, relief="flat", background="#2196F3")
        self.style.configure("TLabel", padding=6)
        self.style.configure("TEntry", padding=6)
        
        # Create main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Initialize variables
        self.input_file = tk.StringVar()
        self.output_folder = tk.StringVar()
        
        # Create widgets
        self.create_widgets()
        
        # Set default values
        self.set_default_paths()
        
        # Configure menu for macOS
        if platform.system() == 'Darwin':
            self.configure_macos_menu()

    def configure_macos_menu(self):
        # Create a minimal menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Add a basic File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)

    def set_default_paths(self):
        # Set default paths to Desktop
        desktop = str(Path.home() / "Desktop")
        self.input_file.set(os.path.join(desktop, ""))
        self.output_folder.set(os.path.join(desktop, ""))

    def create_widgets(self):
        # Input file selection
        input_frame = ttk.LabelFrame(self.main_frame, text="Select Input HTML File", padding="10")
        input_frame.pack(fill=tk.X, pady=10)
        
        # Create a frame to hold the entry and button
        input_entry_frame = ttk.Frame(input_frame)
        input_entry_frame.pack(fill=tk.X, expand=True)
        
        # Create the entry with a custom style to make it look like it's readonly
        self.input_entry = ttk.Entry(input_entry_frame, textvariable=self.input_file)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.input_entry.bind('<Key>', lambda e: 'break')  # Prevent typing
        
        ttk.Button(input_entry_frame, text="Browse", command=self.select_input_file).pack(side=tk.RIGHT, padx=5)
        
        # Output folder selection
        output_frame = ttk.LabelFrame(self.main_frame, text="Select Output Folder", padding="10")
        output_frame.pack(fill=tk.X, pady=10)
        
        # Create a frame to hold the entry and button
        output_entry_frame = ttk.Frame(output_frame)
        output_entry_frame.pack(fill=tk.X, expand=True)
        
        # Create the entry with a custom style to make it look like it's readonly
        self.output_entry = ttk.Entry(output_entry_frame, textvariable=self.output_folder)
        self.output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.output_entry.bind('<Key>', lambda e: 'break')  # Prevent typing
        
        ttk.Button(output_entry_frame, text="Browse", command=self.select_output_folder).pack(side=tk.RIGHT, padx=5)
        
        # Links text area
        links_frame = ttk.LabelFrame(self.main_frame, text="Paste Links (one per line)", padding="10")
        links_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.links_text = scrolledtext.ScrolledText(links_frame, height=10, wrap=tk.WORD)
        self.links_text.pack(fill=tk.BOTH, expand=True)
        
        # Generate button
        ttk.Button(self.main_frame, text="Generate HTML Files", command=self.generate_html).pack(pady=20)

    def select_input_file(self):
        file_path = filedialog.askopenfilename(
            initialdir=self.input_file.get(),
            title="Select HTML File",
            filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
        )
        if file_path:
            self.input_file.set(file_path)
            # Update the entry to show the full path
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, file_path)

    def select_output_folder(self):
        folder_path = filedialog.askdirectory(
            initialdir=self.output_folder.get(),
            title="Select Output Folder"
        )
        if folder_path:
            self.output_folder.set(folder_path)
            # Update the entry to show the full path
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, folder_path)

    def extract_filename_from_url(self, url):
        # Remove the domain and query parameters
        path = urllib.parse.urlparse(url).path
        # Remove leading/trailing slashes and replace remaining slashes with underscores
        filename = path.strip('/').replace('/', '_')
        # Remove any file extensions
        filename = filename.split('.')[0]
        return filename

    def generate_html(self):
        # Validate inputs
        if not self.input_file.get():
            messagebox.showerror("Error", "Please select an input HTML file")
            return
            
        if not self.output_folder.get():
            messagebox.showerror("Error", "Please select an output folder")
            return
            
        links = self.links_text.get(1.0, tk.END).strip().split('\n')
        if not links or not any(link.strip() for link in links):
            messagebox.showerror("Error", "Please enter at least one link")
            return
            
        try:
            # Read input file
            with open(self.input_file.get(), 'r', encoding='utf-8') as file:
                template_html = file.read()
            
            success_count = 0
            for link in links:
                link = link.strip()
                if not link:
                    continue
                    
                # Extract filename from URL
                filename = self.extract_filename_from_url(link)
                
                # Process HTML content
                processed_html = re.sub(
                    r'<a[^>]*href="([^"]*#####[^"]*)"[^>]*>',
                    lambda m: m.group(0).replace("#####", link),
                    template_html
                )
                
                # Create output filename
                output_filename = f"{filename}.html"
                output_path = os.path.join(self.output_folder.get(), output_filename)
                
                # Save processed HTML
                with open(output_path, 'w', encoding='utf-8') as file:
                    file.write(processed_html)
                
                success_count += 1
            
            messagebox.showinfo("Success", f"Generated {success_count} HTML files successfully!\nSaved to: {self.output_folder.get()}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process HTML: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HTMLLinkReplacer(root)
    root.mainloop() 