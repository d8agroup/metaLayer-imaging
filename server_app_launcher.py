from server.application import app
import socket

if socket.gethostname() == 'matt-griffiths':
    app.run(debug=True, port=5001)
else:
    app.run(debug=True, host='0.0.0.0')