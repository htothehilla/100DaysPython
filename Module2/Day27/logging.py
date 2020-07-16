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


import logging
import os

# os.chdir(".\\Module2\\Day27")

log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day27_logging.log",
                    level=logging.DEBUG,
                    format=log_formatter,
                    filemode="w")
logger = logging.getLogger()


def quadratic_formula(a: float, b: float, c: float) -> (float, float):
    """
    Solve for x in the quadratic formula.
        ax^2 + bx + c = 0
    :param a: float
    :param b: float
    :param c: float
    :return: Solve for x, Return the positive and negative roots as float in a tuple
    """
    logger.info(f"Quadratic Formula Solver: {a}x^2 + {b}x + {c} = 0")

    # Calculate the discriminant
    logger.debug(f"Calculate the discriminant: {b}^2 - 4*{a}*{c}")
    discrim = (b ** 2) - (4 * a * c)
    logger.debug(f"Discriminant: {discrim}")

    # Calculate the positive and negative roots
    logger.debug(f"Calculate the pos/neg roots: (-{b} +/- sqrt({discrim})) / (2*{a})")
    try:
        pos_root = (-b + (discrim ** 0.5)) / (2 * a)
        neg_root = (-b - (discrim ** 0.5)) / (2 * a)
        logger.debug(f"Positive Root: {pos_root}, Negative Root: {neg_root}")
        return pos_root, neg_root
    except ZeroDivisionError as err:
        logger.error(f"{a} cannot be equal to zero.\n{err}")
        raise
    except TypeError as err:
        logger.error(f"Invalid type.\n{err}")
        raise
    except ValueError as err:
        logger.error(f"Invalid value.\n{err}")
        raise
    finally:
        logger.debug("Function Complete")


roots = quadratic_formula(3, 4, 5)
print(roots)
