"""
Logger Manager - управління логуванням
"""

import logging
from pathlib import Path
from datetime import datetime
import config

class LoggerManager:
    """Менеджер логування"""
    
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.log_file = self._create_log_file()
        self._setup_logger()
    
    def _create_log_file(self):
        """Створити файл логу"""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = config.LOGS_DIR / f"lir_{timestamp}.log"
        return log_file
    
    def _setup_logger(self):
        """Налаштування логера"""
        
        self.logger = logging.getLogger("LirModernizer")
        self.logger.setLevel(logging.DEBUG)
        
        # Файловий обробник
        file_handler = logging.FileHandler(self.log_file, encoding='utf-8')
        file_level = logging.DEBUG if self.verbose else logging.INFO
        file_handler.setLevel(file_level)
        
        # Консольний обробник
        console_handler = logging.StreamHandler()
        console_level = logging.INFO if self.verbose else logging.ERROR
        console_handler.setLevel(console_level)
        
        # Формат
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Додати обробники
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def info(self, message):
        """Інформаційне повідомлення"""
        self.logger.info(message)
        if self.verbose:
            print(f"[+] {message}")
    
    def error(self, message):
        """Повідомлення про помилку"""
        self.logger.error(message)
        print(f"[ERROR] {message}")
    
    def warning(self, message):
        """Попередження"""
        self.logger.warning(message)
        if self.verbose:
            print(f"[!] {message}")
    
    def debug(self, message):
        """Відладкове повідомлення"""
        self.logger.debug(message)
        if self.verbose:
            print(f"[DEBUG] {message}")
    
    def success(self, message):
        """Повідомлення про успіх"""
        self.logger.info(f"SUCCESS: {message}")
        print(f"[OK] {message}")
    
    def close(self):
        """Закрити логер"""
        for handler in self.logger.handlers:
            handler.close()
