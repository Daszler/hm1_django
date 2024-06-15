from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)


def starting_page(request):
    logger.info('Index page accessed')
    start_page = """
    <html>
    <body>
    <h1>Это стартовая страница!</h1>
    </body>
    </html>"""
    return HttpResponse(start_page)


def about_me(request):
    logger.info('About page accessed')
    about_me = """
    <html>
    <body>
    <h1>Меня зовут Михаил, мне 26 лет и я работаю в клиентской поддержке
    Яндекса. Очень стремлюсь стать разработчиком на Django</h1>
    </body>
    </html>"""
    return HttpResponse(about_me)