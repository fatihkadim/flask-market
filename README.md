# Flask-Market

A simple Flask-based application for learning backend and frontend integration.  
It includes user registration/login and product purchasing/selling functionalities.

---

## Project Structure

| File / Folder       | Description                               |
|--------------------|-------------------------------------------|
| market/            | Main module of the application            |
| templates/         | HTML templates (with Bootstrap support)  |
| forms.py           | User forms                                |
| models.py          | Database models                           |
| routes.py          | Application routes                        |
| init.py            | Flask application and configuration       |
| run.py             | Entry point to run the application       |
| requirements.txt   | Project dependencies                       |
| LICENSE            | MIT license                               |
| README.md          | Project description (this file)          |

---

## Features

- User registration (`Register`)  
- User login / logout  
- Password security with Bcrypt hashing  
- Product purchasing and selling  
- Database operations using SQLAlchemy ORM  
- Form interactions via HTTP GET & POST  
- Frontend built with HTML + Bootstrap  

---

## Technologies Used

| Layer     | Technology                                |
|-----------|-------------------------------------------|
| Backend   | Flask, Flask-SQLAlchemy, Flask-Bcrypt, Flask-WTF |
| Frontend  | HTML5, Bootstrap                           |
| Database  | SQLite (development environment)          |

---

## Installation and Running

```bash
# Clone the repository
git clone https://github.com/fatihkadim/flask-market.git
cd flask-market

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Unix/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
Open your browser at: http://127.0.0.1:5000

```

## Environment Variables

If using a `.env` file, define:

SECRET_KEY=a_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///market.db


## Why This Project?

This project is ideal for those who want to:

- Learn backend & frontend integration with Flask
- Master user authentication and password security
- Gain practical experience in ORM-based database management

## License

This project is licensed under the MIT License.



# TR

# flask-Market

Basit bir Flask tabanlı uygulama, backend ve frontend entegrasyonunu öğrenmek için tasarlanmıştır.  
Uygulama kullanıcı kayıt/giriş ve ürün alım/satım fonksiyonlarını içerir.

---

## Proje Yapısı

| Dosya / Klasör      | Açıklama                                         |
|--------------------|-------------------------------------------------|
| market/            | Uygulamanın ana modülü                           |
| templates/         | HTML şablonları (Bootstrap desteği ile)         |
| forms.py           | Kullanıcı formları                               |
| models.py          | Veritabanı modelleri                             |
| routes.py          | Uygulama rotaları                                |
| init.py            | Flask uygulaması ve yapılandırması               |
| run.py             | Uygulamayı çalıştırmak için giriş noktası        |
| requirements.txt   | Proje bağımlılıkları                             |
| LICENSE            | MIT lisansı                                      |
| README.md          | Proje açıklaması (bu dosya)                     |

---

## Özellikler

- Kullanıcı kaydı (`Register`)  
- Kullanıcı giriş / çıkış  
- Bcrypt ile şifre güvenliği  
- Ürün alım ve satım işlemleri  
- SQLAlchemy ORM kullanarak veritabanı işlemleri  
- HTTP GET & POST ile form etkileşimleri  
- Frontend: HTML + Bootstrap  

---

## Kullanılan Teknolojiler

| Katman     | Teknoloji                                |
|-----------|------------------------------------------|
| Backend   | Flask, Flask-SQLAlchemy, Flask-Bcrypt, Flask-WTF |
| Frontend  | HTML5, Bootstrap                          |
| Veritabanı| SQLite (geliştirme ortamı)               |

---

## Kurulum ve Çalıştırma

```bash

# Depoyu klonla
git clone https://github.com/fatihkadim/flask-market.git
cd flask-market

# Sanal ortam oluştur
python -m venv venv

# Sanal ortamı aktif et
# Unix/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Uygulamayı çalıştır
python run.py
Tarayıcınızdan açın: http://127.0.0.1:5000

```

## Ortam Değişkenleri
Eğer .env dosyası kullanıyorsanız, tanımlayın:

SECRET_KEY=a_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///market.db

## Neden Bu Proje?
Bu proje, şu amaçlar için idealdir:

Flask ile backend ve frontend entegrasyonunu öğrenmek

Kullanıcı kimlik doğrulama ve şifre güvenliğini geliştirmek

ORM tabanlı veritabanı yönetimi konusunda pratik deneyim kazanmak

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
