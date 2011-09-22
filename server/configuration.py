import socket

MASK_ERRORS = True



#ERROR MESSAGES
ERROR_NOIMAGE = { 'status':'failed', 'code':101, 'error':'The required POST field \'image\' was not supplied' }
ERROR_IMAGEERROR = { 'status':'failed', 'code':102, 'error':'The image supplied could not be ready by the system' }


#IMAGE PROCESSING
MIN_COLOR_COUNT = 100

if socket.gethostname() == 'matt-griffiths':
    MASK_ERRORS = False