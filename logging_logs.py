import logging
#from logging import * #To avoid writing logging always

#log process id and change log output format (process)
#to track msgs we add line numbers(lineno)
#to add date and time (asctime)
logging.basicConfig(filename='app.log',
            level=logging.DEBUG,
            filemode='w',
            format="%(asctime)s/%(lineno)s:%(name)s:%(levelname)s:%(message)s:%(process)s",
            datefmt='%d-%b-%y %H:%M%S', #Changing date format
            )

logging.debug("This is a debug msg") #10
logging.info("Message for information") #20
logging.warning("Warning process initiation message")  #30
logging.error("There is an error msg") #40
logging.critical("Critical error present in the program") #50

# By default the logging level is set to 30 ie warning

# we can also change the style for logging by adding style="{" in
# the basicConfig()
#After that no need to add %()s