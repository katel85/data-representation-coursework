from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
        return "Hello Mammy"
        
if __name__ == "__main__":
    app.run(debug=True)

# run in cmd enviroment as below
''' C:\Users\kate_\Data Representation\data-representation-coursework\Labs\Week8-Flask (main -> origin)                    
(venv) λ python a_server.py                                                                                            
 * Serving Flask app 'a_server'                                                                                        
 * Debug mode: on                                                                                                      
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead. 
 * Running on http://127.0.0.1:5000                                                                                    
Press CTRL+C to quit                                                                                                   
 * Restarting with stat                                                                                                
 * Debugger is active!                                                                                                 
 * Debugger PIN: 434-882-680                                                                                           
127.0.0.1 - - [29/Nov/2022 16:14:25] "GET / HTTP/1.1" 200 -                                                            
127.0.0.1 - - [29/Nov/2022 16:14:25] "GET /favicon.ico HTTP/1.1" 404 -           

                                      '''

# other way is to run in cmd by using flas k app
'''C:\Users\kate_\Data Representation\data-representation-coursework\Labs\Week8-Flask (main -> origin)                      
(venv) λ set FLASK_APP=a_server                                                                                          
                                                                                                                         
C:\Users\kate_\Data Representation\data-representation-coursework\Labs\Week8-Flask (main -> origin)                      
(venv) λ run flask                                                                                                       
'run' is not recognized as an internal or external command,                                                              
operable program or batch file.                                                                                          
                                                                                                                         
C:\Users\kate_\Data Representation\data-representation-coursework\Labs\Week8-Flask (main -> origin)                      
(venv) λ flask run                                                                                                       
 * Serving Flask app 'a_server'                                                                                          
 * Debug mode: off                                                                                                       
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.   
 * Running on http://127.0.0.1:5000                                                                                      
Press CTRL+C to quit                                                                                                     
                                                                                                                         
'''