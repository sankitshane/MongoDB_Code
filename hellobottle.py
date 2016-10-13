import bottle

@bottle.route('/')
def home_page():
    return "Hello World!\n"

@bottle.route('/testpage')
def test_page():
    return "This is a test Page"

bottle.debug(True)
bottle.run(host = 'localhost',port = 8080)
