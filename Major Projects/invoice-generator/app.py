from weasyprint import HTML
import os

html = HTML('template/test.html', base_url=os.path.abspath('.'))
html.write_pdf('test_output.pdf')
print("Test PDF generated.")
