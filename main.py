from backend.auth import login
from backend.menu import menu_utama

if login():
    menu_utama()
