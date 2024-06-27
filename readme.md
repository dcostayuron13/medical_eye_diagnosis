# Create virtual environment (replace 'myvenv' with your desired name)
python -m venv myvenv

# Activate virtual environment
# Windows
myvenv\Scripts\activate

# macOS/Linux
source myvenv/bin/activate

# Install Django
pip install -r requirements.txt


# Create Django project 
django-admin startproject medical_diagnosis

# Change directory
cd medical_diagnosis

# Run development server
python manage.py runserver

# Deactivate virtual environment (when done)
deactivate  # Windows
source deactivate  # macOS/Linux
