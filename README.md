# 🎤 Late Show API

Flask API to manage guests, episodes & appearances. Includes JWT authentication.

---

## ⚙️ Setup

1. Clone repo & install deps:
```bash
git clone <repo_url>
cd late-show-api
pipenv install && pipenv shell
Create DB:

bash
Copy
Edit
psql -U user2
CREATE DATABASE late_show_db;
Migrate & seed:

bash
Copy
Edit
flask db init
flask db migrate -m "init"
flask db upgrade
python server/seed.py
Run server:

bash
Copy
Edit
flask run
🔐 Auth Flow
Register: POST /register

Login: POST /login → returns JWT

Use token in headers:

makefile
Copy
Edit
Authorization: Bearer <token>
📚 Routes
Method	Endpoint	Protected	Description
POST	/register	❌	Register user
POST	/login	❌	Login user
GET	/episodes	❌	List episodes
GET	/episodes/<id>	❌	Episode details
DELETE	/episodes/<id>	✅	Delete episode
GET	/guests	❌	List guests
POST	/appearances	✅	Create appearance

📬 Postman
Import challenge-4-lateshow.postman_collection.json

After login, Scripts → Tests:

js
Copy
Edit
let data = pm.response.json();
pm.collectionVariables.set("token", data.access_token);

repolink
https://github.com/petermunene/late-show-api-challenge-