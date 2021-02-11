from backend.app import create_app
from backend.settings import DEBUG, HOST, PORT

if __name__ == '__main__':
    app = create_app()
    app.run(
            host=HOST,
            port=PORT,
            debug=DEBUG
            )
