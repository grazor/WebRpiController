#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Error handling """

from flask import render_template
from wrc import app


@app.errorhandler(400)
def not_found(error):
    return render_template('errors.html', errno="400. Bad Request")


@app.errorhandler(403)
def not_found(error):
    return render_template('errors.html', errno="403. Forbidden")


@app.errorhandler(404)
def not_found(error):
    return render_template('errors.html', errno="404. Not Found")


@app.errorhandler(405)
def not_found(error):
    return render_template('errors.html', errno="404. Method not allowed")


@app.errorhandler(500)
def not_found(error):
    return render_template('errors.html', errno="500. Internal Server Error")