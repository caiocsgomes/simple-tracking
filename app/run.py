from utils.factory import create_app
from utils.config import ProdConfig, DevConfig
import os

if __name__ == '__main__':
    if os.getenv("ENV") == 'PROD':
        app = create_app(ProdConfig)
        app.run(port=5000, host="0.0.0.0", use_reloader=False)
    else:
        app = create_app(DevConfig)
        app.run(port=5000, host="127.0.0.1", use_reloader=True)
