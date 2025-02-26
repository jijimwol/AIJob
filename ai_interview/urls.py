from django.urls import path
from .views import (
    home, register_view, login_view, logout_view, index, summary_view,analyze_personality,clear_history
)

urlpatterns = [
    path("", home, name="home"),  # Home Page
    path("register/", register_view, name="register"),  # Register Page
    path("login/", login_view, name="login"),  # Login Page
    path("logout/", logout_view, name="logout"),  # Logout Action
    path("dashboard/", index, name="index"),  # Main Dashboard (Interview Practice)
    path("summary/", summary_view, name="summary"),
    path("personality/", analyze_personality, name="personality"),
    path("clear-history/", clear_history, name="clear_history"),

  # User's Interview Summary
]
