from flask import (Blueprint, render_template)
from app.logIn import *

Main = Blueprint(
            'Main',
            __name__,
            template_folder="templates",
        )


@Main.route('/main')
def main():
    return render_template("main/main.html")
