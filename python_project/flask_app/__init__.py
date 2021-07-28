from flask import Flask

app=Flask(__name__)
app.secret_key = "we keep secrets to keep this safe"