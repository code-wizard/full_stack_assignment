Step to run the project locally
=> install all dependencies using pip install -r requirements.txt

=> run ./manage.py migrate to populate the database

=> If you hit CORS errors, add your frontend app host address
CORS_ORIGIN_WHITELIST = ['localhost:4207']
or  set CORS_ORIGIN_ALLOW_ALL = TRUE
