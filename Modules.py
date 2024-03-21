import_modules='''
import os # Os Module must be imported first to install any package if not installed in between
import time
#import mysql.connector as sqlcon
import pymysql as sqlcon
import pickle
import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, K_SPACE, K_UP
import csv
import webbrowser
import PySimpleGUI as sg
import subprocess
import randfacts
import pywhatkit
from num2words import num2words
import random
import wikipedia
import webbrowser
import pyjokes
import smtplib
import ctypes
import requests
from ecapture import ecapture as ec
import sys
'''

try:
    exec(import_modules)
except:
    print('Installing Required Packages')
    os.system('pip install matplotlib PySimpleGUI mysql-connector pyttsx3 pyaudio SpeechRecognition \
    wikipedia pyjokes requests ecapture PyWhatKit randfacts num2words pymysql')
    os.system('pip3 install matplotlib PySimpleGUI mysql-connector pyttsx3 pyaudio SpeechRecognition \
    wikipedia pyjokes requests ecapture PyWhatKit randfacts num2words pymysql')
    os.system('pip install pygame --pre');os.system('pip3 install pygame --pre')

    try:
        exec(import_modules)
    except:
        raise Exception('Unable to Install and import some particular Modules')
