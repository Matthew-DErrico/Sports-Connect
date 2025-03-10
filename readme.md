 # Sports Connect

**Sports Connect** is a web platform that helps sports enthusiasts connect, find teammates at a matching skill level, and organize games. Whether you're looking for casual play or competitive matches, **Sports Connect** makes it easy to build teams, track skill levels, and foster a thriving sports community.

---

## 🚀 Basic Features

- **Skill-Based Matching** – Find players with similar skill levels in your area.  
- **Team Formation** – Create or join teams for casual games or competitive events.  
- **Ratings & Reviews** – Leave feedback on teammates and past games.  
- **Real-Time Communication** – Chat and coordinate with players easily.  
- **Event Scheduling** – Plan matches and tournaments with automated reminders.  

### What Specific features will this Django Sports Connect website have available to implement?
- [x] **Production ready**: you can immediately deploy this to cloud such as Vercel, Railway.app, Render.com etc.
- [x] Comes with a default landing page that you can modify, for more landing pages visit [Awesome landing pages](https://github.com/PaulleDemon/awesome-landing-pages).
- [x] **Responsive design**: forget about making things responsive yourself, as it includes responsive `base.html`, you can extend from.
- [x] **Pricing page**: Comes with a basic pricing page you can modify
- [x] **Postgres DB ready**: Comes with postgres Db configuration for production
- [x] **ESP**: use transactional emails at scale (sending email notifications)
- [x] **Modern admin:** uses unfold admin module.
- [x] **Payment integration:** Default Stripe integration, just add your stripe keys and get started
- [x] Recurring charges
- [x] **Custom user model:** Easily modify the user model.
- [x] **Login and Signup flow:** Including, verification email, resend token, password reset.
- [x] **Blog:** Has blog with Trix WYSIWYG editor built into the admin panel.
- [x] **Contact us:** Contact page and model to manage customer enquires.
- [x] 404 page
- [x] Technical SEO optimization.
- [x] Dynamic Sitemap.xml
- [x] Robots.txt
- [x] Google analytics
- [x] **Django storages:** Storage integration for production (default Google Object storage)
- [x] **Tailwind css:** setup for rapid development (note: the tailwind classes are prefixed with `tw-`, to differentiate them)
- [ ] **CLI Wizard:** Customize your setup with CLI wizard (upcoming)

### Demo
Visit the demo site: [Django Demo website](https://django-saas-boilerplate.vercel.app/)

For admin and login use.
```
demo@mail.com
demo123*
```
>[!NOTE]
> You will not receive any confirmation email upon signup as its disabled, use the above account to login to admin dashboard

For testing stripe check out test cards: https://docs.stripe.com/testing

---

## 🛠 Tech Stack

| **Technology**  | **Usage** |
|----------------|----------|
| Django        | Backend Framework |
| Python        | Programming Language |
| PostgreSQL    | Database |
| Django Templates | Frontend |
| Git & GitHub  | Version Control |
| GitHub Projects | Project Management |

## 📖 Getting Started

### 1️⃣ Local development

follow the below steps :
1. Star the repo: https://github.com/PaulleDemon/Django-SAAS-Boilerplate
   
2. Clone the repo
`git clone https://github.com/PaulleDemon/Django-SAAS-Boilerplate`

3. Install python 3.8 or above.
https://www.python.org/downloads/

4. Open the template folder and from the terminal change the
directory to the current working directory.
`cd home/Template`

5. Install dependencies in an environment (creating an
enviornment is optional, but recommended)
```
pip install -r requirements.txt
```

6. Add a `.env` file inside the `project` folder with the following
```py
DEBUG=1
PYTHON_VERSION=3.10
DOMAIN=""

ALLOWED_HOSTS=".up.railway.app"
ALLOWED_CORS=""

SECRET_KEY=""
PORD_SECRET_KEY=""

DJANGO_SUPERUSER_EMAIL="" # optonal use if you want to create supruser using --noinput
DJANGO_SUPERUSER_PASSWORD="" # optonal use if you want to create supruser using --noinput

EMAIL_HOST="smtpout.server.net"
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""

POSTGRES_DATABASE=""
POSTGRES_USER=""
POSTGRES_PASSWORD=""
POSTGRES_HOST=""

POSTGRES_URL=""

PROJECT_ID="" # firebase project id
BUCKET_NAME=".appspot.com" # firebase storage name
FIREBASE_CRED_PATH="project/firebase-cred.json"

FIREBASE_ENCODED=""
CLOUD_PLATFORM="RAILWAY"

GOOGLE_ANALYTICS="G-"

STRIPE_TEST_API_KEY=""
STRIPE_WEBHOOK_TEST_API_KEY=""
STRIPE_PUB_TEST_KEY=""

STRIPE_PROD_API_KEY=""
STRIPE_WEBHOOK_PROD_API_KEY=""
STRIPE_PUB_PROD_KEY=""
```

7. Now in your terminal Create databases and Tables using
```
python manage.py migrate
```
Your database is created and ready to use.

8. Now run the website from the terminal using.
```py
python manage.py runserver
```
Your website should be available at: http://localhost:8000/

9. To run Tailwind CSS open a new terminal and run
```py
python manage.py tailwind start
```

**Note:** If you are facing problems starting this program in windows OS, remove logging from project/settings.py

### Admin superuser
To create a admin superuser use the following in terminal
```py
python manage.py createsuperuser
```

#### changing example.com to localhost/yourdomain
If you are sending reset email you may notice its being sent from example.com, inorder to 
change that you need to go to admin dashboard and from sites, change to your domain

![site name](demo/images/site-change.png)

### Customizing

All html, css, js and assets lies inside the templates.
- To modify the landing page, update `home.html`.
- To add link to header and footer or modify head tags, check `base.html`.
- extend `base.html` to have the same footer and header.

#### Adding title, description to page
To add title and meta tags to a page use the following tags
```py
{% block title %}lorem impsum {% endblock title %}
{% block description %}lorem impsum{% endblock description %} #meta description

{% block socialTitle %}{{blog.title}} | {% endblock socialTitle %} # open graph title, for socials
{% block socialDescription %}{{blog.meta_description}}{% endblock socialDescription %} # open graph description, for socials
{% block pageType %}article{% endblock pageType %}
{% block pageImage %}{% endblock pageImage %} # social image
```

To add additional head tags

```py
{% block head_tags %}lorem impsum {% endblock head_tags %}
```
To add scripts at the end of the elements
```
{% block scripts %}
    <script src="{% static "" %}" />
{% endblock scripts %}
```

### Payment - Stripe
By default it is set up to use Stripe you can however change this to use other 
payment gateways supported by django-payments. 

> [!CAUTION]  
> Don't make payment to your self in production, as this goes against Stripe terms of use. Use only stripe test account for testing purposes.

You can get the stripe test account secret key, public key and webhook key from stripe dashboard.

* To forward webhook request to local development follow the stripe guide: https://docs.stripe.com/webhooks#local-listener

## Deployment:

You can make use of Railway to deploy your own instance. 

<a href="https://railway.app?referralCode=BfMDHP">
  <img src="railway.png" alt="railway icon" height="50px"/>
</a>

Link to deploy to [Railway.app](https://railway.app?referralCode=BfMDHP)

once you complete make sure to 
```
python manage.py collectstatic
```
and set
```
DEBUG=0
```
**Generate secret key**
To generate secret key use `from django.core.management.utils import get_random_secret_key` then `get_random_secret_key()` in your python shell

**Note:** Don't forget to set the sites to your domain instead of example.com in the admin panel

> [!NOTE]  
> Make sure to add webhook endpoint during production via stripe, other wise you may not get the confirmations

#### Create a firebase credential file

> [!NOTE] 
We'll be using firebase for persistent storage, to upload user files. Firebase is pre-configured as there are other firebase services developers may want to use. <br><br> You can also use any of the storage supported by [django-storages](https://github.com/jschneier/django-storages), if you don't want to use firebase.

To use Firebase

1. We use Google storage for storing files. Go to firebase -> storage -> create (make it public)

2. Now Go to firebase -> project settings -> service account -> Generate new private key.

Rename the private as `firebase-cred.json`

Use this private file as your credential file.

#### Deploying credential file to production
Sometimes your cloud provider may not provide you with storage for secret files. 
So convert the credential file to base64 using
```
base64 firebase-cred.json > encoded.txt
```
Now copy the contents of encoded.txt and paste it in `FIREBASE_ENCODED="wedde"` variable

## 🔥 Contributing

Want to help improve **Sports Connect**? Follow these steps:

1. **Fork** the repository.
2. **Create a new branch** (`feature-name`).
3. **Commit your changes** with clear messages.
4. **Push to GitHub** and submit a **Pull Request**.

Please review our [Contributing Guidelines](CONTRIBUTING.md) before submitting.

---

## 📜 License

This project is licensed under the **GNU Affero General Public License (AGPL-3.0)**.  
See the [LICENSE](LICENSE) file for full details.

---

## 📬 Contact

For questions or collaboration, reach out to us at:  
📧 **[email-here]**  
🌐 **[Sports Connect Website](your-website-here)**  

---

## 👥 Team - Game Changers

- **Matthew** – Product Owner, Database Developer  
- **Alessandro** – Frontend Developer  
- **Grayson** – Backend Developer  
- **Zach** – Scrum Master, QA Engineer / Documentation Specialist  
