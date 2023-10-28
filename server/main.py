from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__, "/public/static")

@app.route("/")
def home():
    html = """
    <!doctype html>
    <html>
    <head>
        <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
    </head>
    <body>
        Pyodide test page <br>
        Open your browser console to see Pyodide output
        <script type="text/javascript">
        async function main(){
            const res = await window.fetch("public/sample.py");
            const pycode = await res.text();

            let pyodide = await loadPyodide();
            await pyodide.loadPackage("opencv-python");
            console.log("Pyodide is ready.");
            await pyodide.runPython(pycode);
        }
        main();
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

# 静的ファイルの配信
@app.route("/public/<path:path>")
def send_public(path):
    return send_from_directory("public/static", path)
