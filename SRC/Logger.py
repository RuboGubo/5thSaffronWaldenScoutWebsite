import logging

logging.basicConfig(filename='SRC/System.log', level=logging.DEBUG,
                format='%(levelname)s:%(name)s:%(message)s')

class log():
    def info(message):
        logging.info(message)
        print('Info: ' + str(message))
        
    def critical(message):
        level = 'Crititcal '
        bordertop = '\n' + level + ('=' * (len(message)-len(level)))
        borderbottom = '\n' + ('=' * len(message))
        message = bordertop + '\n' + message + borderbottom
        
        logging.critical(message)
        print(message)
        
    def warning(message):
        logging.warning(message)
        print('Warning: ' + str(message))
        
    def debug(message):
        logging.debug(message)
        print('Debug: ' + str(message))
        
    def error(message):
        logging.error(message)
        print('Error: ' + str(message))
    


