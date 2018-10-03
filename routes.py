from flask_restful import Api
from config import generate_session
from models import Test

app, port_num, session = generate_session()
my_api = Api(app)


@app.route('/api/test')
def test_route():
    session.add(Test())
    session.commit()
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True, port=port_num, host='0.0.0.0')
