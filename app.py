from flask import Flask, render_template, request

from markupsafe import Markup

app = Flask(__name__, template_folder='template')


@app.route("/", methods=['GET'])
def content():
    print(request)
    file = request.args.get('file')
    filename = file + '.txt'
    try:
        with open(filename, 'rb') as file:
            content = file.read()
    except FileNotFoundError:
        return render_template('content.html', text=Markup("<h2> File Not Found. </h2>"))
    try:
        print("filename: ", filename)
        content.decode("utf-8")
        val = utf8_file(filename)
        return render_template('content.html', text=Markup(val))
    except:
        print("in except")
        utf_content = content.decode("utf-16")
        return render_template("content.html", text=Markup(utf_content))


def utf8_file(file):
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
                return render_template('content.html', text=Markup('<h2>start number is greater</h2>'))
            elif int(end) < 0:
                return render_template('content.html', text=Markup('<h2>end number is smaller</h2>'))
            if not start or not end:
                commands[number[:-1]] = description.strip()
                list.append(description.strip())
            if int(start) <= int(number[:-1]) <= int(end):
                commands[number[:-1]] = description.strip()
                list.append(description.strip())

    fh.close()
    return ' \n'.join(map(str, list))


if __name__ == '__main__':
    app.run(debug=True)
