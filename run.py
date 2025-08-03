from app import create_app
from app.database import init_db

app = create_app('development')

if __name__ == '__main__':
    init_db(app)
    app.run(debug=True)
