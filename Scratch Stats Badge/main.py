from requests import get
from flask import Flask, request, Response
from flask_cors import CORS
from API import get_user_data, get_studio_data, get_project_data

app = Flask('Scratch Stats Badge')
CORS(app)


@app.route("/")
def root():
    data = {"Name": "Scratch Stats Badge",
            "Version": "1.0",
            "Description": "Scratch Stats Badge maker, which can be used to add dynamic badges to Github readmes, etc.",
            "Docs": "https://github.com/Sid72020123/Scratch-Stats-Badge#readme",
            "Developer": "Sid72020123 on Scratch"
            }
    return data


@app.route("/user")
def user():
    arguments = request.args
    username = arguments.get("username", default="", type=str)
    if username == "":
        response = Response(get(
            f"https://img.shields.io/static/v1?label=Error&message=Username not given!&color=red&style=flat&labelColor=white").content)
        response.headers['Content-Type'] = 'image/svg+xml'
        return response
    type = arguments.get("data", default="username", type=str)
    label = arguments.get(
        "label", default=f"{username}'s {type} data:", type=str)
    color = arguments.get("color", default="green", type=str)
    label_color = arguments.get("label_color", default="gray", type=str)
    style = arguments.get("style", default="flat", type=str)
    data = get_user_data(username, type)
    if data is False:
        response = Response(get(
            f"https://img.shields.io/static/v1?label=Error&message=An error occurred! Check if the user exists...&color=red&style=flat&labelColor=white").content)
        response.headers['Content-Type'] = 'image/svg+xml'
        return response
    response = Response(get(
        f"https://img.shields.io/static/v1?label={label}&message={data}&color={color}&style={style}&labelColor={label_color}").content)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response


@app.route("/studio")
def studio():
    arguments = request.args
    studio = arguments.get("id", default="", type=str)
    if studio == "":
        response = Response(get(
            f"https://img.shields.io/static/v1?label=Error&message=Studio ID not given!&color=red&style=flat&labelColor=white").content)
        response.headers['Content-Type'] = 'image/svg+xml'
        return response
    type = arguments.get("data", default="title", type=str)
    label = arguments.get(
        "label", default=f"Studio {studio}'s {type} data:", type=str)
    color = arguments.get("color", default="green", type=str)
    label_color = arguments.get("label_color", default="gray", type=str)
    style = arguments.get("style", default="flat", type=str)
    data = get_studio_data(studio, type)
    if data is False:
        response = Response(get(
            f"https://img.shields.io/static/v1?label=Error&message=An error occurred! Check if the studio exists...&color=red&style=flat&labelColor=white").content)
        response.headers['Content-Type'] = 'image/svg+xml'
        return response
    response = Response(get(
        f"https://img.shields.io/static/v1?label={label}&message={data}&color={color}&style={style}&labelColor={label_color}").content)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response


@app.route("/project")
def project():
    arguments = request.args
    project = arguments.get("id", default="", type=str)
    if project == "":
        response = Response(get(
            f"https://img.shields.io/static/v1?label=Error&message=Project ID not given!&color=red&style=flat&labelColor=white").content)
        response.headers['Content-Type'] = 'image'
        return response
    type = arguments.get("data", default="title", type=str)
    label = arguments.get(
        "label", default=f"Project {project}'s {type} data:", type=str)
    color = arguments.get("color", default="green", type=str)
    label_color = arguments.get("label_color", default="gray", type=str)
    style = arguments.get("style", default="flat", type=str)
    data = get_project_data(project, type)
    if data is False:
        response = Response(get(
            f"https://img.shields.io/static/v1?label=Error&message=An error occurred! Check if the project exists...&color=red&style=flat&labelColor=white").content)
        response.headers['Content-Type'] = 'image/svg+xml'
        return response
    response = Response(get(
        f"https://img.shields.io/static/v1?label={label}&message={data}&color={color}&style={style}&labelColor={label_color}").content)
    response.headers['Content-Type'] = 'image/svg+xml'
    return response


app.run(host='0.0.0.0', port=8080, debug=True)
