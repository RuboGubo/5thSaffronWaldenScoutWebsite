from flask import Flask, render_template, templating
from SRC.Logger import log


app = Flask(__name__)

# Main website
@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/Pages/Home/')
def ContentHome():
    return render_template('Home.html')

@app.route('/test')
def test():
    return 'Welcome to the test server, here you can see the scout website as it is developed by \'RuboGubo\''

@app.route('/Pages/Explorers/VideosFromCamp')
def ExplorersVideosFromCamp():
    return "<style>html{width: 100%; font-family: 'Courier New', Courier, monospace;}</style>" + 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'*100

# API Module
@app.route('/API/<ProgramID>/')
def API(ProgramID):
    log.debug ("ProgramID=" + ProgramID)
    
    ProgramID = int(ProgramID)
    
    if ProgramID == 0:
        log.debug('No Module')
    elif ProgramID == 1:
        log.debug('No Module')
    elif ProgramID == 2:
        log.debug('No Module')
    elif ProgramID == 3:
        log.debug('No Module')
    else:
        log.debug('error')
    
    return ("<style>html{width: 100%; font-family: 'Courier New', Courier, monospace;}</style>Running Program ID:  " + str(ProgramID))


if __name__ == '__main__':
    Dev = False
    app.run(host='192.168.0.19', port=8090, debug=Dev)