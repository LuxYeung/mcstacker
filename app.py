from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

# Configuration - modify these as needed
HTML_FILES_DIRECTORY = "/opt/render/project/src/app"  # Directory where your HTML files are stored

@app.route('/')
def home():
    """Serve the index.html file for the root path"""
    try:
        return send_from_directory(HTML_FILES_DIRECTORY, 'index.html')
    except FileNotFoundError:
        return "Welcome! No index.html found.", 200

@app.route('/<path:filename>')
def serve_file(filename):
    """Serve any file from the HTML directory based on the URL path"""
    try:
        # If filename doesn't have an extension, assume it's HTML
        if '.' not in filename:
            filename += '.html'

        # Security check to prevent directory traversal
        if '..' in filename or filename.startswith('/'):
            abort(404)

        return send_from_directory(HTML_FILES_DIRECTORY, filename)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    # Create the HTML files directory if it doesn't exist
    if not os.path.exists(HTML_FILES_DIRECTORY):
        os.makedirs(HTML_FILES_DIRECTORY)
        print(f"Created directory: {HTML_FILES_DIRECTORY}")
        print("Please put your HTML files in this directory")

    print(f"Starting server...")
    print(f"Access your site at: http://localhost:5000")
    print(f"Place your HTML files in the '{HTML_FILES_DIRECTORY}' folder")
    print("Example: example.com/this -> html_files/this.html")

    app.run(host='0.0.0.0', port=5010, debug=True)
