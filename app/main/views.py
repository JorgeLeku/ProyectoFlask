from flask import (Blueprint, render_template)

Main = Blueprint(
            'Main',
            __name__,
            template_folder="app/templates",
        )


@Main.route('/main')
def main():
    return render_template("main.html")
