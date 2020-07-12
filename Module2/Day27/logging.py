# The logging module offers the ability to
# track the progress of the application and report on successes and failures.

# The module contains the standard levels of DEBUG, INFO, WARNING, ERROR, and CRITICAL',
# but custom levels can be created. The logger first needs to be
# created using the.basicConfig()function and the log file is passed as a parameter

import logging

# os.chdir(".\\Module2\\Day27")

logging.basicConfig(filename="module2_day27_logging.log")
logger = logging.getLogger()
logger.info("This is a custom info message.")
logger.warning("This is a custom warning message.")

print(logger.level)
log_level = [("NOTSET", 0), ("DEBUG", 10), ("INFO", 20), ("WARNING", 30), ("ERROR", 40), ("CRITICAL", 50)]

logger.level = "DEBUG"
logger.info("This is a custom info message.")
logger.warning("This is a custom warning message.")

# above
# While the file was created, the .info() message was not recorded.
# The .level method. This will provide the numerical representation of the level created in the .basicConfig() function.
# A logger level of 30 represents the level "WARNING".
# The logger will only print messages that have a level greater than or equal to the level set when creating the logger.
# Therefore, since an info() message is being written and "INFO" is a lower level than "WARNING", the message is not recorded.

# The format option is used to customize the default settings of the log message. This additional functionality improves the readability and effectiveness of the log files. After a logger is created, there are only certain attributes that can be changed, like the logger level.
# Therefore, it's important to plan the needs of the logger before creating the object.

import logging

# os.chdir(".\\Module2\\Day27")
log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day27_logging.log",
                    level=logging.DEBUG,
                    format=log_formatter)
logger = logging.getLogger()
logger.info("This is a custom info message.")
logger.warning("This is a custom warning message.")

# example
import logging

# os.chdir(".\\Module2\\Day27")

log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day27_logging.log",
                    level=logging.DEBUG,
                    format=log_formatter,
                    filemode="w")
logger = logging.getLogger()
logger.debug("This is a custom debug message.")
logger.info("This is a custom info message.")
logger.warning("This is a custom warning message.")
logger.error("This is a custom error message.")
logger.critical("This is a custom critical message.")
