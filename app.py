from flask import Flask, render_template, templating
from SRC.Logger import log


app = Flask(__name__)

# Main website
@app.route('/')
def Home():
    return render_template('Home.html')


# API Module
@app.route('/API/<ProgramID>/')
def background_process_test(ProgramID):
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
    
    return ("Running Program ID:  " + str(ProgramID))


if __name__ == '__main__':
    Dev = True
    app.run(host='0.0.0.0', port=5000, debug=Dev)