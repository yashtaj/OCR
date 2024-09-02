Django OCR Application - ReadMe

Overview:
This project is a Django web application that performs Optical Character Recognition (OCR) on uploaded images. 
The extracted text is displayed on a results page, and users can download the text as a .txt or .pdf file. The extracted text is also stored in a SQLite database.

Steps Taken:

1.Setting Up the Django Project:

    Created a new Django project and app.
    Configured the necessary settings for the project.

2.OCR Implementation:

    Installed Tesseract OCR and pytesseract for text extraction.
    Developed a form for image upload and integrated webcam functionality to capture images directly.
    Processed the uploaded/captured images to extract text using Tesseract.

3.Displaying Results:
    Displayed the extracted text on the results page.
    Added functionality to download the extracted text as a .txt or .pdf file.

4.Database Integration:
    Configured the project to use SQLite for storing the extracted text and related metadata.
    Created a model to store the text, image name, and timestamp.

5.Styling:
    Enhanced the appearance of the homepage and results page using CSS.

    

Installation and Setup:

1.Prerequisites:
    Python 3.8 or higher.
    Django 3.2 or higher.
    Tesseract OCR installed.

2.Installation Steps:
    Clone the project repository.
    Install the required Python packages using pip.
    Set up Tesseract OCR by installing it and adding it to the system PATH.
    Apply the database migrations using Django's migration commands.
    Run the Django development server to start the application.

3.Viewing Stored Data:
    Open the db.sqlite3 file using DB Browser for SQLite.
    The extracted text is stored in the ocr_app_extractedtext table.



How to Run the Project:

1.Navigate to the Project Directory:
    Open a terminal or command prompt.
    Use cd to change the directory to the project folder.

2.Apply Migrations:
    Run python manage.py migrate to apply the database migrations.
    

3.Start the Development Server:
    Run 'python manage.py runserver'.
    Open your browser and go to http://127.0.0.1:8000/.

4.Upload Images and View Results:
    Upload an image or capture one using your webcam.
    The extracted text will be displayed on the results page.

5.Download and View Stored Data:
    Download the text as a .txt or .pdf file.
    View the stored data in the SQLite database using DB Browser for SQLite.

