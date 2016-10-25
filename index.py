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
  pictures=['arts1','street','townHall','bullring','skyline','velesEvents']
  descriptions=['First description','Second description','Third description',
  'qwe','qweqwe','Veles e Vents']
  return render_template('gallery.html',topic=topic,pictures_descriptions=zip(pictures,descriptions)), 200

@app.route("/Nature")
def nature():
  topic='Nature'
  pictures=['albufera','malvarrosaBeach','coast','montanejos','serella','covaTallada']
  descriptions=['Albufera','Malvarrosa','Altea','Montanejos','Serella','Cova tallada']  
  return render_template('gallery.html',topic=topic,pictures_descriptions=zip(pictures,descriptions)), 200


@app.route("/Leisure")
def leisure():
  topic='Leisure'
  pictures=['fallas','gulliver','marinaBeach','umbracle','olympia','heronCity']
  descriptions=['Fallas','Gulliver','Marina Beach','Umbracle Disco',
  'Olumpia Theatre','Heron City']  
  return render_template('gallery.html',topic=topic,pictures_descriptions=zip(pictures,descriptions)), 200

@app.route("/Sports")
def sports():
  topic='Sports'
  pictures=['fonteta','surf','athleticsTrack',
  'mestalla','skatePark','volleyCourt']
  descriptions=['"La Fontenta" basket stadium','Surf on Malvarrosa Beach',
  'Athletics Track','Valencia CF stadium', 'Skate park','Volleyball courts']  
  return render_template('gallery.html',topic=topic,pictures_descriptions=zip(pictures,descriptions)), 200

@app.route("/<catalogue>/<picture>")
def picture(catalogue=None,picture=None):
  cat = {'catalogue':catalogue}
  pict = {'picture':picture}
  if catalogue == "City":
    if picture == "street":
      description = 'Valencia`s street'
    elif picture == "arts1":
      description = 'Arts'
    elif picture == "townHall":
      description = 'Arts2'
    elif picture == "bullring":
      description = 'Bullring'
    elif picture == "skyline":
      description = 'Skyline'
    elif picture == "velesEvents":
      description = 'Veles e Vents'
  elif catalogue == "Nature":
    if picture == "albufera":
      description = 'Albuferaa'
    elif picture == "malvarrosaBeach":
      description = 'Malvarrosa Beach'
    elif picture == "coast":
      description = 'Altea`s coast'
    elif picture == "montanejos":
      description = 'Montanejos lake'
    elif picture == "serella":
      description = 'Serella`s mountain'
    elif picture == "covaTallada":
      description = 'Cova Tallada'
  elif catalogue=="Leisure":
    if picture=="fallas":
      description = 'These are las fallas'
    elif picture == "gulliver":
      description = 'Gulliver'
    elif picture == "marinaBeach":
      description = 'Marina Beach'
    elif picture == "umbracle":
      description = 'Umbracle'
    elif picture == "olympia":
      description = 'Olympia'
    elif picture == "heronCity":
      description = 'Heron City'
  elif catalogue=="Sports":
    if picture=="fonteta":
      description = 'This is Valencia Basket`s stadium'
    elif picture == "surf":
      description = 'Surf'
    elif picture == "athleticsTrack":
      description = 'Athletics Track'
    elif picture == "skatePark":
      description = 'Skate Park'
    elif picture == "mestalla":
      description = 'Mestalla'
    elif picture == "volleyCourt":
      description = 'VolleyBall court'

  return render_template('picture.html',cat=cat,pict=pict,description=description), 200
  

@app.errorhandler(404)
def page_not_found(error):
  return "Couldn't find the page you requested.", 404

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
