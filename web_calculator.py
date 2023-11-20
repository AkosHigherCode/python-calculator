from flask import Flask, request, render_template_string

app = Flask(__name__)

# Enhanced HTML template with CSS
html_template = '''
<!doctype html>
<html>
<head>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #333;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: inline-block;
            margin-top: 20px;
        }
        input[type=text] {
            width: 300px;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        input[type=submit] {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type=submit]:hover {
            background-color: #0056b3;
        }
        p {
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Python Calculator</h1>
    <h4>created by Akos Vagvolgyi</h4>
    <form method="POST">
        <input type="text" name="expression" placeholder="Enter expression" />
        <input type="submit" value="Calculate">
    </form>
    <p>Result: {{ result }}</p>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ""
    if request.method == 'POST':
        expression = request.form['expression']
        try:
            result = eval(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(debug=True)
