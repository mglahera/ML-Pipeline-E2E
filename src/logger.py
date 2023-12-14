import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=3)  # Crea un nuevo archivo cuando alcanza 10 KB y mantiene hasta 3 archivos de respaldo.
file_handler.setLevel(logging.DEBUG)  # Puedes ajustar el nivel según tus necesidades.
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

