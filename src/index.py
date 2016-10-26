from flask import Flask, url_for, render_template, request
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
  descriptions=['Arts and Science City','Street','Town Hall',
  'Bullring','Skyline','Veles e Vents']
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
      description = 'This is a Valencia`s street located in Campanar neighbourhood'
    elif picture == "arts1":
      description = 'The famous "Ciudad de las artes y las ciencias"'
    elif picture == "townHall":
      description = 'This is the town hall, located in the citycentre'
    elif picture == "bullring":
      description = 'An old bullring'
    elif picture == "skyline":
      description = 'Nice views of Valencia skyline'
    elif picture == "velesEvents":
      description = 'Veles e Vents is a building in the port'
    else:
      return page_not_found(404)
  elif catalogue == "Nature":
    if picture == "albufera":
      description = "L'albugfera is the most famous lake in Valencia"
    elif picture == "malvarrosaBeach":
      description = 'Malvarrosa Beach is inside Valencia city'
    elif picture == "coast":
      description = 'Altea`s coast'
    elif picture == "montanejos":
      description = 'Montanejos lake'
    elif picture == "serella":
      description = 'Serella`s mountain'
    elif picture == "covaTallada":
      description = 'Cova Tallada'
    else:
      return page_not_found(404)
  elif catalogue=="Leisure":
    if picture=="fallas":
      description = 'A monument of Valencia`s fest'
    elif picture == "gulliver":
      description = 'Gulliver is a place to enjoy with your kids'
    elif picture == "marinaBeach":
      description = 'Marina Beach is a evening disco'
    elif picture == "umbracle":
      description = 'Umbracle is a night disco'
    elif picture == "olympia":
      description = 'Olympia theatre is the most famous theatre in Valencia'
    elif picture == "heronCity":
      description = 'Heron City has cinemas, bowling and lots of leisure places'
    else:
      return page_not_found(404)
  elif catalogue=="Sports":
    if picture=="fonteta":
      description = 'This is Valencia Basket`s stadium'
    elif picture == "surf":
      description = 'Surf is very usual on Malvarrosa Beach'
    elif picture == "athleticsTrack":
      description = 'Athletics Track where you can go for free'
    elif picture == "skatePark":
      description = 'The new Skate Park'
    elif picture == "mestalla":
      description = 'Mestalla is the Valencia CF stadium'
    elif picture == "volleyCourt":
      description = 'VolleyBall court'
    else:
      return page_not_found(404)
  else:
    return page_not_found(404)

  return render_template('picture.html',cat=cat,pict=pict,description=description), 200

@app.route("/redirect", methods=['POST','GET'])
def redirection():
   dest = request.form['dest']
   if dest == "Sports":
     return sports()
   elif dest == "City":
     return city()
   elif dest == "Nature":
     return nature()
   elif dest == "Leisure":
     return leisure()
   elif dest == "/":
     return cover()

@app.errorhandler(404)
def page_not_found(error):

  form = '''
  <html>
  <head>
    <link href="../static/css/bootstrap.min.css" rel="stylesheet"/>
    <link href="../static/css/style.css" rel="stylesheet"/>
  <body>
    <div id="container">
    <h1> ERROR, the requested URL is not valid</h1>
      <div class="mainImgContainer">
        <h3> Let us take you back </h3>
        <h4> Where do you want to go? </h4>
        <br/><br/><br/>
        <form action="/redirect" method="post" name="form">
          <input type="radio" name="dest" value="/"> <b>Home</b>
          <input type="radio" name="dest" value="City"> <b>City</b>
          <input type="radio" name="dest" value="Nature"> <b>Nature</b>
          <input type="radio" name="dest" value="Leisure"> <b>Leisure</b>
          <input type="radio" name="dest" value="Sports"> <b>Sports</b>
          <br/><br/>
          <input type="submit" value="Go!" class="btnGo btn btn-primary btn-lg">
        </form>
      </div>
    </div>
  <html><body>
  '''
  return form

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
