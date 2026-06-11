from app.config import settings
from app.ui import build_ui

if __name__ == "__main__":
    app = build_ui()
    app.launch(server_name=settings.host, server_port=settings.port)
