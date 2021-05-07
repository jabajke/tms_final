from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about,name="about")
]


# echo "# myfirst_project" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/jabajke/myfirst_project.git
# git push -u origin main
# .idea /
# db.sqlite3
# main /
# manage.py
# webfirst /
