import os
from flask import render_template
import psutil

def getcpu():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage

def getram():
    ram_usage = psutil.virtual_memory()[2]
    ram_usagegb = psutil.virtual_memory()[3]/1000000000
    return ram_usage, ram_usagegb

def index():
    cpu_use = getcpu()
    ram_use,ram_usegb = getram()
    return render_template("index.html", cpu_usage=cpu_use, ram_usage=ram_use, ram_usagegb=ram_usegb)

