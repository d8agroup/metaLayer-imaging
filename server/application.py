from flask import Flask, request, jsonify
from PIL import Image
from configuration import *

app = Flask(__name__)

@app.route('/test')
def test():
    return "worked"

@app.route('/processimage', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify(ERROR_NOIMAGE)
    
    file = request.files['image']
    
    try:
        image = Image.open(file)
    except Exception, e:
        if MASK_ERRORS:
            return ERROR_IMAGEERROR
        raise e
    
    colors = []
    
    try:
        unsorted_colors = image.getcolors(MAX_COLOR_DEPTH)
        if unsorted_colors != None:
            if SORT_COLORS:
                colors = sorted(unsorted_colors, key=lambda color: color[0] * -1)
            else:
                colors = unsorted_colors
            if MIN_COLOR_COUNT > 0:
                colors = [color for color in colors if color[0] >= MIN_COLOR_COUNT]
    except MemoryError, e:
        if not MASK_ERRORS:
            raise e
    
    return_data = {
        'histogram':image.histogram(),
        'colors':colors,
        'format':image.format,
        'mode':image.mode,
        'size':image.size
    }
    
    return jsonify(return_data)
