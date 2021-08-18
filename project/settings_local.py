SECRET_KEY = 'django-insecure-+1tfiub0^^bw&g^lq1*#c(2+jozw8t&h#+)@%o=tp5$fsp%ym0'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'project',
        'USER': 'postgres',
        'PASSWORD': '0000',
        'HOST': 'postgres',
        'PORT': '5432'
    }
}
