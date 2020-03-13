import json

from flask import Flask, render_template, request
import re

app = Flask(__name__, template_folder='template')


@app.route("/", methods=['GET'])
def content():
    print(request)
    file = request.args.get('file')
    filename = file + '.txt'
    with open(filename, 'rb') as file:
        content = file.read()
    try:
        print("filename: ", filename)
        content.decode("utf-8")
        print("1")
        val = utf8_file(filename)
        print("2")
        return render_template('content.html', text=val)
    except:
        print("in except")
        utf_content = content.decode("utf-16")
        return render_template("content.html", text=utf_content)


def utf8_file(file):
    print("in metthod: ", file)
    commands = {}
    list = []
    start = request.args.get("start")
    end = request.args.get("end")
    with open(file) as fh:
        for line in fh:
            number, description = line.strip().split(' ', 1)
            commands[number[:-1]] = description.strip()
            max_len = len(commands)
            if int(start) > int(max_len):
                return render_template('content.html', text='start number is greater')
            elif int(end) < 0:
                return render_template('content.html', text='end number is smaller')
            if not start or not end:
                commands[number[:-1]] = description.strip()
                list.append(description.strip())
            if int(start) <= int(number[:-1]) <= int(end):
                print("in if: ", start, number[:-1], end)
                commands[number[:-1]] = description.strip()
                list.append(description.strip())

    fh.close()
    return ' \n'.join(map(str, list))


if __name__ == '__main__':
    app.run(debug=True)
