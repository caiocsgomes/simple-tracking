import os

from utils.config import ProdConfig, DevConfig, LocalConfig
from utils.factory import create_app

if __name__ == '__main__':
    if os.getenv("ENV") == 'LOCALHOST':
        app = create_app(LocalConfig)
        app.run(port=5000, host="0.0.0.0", use_reloader=True)
    elif os.getenv("ENV") == 'DEV':
        app = create_app(DevConfig)
        app.run(port=5000, host="0.0.0.0", use_reloader=True)
    else:
        app = create_app(ProdConfig)
        app.run(port=5000, host="0.0.0.0", use_reloader=False)
