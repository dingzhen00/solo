## The completed web project can be viewed through the following link
Access via this link：https://products-app6.onrender.com/
## Main templates of the website:
- index.html
  - The home page of the website, which provides access to various pages including product listings, login, registration and administration login pages
- products_list.html
  - The corresponding button name is __Go to all products page__.The product list home page is the home page where you can display all your products, add a shopping cart and search function. 
- register.html
  - The corresponding button name is __Registration__.Go to the user registration screen and register as a user, after registration you can perform the billing function, ordinary visitors cannot be billed
- sign_in.html
  - The login page, with the corresponding button __Log in__, allows you to log in as a user and check out your orders once you have done so.
- admin_login.html
  - The corresponding button name is __Administrator Login__.Go to the admin login page, only admins can login
- admin_in.html
  - The page after the administrator enters, showing the number of orders, order information and a chart of the total order quantity
- Cart.html
  -  This page is for adding a shopping cart function to the rightmost button on the product_list.
- detail.html
  - This is the page where the product details are displayed, accessed by clicking on the item name in the product_list page.
- search_results.html
  - This is the search function, which can be accessed from the top right hand corner of the product_list page via the search function.
## Models in the application:
- eletronics(models.Model):
- User(models.Model):
  - Product table to display all the products on the website.
- Part(models.Model):
  - Tables associated with order creation
- Order(models.Model):
  - The order form, where orders created by users are stored
- eletronicsdetail(models.Model):
  - This is the second chapter of the product information sheet, which is used to show product details.
## Environmental settings:
- __Basic environment setup__
__Note: All settings below are based on the codio platform__
~~~
pyenv update
pyenv install 3.10.7
pyenv local 3.10.7
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install django
pip insrall behave
pip install selenium
pip install behave django-behave
pip install whitenoise
~~~
- __Headless chrome browser installation (required for Behave testing)__
__Note: That after installing the headless browser you will need to set the path for debugging depending on the location of your project.__
~~~
sudo apt-get update
sudo apt-get install -y wget unzip
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
rm google-chrome-stable_current_amd64.deb
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/local/bin/
rm chromedriver_linux64.zip
~~~
## Basic instructions:
- Activating the virtual environment
~~~
source .venv/bin/activate
~~~
- Database commands, used after modifying models.py and updating the database
~~~
python3 manage.py migrate
python3 manage.py makemigrations shop
~~~
- Run server commands
~~~
python3 manage.py runserver 0.0.0.0:8000
~~~
- Behave Test
Activate the virtual environment first
~~~
source .venv/bin/activate
~~~
Then type behave in the terminal to test
~~~
behave
~~~