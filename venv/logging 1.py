import logging
#create and configure logger
logging.basicConfig(filename = "D:/Python/lumberjack.Log",
                    level = logging.DEBUG)
logger = logging.getLogger()

#test the logger
logger.info("our first message.")

print(logger.level)
