from flask import Flask
from main import Main
from output_managers.json import JSONOutputManager
from time import time


app = Flask(__name__)


def logged_handler(func):
    def resulting_func():
        start = time()
        print(f"Start {func.__name__}")
        result = func()
        finish = time()
        print(f"Finish {func.__name__} in {finish - start}")
        return result
    return resulting_func


@app.route("/")
@logged_handler
def handler():
    output_manager = JSONOutputManager()
    Main(output_manager).run()
    return {"result": output_manager.buffer}
