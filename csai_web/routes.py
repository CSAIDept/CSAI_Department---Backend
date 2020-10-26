import json
from flask import request, jsonify, render_template
from csai_web import app, limiter
import pandas as pd
from csai_web.middleware import login_required


@app.route("/yo")
def catch():
    return render_template('home.html')