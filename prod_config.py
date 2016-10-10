# Statement for enabling the development environment
DEBUG = True

# Define the application directory
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))  

# Define the database - we are working with
# SQLite for this example
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_DATABASE_URI='postgresql://root:root@localhost/test'
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
DATABASE_CONNECT_OPTIONS = {}

# MongoDB connection details
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'ucc'
# MONGO_AUTO_START_REQUEST=True
# MONGO_REPLICA_SET='replica'
# MONGO_READ_PREFERENCE='primary'
# MONGO_USERNAME='ucc'
# MONGO_PASSWORD='changelater'

# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
#CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
# signing the data. 
#CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
#SECRET_KEY = "secret"
