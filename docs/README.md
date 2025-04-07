# HTML Link Replacer

A user-friendly GUI application for replacing links in HTML content. This tool allows you to easily find and replace specific patterns in HTML links while preserving the rest of the HTML structure.

## Directory Structure

```
HTML Link Replacer/
├── src/                    # Source code
│   ├── html_link_replacer.py  # Main application
│   ├── setup.py              # Package configuration
│   └── requirements.txt      # Python dependencies
├── docs/                   # Documentation
│   └── README.md            # This file
├── scripts/                # Helper scripts
│   ├── create_desktop_launcher.sh  # Desktop launcher creator
│   └── HTML Link Replacer.applescript
└── resources/              # Additional resources
```

## Features

- Modern and intuitive graphical user interface
- Load HTML from files or paste directly
- Process multiple links at once
- Generate individual HTML files for each link
- Automatic filename generation from URLs
- Preview changes before saving
- Save processed HTML to specified output folder

## Installation

1. Make sure you have Python 3.x installed on your system
2. Navigate to the source directory:
   ```bash
   cd src
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Launch the application from the src directory:
   ```bash
   cd src
   python html_link_replacer.py
   ```

2. Using the application:
   - Select an input HTML file using the "Browse" button
   - Choose an output folder for the generated files
   - Paste your links (one per line) in the text area
   - Click "Generate HTML Files" to process

3. The application will:
   - Process each link
   - Create individual HTML files
   - Name files based on the URL structure
   - Save all files to your chosen output folder

## Example

If you have HTML with links like:
```html
<a href="https://example.com/#####">Click here</a>
```

And you paste multiple links like:
```
https://secure.winred.com/1776-project-pac/tuckernucleararrest-tuckerarrestem-em-tv
https://secure.winred.com/another-project/another-campaign
```

The application will:
1. Create separate HTML files for each link
2. Name them appropriately (e.g., `1776-project-pac_tuckernucleararrest-tuckerarrestem-em-tv.html`)
3. Replace the ##### placeholder in each file with the corresponding link

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have suggestions for improvements, please check the log file at `~/Desktop/html_link_replacer.log` or open an issue on the project's repository. 