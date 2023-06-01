# --encoding:utf-8--

import logging
import logging.handlers
import os
import time

project_root = os.path.dirname(os.path.dirname(__file__))
configFilePath = os.path.abspath(project_root + "/config.ini")


class CommonLogger:
    def __init__(self):
        log_dir_path = os.getcwd() + '/dolphin/log'
        if not os.path.exists(log_dir_path):
            os.makedirs(log_dir_path)
        now_date_time = time.strftime('%Y-%m-%d', time.localtime())
        log_file_name = log_dir_path + "/spider" + now_date_time + ".log"
        self.logger = logging.getLogger('dolphin')
        # to avoid the log output multi times
        # we should check the logger handler before add handler
        # https://stackoverflow.com/questions/17745914/python-logging-module-is-printing-lines-multiple-times
        if not self.logger.hasHandlers():
            file_handler = logging.handlers.RotatingFileHandler(log_file_name,
                                                                maxBytes=1024 * 1024 * 100,
                                                                backupCount=1)
            logger_format = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
            formatter = logging.Formatter(logger_format)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
            self.logger.setLevel(logging.INFO)

    def get_logger(self):
        return self.logger

    @staticmethod
    def init_log_path(file_name: str):
        log_dir_path = os.getcwd() + '/dolphin/log'
        if not os.path.exists(log_dir_path):
            os.makedirs(log_dir_path)
        now_date_time = time.strftime('%Y-%m-%d', time.localtime())
        log_file_name = log_dir_path + "/" + file_name + now_date_time + ".log"
        return log_file_name

    def get_logger_by_name(self, name: str):
        logger = logging.getLogger(name)
        log_file_name = self.init_log_path(name)
        if not logger.hasHandlers():
            file_handler = logging.handlers.RotatingFileHandler(log_file_name,
                                                                maxBytes=1024 * 1024 * 100,
                                                                backupCount=1)
            logger_format = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
            formatter = logging.Formatter(logger_format)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.INFO)
        return logger

    def get_cert_logger(self):
        return self.get_logger_by_name("cert-logger")

    def get_task_sender_logger(self):
        return self.get_logger_by_name("cruise-task-sender")

    def get_executor_logger(self):
        return self.get_logger_by_name("cruise-task-executor")

    def get_common_logger(self):
        return self.get_logger_by_name("common")
