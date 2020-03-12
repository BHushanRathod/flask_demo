from flask import Flask, render_template, request
import re

app = Flask(__name__, template_folder='template')

@app.route("/", methods=['GET'])
def content():
    print(request)
    with open('file1.txt', 'rb') as file:
        content = file.read()
    print(type(content))
    try:
        utf_content = content.decode("utf-8")
    except:
        utf_content = content.decode("utf-16")

    temp = re.findall("([0-9]):([a-zA-Z]+)", utf_content)
    print(temp)

    # print("utf_content: ", utf_content)

    file.close()
    return render_template('content.html', text=utf_content)


if __name__ == '__main__':
    app.run(debug=True)
