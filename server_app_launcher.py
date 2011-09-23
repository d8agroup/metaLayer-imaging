from server.application import app
import socket

if socket.gethostname() == 'matt-griffiths':
    app.run(debug=True)
else:
    app.run(debug=True, host='0.0.0.0')