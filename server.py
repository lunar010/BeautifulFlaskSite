import re
from flask import Flask, redirect, request, render_template, session, send_from_directory
from flask_session import Session

app=Flask(__name__)

@app.route('/<site>')
def sites(site):
    if site == "home":
        return render_template('home.html')
    elif site == "index":
        return render_template('home.html')
    elif site == "discord":
        return redirect('https://discord.gg/Fn2xBdaWHA')
    elif site == "kakao":
        return redirect('https://open.kakao.com/o/sfRq9IRd')
    else:
        return render_template('home.html')

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug = True)

