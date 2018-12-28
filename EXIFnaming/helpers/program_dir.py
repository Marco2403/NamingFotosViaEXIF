import datetime as dt
import os
from logging import Logger


def get_saves_dir(*subpath):
    create_program_dir()
    return os.path.join(".EXIFnaming", "saves", *subpath)


def get_gps_dir(*subpath):
    return os.path.join(".EXIFnaming", "gps", *subpath)


def get_info_dir(*subpath):
    create_program_dir()
    return os.path.join(".EXIFnaming", "info", *subpath)


def get_setexif_dir(*subpath):
    create_program_dir()
    return os.path.join(".EXIFnaming", "setexif", *subpath)


def get_log_dir(*subpath):
    create_program_dir()
    return os.path.join(".EXIFnaming", "log", *subpath)


def create_program_dir():
    mainpath = ".EXIFnaming"
    subdirs = ["saves", "gps", "info", "setexif", "log"]
    for subdir in subdirs:
        path = os.path.join(mainpath, subdir)
        os.makedirs(path, exist_ok=True)


def log() -> Logger:
    if not log.logger:
        import logging
        logFormatter = logging.Formatter("%(asctime)s  %(message)s")
        rootLogger = logging.getLogger()

        timestring = dt.datetime.now().strftime("%y%m%d%H%M")
        fileHandler = logging.FileHandler(get_log_dir(timestring + ".log"))
        fileHandler.setFormatter(logFormatter)
        rootLogger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        rootLogger.addHandler(consoleHandler)
        rootLogger.setLevel(10)
        log.logger = rootLogger
    return log.logger


log.logger = None


def log_function_call(function_name: str, *parameters):
    parameters = [str(parameter) for parameter in parameters]
    parameter_str = ", ".join(parameters)
    log().info("call %s(%s)", function_name, parameter_str)
