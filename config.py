"""
PyFood Configuration
"""

import os
from datetime import timedelta

DEBUG = os.getenv('DEBUG', 'True') == 'True'
TESTING = False
SECRET_KEY = os.getenv('SECRET_KEY', 'pyfood-dev-secret-key')

HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', 5000))
WORKERS = int(os.getenv('WORKERS', 4))

UPDATE_INTERVAL = 2
HISTORY_SIZE = 300

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 85
DISK_THRESHOLD = 90
TEMP_WARNING = 80
TEMP_CRITICAL = 95

AUTO_OPTIMIZE = False
KILL_TIMEOUT = 5
CACHE_CLEANUP_ENABLED = True
MEMORY_OPTIMIZATION_ENABLED = True
DISK_CLEANUP_ENABLED = True
NETWORK_OPTIMIZATION_ENABLED = True

MIN_PROCESS_MEMORY = 10
MONITOR_CHILD_PROCESSES = True

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
LOG_FILE = 'pyfood.log'
LOG_MAX_SIZE = 10 * 1024 * 1024
LOG_BACKUP_COUNT = 5

DATA_DIR = os.getenv('DATA_DIR', './data')
REPORT_DIR = os.path.join(DATA_DIR, 'reports')
CACHE_DIR = os.path.join(DATA_DIR, 'cache')

API_RATE_LIMIT = 100
API_TIMEOUT = 30

PERMANENT_SESSION_LIFETIME = timedelta(days=7)
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')

ENABLE_ANALYTICS = True
ENABLE_RECOMMENDATIONS = True
ENABLE_AUTOSTART_MANAGER = True
ENABLE_TEMPERATURE_MONITORING = True
ENABLE_PROCESS_MANAGER = True

TEMP_PATHS = ['/tmp', '/var/tmp', '/var/cache/apt/archives']
CACHE_PATHS = ['~/.cache', '~/.local/share/Trash']

SYSTEM_COMMANDS = {
    'package_manager': 'apt',
    'sudo': 'sudo',
    'sync': 'sync',
}
