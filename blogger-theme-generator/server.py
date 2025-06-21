from flask import Flask, render_template, request, Response
import os

app = Flask(__name__)

# Path where XML templates live
TEMPLATE_DIR = os.path.join(app.root_path, 'templates')

@app.route('/')
def index():
    """Render form for user input."""
    # Collect available XML templates from the templates directory
    themes = [f for f in os.listdir(TEMPLATE_DIR) if f.endswith('.xml')]
    return render_template('index.html', themes=themes)

@app.route('/generate', methods=['POST'])
def generate():
    """Create XML from template and show preview."""
    theme = request.form.get('theme')
    blog_title = request.form.get('blog_title', '')
    author_name = request.form.get('author_name', '')
    custom_xml = request.form.get('custom_xml')

    # If user dragged in a custom file, use it instead of predefined template
    if custom_xml:
        xml_template = custom_xml
    else:
        template_path = os.path.join(TEMPLATE_DIR, theme)
        with open(template_path, 'r') as f:
            xml_template = f.read()

    # Replace placeholders with user values
    xml_output = (xml_template
                  .replace('{{blog_title}}', blog_title)
                  .replace('{{author_name}}', author_name))

    return render_template('preview.html', xml_output=xml_output)

@app.route('/download', methods=['POST'])
def download():
    """Return XML as downloadable file."""
    xml_data = request.form.get('xml_data', '')
    filename = request.form.get('filename', 'theme.xml')
    return Response(
        xml_data,
        mimetype='application/xml',
        headers={
            'Content-Disposition': f'attachment;filename={filename}'
        }
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
