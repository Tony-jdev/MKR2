# Setup Instructions
## 1. Clone the Repository
Clone the project repository to your local machine:
```
git clone <repository-url>
cd MKR2
```
## 2. Set Up Virtual Environment
Create and activate a virtual environment to manage dependencies:
- Linux/Mac:
```
python3 -m venv venv
source venv/bin/activate
```
- Windows:
```
python -m venv venv
venv\Scripts\activate
```
## 3. Install Dependencies
Install the required Python packages from requirements.txt:
```
pip install -r requirements.txt
```
## 4. Apply Migrations
Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```
## 5. Create a Superuser (Optional)
To access the Django admin panel, create a superuser:
```
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.
# Running the Server
Start the Django development server to run the application locally:
```
python manage.py runserver
```
Access the app at http://127.0.0.1:8000/. The admin panel is available at http://127.0.0.1:8000/admin/

# Running Tests
Unit tests are located in recipe/tests/. Run them to verify the functionality of views and models:
```
python manage.py test recipe.tests
```
