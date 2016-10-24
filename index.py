from flask import Flask, url_for, render_template
app=Flask(__name__)

@app.template_global(name='zip')
def _zip(*args, **kwargs):
  return __builtins__.zip(*args, **kwargs)

@app.route("/")
def cover():
  return render_template('cover.html'), 200

@app.route("/City")
def city():
  topic='City'
  pictures=['street','arts1',
  'arts2','townHall','bullring','skyline','townHall2','velesEvents']
  descriptions=['First description','Second description','Third description','qwe','qweqwe']
  return render_template('gallery.html',topic=topic,pictures_descriptions=zip(pictures,descriptions)), 200

@app.route("/Nature")
def nature():
  topic='Nature'
  pictures=['albufera','malvarrosaBeach','coast']
  descriptions=['Albufera','Malvarrosa','Random Coast']  
  return render_template('gallery.html',topic=topic,pictures_descriptions=zip(pictures,descriptions)), 200


@app.route("/Leisure")
def leisure():
  topic='Leisure'
  pictures=['fallas']
  descriptions=['Fallas']  
  return render_template('gallery.html',topic=topic,pictures_descriptions=zip(pictures,descriptions)), 200

@app.route("/Sports")
def sports():
  topic='Sports'
  pictures=['fonteta','surf','llevant','athleticsTrack',
  'mestalla','paddleSurf','skatePark','volleyCourt','courts']
  descriptions=['"La Fontenta" basket stadium','Surf on Malvarrosa Beach',
  'Levante UD stadium','Athletics Track','Valencia CF stadium',
  'Paddle surf on Valencia`s port','Skate park','Volleyball courts','Sports courts']  
  return render_template('gallery.html',topic=topic,pictures_descriptions=zip(pictures,descriptions)), 200

@app.route("/<catalogue>/<picture>")
def picture(catalogue=None,picture=None):
  cat = {'catalogue':catalogue}
  pict = {'picture':picture}
  return render_template('picture.html',cat=cat,pict=pict)

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
