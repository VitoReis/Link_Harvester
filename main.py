import requests
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

init_page = 1
end_page = 747


def toPDF():
    global init_page, end_page
    pdf_filename = "Book.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    for i in range(init_page, end_page):
        print(f'Adding page {i}...')
        image_path = f'images/Page_{i}.jpg'
        c.drawImage(image_path, 0, 0, width=letter[0], height=letter[1])
        c.showPage()
    c.save()


def download():
    global init_page, end_page
    for i in range(init_page, end_page):
        output_filename = os.path.join('images', f'Page_{i}.jpg')
        url = f'https://slides.com/page-{i}.jpg'
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_filename, 'wb') as f:
                f.write(response.content)
            print(f'Page {i} download completed. File saved as {output_filename}')
        else:
            print(f'Page {i} download error. Status code: {response.status_code}')


def main():
    if 'images' not in os.listdir():
        os.mkdir('images')
    download()
    toPDF()


if __name__ == '__main__':
    main()
