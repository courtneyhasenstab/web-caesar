from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
           <style>
            body {{
                background-color: #2f;
            }}
            .wrapper {{
                top: 45%;
                left: 50%;
                width: 600px;
                height: 600px;
                display: block;
                margin: 0 auto;
                position: fixed;
                box-shadow: 0px 2px 25px #eee;
                transform: translate(-50%, -50%)
            }}
            .inner-wrapper {{
                width: 475px;
                display: block;
                margin: 0 auto;
                padding-top: 50px;
            }}
            form {{
                width: 100%;
                display: block;
                margin: 0 auto;
                font-size: 16px;
                border-radius: 10px;
                font-family: "Comic Sans MS", "Comic Sans";
            }}
            textarea {{
                width: 100%;
                height: 150px;
                margin: 8px 0;
                font-size: 14px;
                border-radius: 4px;
                padding: 12px 20px;
                border: 1px solid #ccc;
                box-sizing: border-box;
            }}
            h1 {{
                color: #2A3132;
                font-weight: 100;
                text-align: left;
                font-family: "Comic Sans MS", "Comic Sans";
            }}
            p {{
                color: #000;
                display: block;
                margin: 0 auto;
                font-size: 16px;
                text-align: left;
                font-weight: 200;
                padding-bottom: 20px;
                font-family: "Comic Sans MS", "Comic Sans";
            }}
            hr {{
                border: 0;
                padding: 0 0 15px 0;
                width: 100%;
                height: 1px;
                opacity: 0.5;
                display: block;
                margin: 0 auto;
                border-top: 1px solid #aeaeae;
            }}
            label {{
                color: #aeaeae;
                font-size: 14px;
                font-weight: 300;
            }}
            input[type=text], select {{
                width: 100%;
                margin: 8px 0;
                padding: 12px 20px;
                border-radius: 4px;
                display: inline-block;
                border: 1px solid #ccc;
                box-sizing: border-box;
            }}
            input[type=submit] {{
                width: 100%;
                color: white;
                border: none;
                margin: 8px 0;
                cursor: pointer;
                padding: 14px 20px;
                border-radius: 4px;
                background-color: #F5FFA;
            }}
            input[type=submit]:hover {{
                background-color: #aeaeae;
                transition: 0.25s ease-in-out;
                -o-transition: 0.25s ease-in-out;
                -ms-transition: 0.25s ease-in-out;
                -moz-transition: 0.25s ease-in-out;
                -webkit-transition: 0.25s ease-in-out;
            }}
            .footer {{
                left: 0;
                bottom: 0;
                width: 100%;
                height: 50px;
                position: absolute;
            }}
            .footer p {{
                color: #aeaeae;
                text-align: center;
                padding: 35px 0 0 0;
            }}
        </style>
    </head>
    <body>
        <div class="wrapper">
            <div class="inner-wrapper">
                <h1>Caesar Cipher</h1>
                <p>A web caesar cipher application! Type in a message and the amount you want of rotation to see your message encrypted!</p>
                <hr>
                <form class="cipher-form" action ="/" method="POST">
                    <textarea name="text" placeholder="Enter Message to Encrypt:">{0}</textarea>
                    <label for "rot">Enter Amount to Rotate:</label>
                    <input type="text" id="rot" name="rot" value="0">
                    <input type="submit" value="Encrypt">
                </form>
            </div>
        </div>
        <div class="footer">
            <p class="footer">Created using Python, Flask, &amp; designed by Bill Phan</p>
        </div>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")

@app.route("/", methods=['POST'])
def encrypt():
    rot = int(request.form['rot'])
    rot_text = str(request.form['text'])
    encrypt_text = rotate_string(rot_text, rot)
    return form.format(encrypt_text)

app.run()