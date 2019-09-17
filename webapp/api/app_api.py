from flask_restplus import Resource, Namespace

app_ns = Namespace('app', description='app related operations')


@app_ns.route('/echo')
class Echo(Resource):
    def get(self):
        return {
            "version": "1.0.2-alpha",
            "status": "App is up and running!"
        }