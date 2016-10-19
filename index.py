from flask import Flask, url_for, render_template
app=Flask(__name__)

@app.route("/")
def index():
  pictures=['albufera','fallas','street','arts1',
  'arts2','malvarrosaBeach','townHall','bullring','skyline','townHall2','coast','velesEvents']
  return render_template('index.html',pictures=pictures), 200

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
