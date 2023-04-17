from flask import Flask, render_template
from controllers.team_controller import team_blueprint

app = Flask(__name__)
app.register_blueprint(team_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)