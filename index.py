from flask import Flask, url_for, render_template
app=Flask(__name__)

@app.route("/")
def cover():
  return render_template('cover.html'), 200

@app.route("/index")
def index():
  pictures=['albufera','fallas','street','arts1',
  'arts2','malvarrosaBeach','townHall','bullring','skyline','townHall2','coast','velesEvents']
  return render_template('index.html',pictures=pictures), 200

@app.route("/city")
def city():
  return render_template('city.html'), 200

@app.route("/coast")
def coast():
  return render_template('coast.html'), 200

@app.route("/leisure")
def leisure():
  return render_template('leisure.html'), 200

@app.route("/sports")
def sports():
  return render_template('sports.html'), 200

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
