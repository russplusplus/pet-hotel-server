import os

from flask import Flask, request, make_response
import psycopg2

try:
    connection = psycopg2.connect(user = "russellkerber",
                                  password = "",
                                  host = "localhost",
                                  port = "5432",
                                  database = "pet-hotel")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

    def create_app(test_config=None):
    # create and configure the app
        app = Flask(__name__, instance_relative_config=True)
        app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        )

        if test_config is None:
            # load the instance config, if it exists, when not testing
            app.config.from_pyfile('config.py', silent=True)
        else:
            # load the test config if passed in
            app.config.from_mapping(test_config)
        
    
        
        # ensure the instance folder exists
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        # db = SQLAlchemy(app) 
        # a simple page that says hello
        @app.route('/hello')
        def hello():
            query = 'SELECT * FROM "owners";'
            # cursor.execute(query)
            # connection.commit()
            # body = ()
            # for taco in cursor:
            #     body = body + taco
            # print(body)
            # status = 'good'
            # returnData = (body, status)
            # headers = {"Content-Type": "application/json"}
            # return make_response(body, 200, headers=headers)
            return "in hello POST"

        @app.route('/owners', methods=['GET', 'POST', 'PUT', 'DELETE'])
        def routestuff():
            if request.method == 'GET':
                return 'Hello GET route'
            if request.method == 'POST':
                return 'Hello POST route'


        

        return app






except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
# finally:
    #closing database connection.
        # if(connection):
        #     cursor.close()
        #     connection.close()
        #     print("PostgreSQL connection is closed")





