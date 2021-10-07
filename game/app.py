from flask import Flask
from main import Main
from outputs.json import JSONOutput


app = Flask(__name__)


@app.route("/")
def get_fighting():
    output = JSONOutput()
    main = Main(output)
    main.run()
    return {"result": output.output_buffer}, 200
