# E-com Shop

A full-featured e-commerce application built with **Python Django** for the backend and **Bootstrap** for the frontend. This application provides a scalable and efficient platform for managing and showcasing products, featuring user authentication, product search, and tagging. It includes dynamic features such as top-rated products, related product recommendations, and most-viewed products using IP-based middleware. Users can register, log in, browse products, and track their order history seamlessly. The project is structured with separate development and production settings, modular requirement files, and an example app with a custom user model for easy deployment and customization.

### Features

- Modular project structure with separate development and production settings
- Custom user model with authentication (registration & login)
- Integrated Bootstrap for responsive UI
- Product rating and reviews
- Related product recommendations
- Most viewed products tracking using IP Middleware
- Product search functionality
- Product tagging for easy filtering
- User order history tracking

---

## Getting Started

### **1. Clone the Project**

```bash
git clone https://github.com/Anirudhmaurya1208/WebScanner.git
cd WebScanner
```

### **2. Set Up a Virtual Environment**

#### **Windows**
```bash
python -m venv env
env\Scripts\activate
```

#### **Mac/Linux**
```bash
python3 -m venv env
source env/bin/activate
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Configure the Database**

Modify `settings.py` to add your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### **5. Apply Migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Create a Superuser**

```bash
python manage.py createsuperuser
```

### **7. Run the Development Server**

```bash
python manage.py runserver
```

### **8. Access the Application**

Open your browser and navigate to:

```
http://localhost:8000
```

Now your e-commerce application is up and running! 🎉

---

## Contributing
If you would like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

---

## License
This project is licensed under the MIT License.

---

### **Need Help?**
If you encounter any issues, feel free to open an issue in the repository or reach out for support.

Happy coding! 🚀
