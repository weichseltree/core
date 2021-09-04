import time
# import cv2
# import ipywidgets as widgets

def array_to_png(image):
    import cv2
    import numpy as np
    
    _, ret = cv2.imencode('.png', np.flip(image, axis=2))
    return ret.tobytes()


def plot_image(image):
    import ipywidgets as widgets
    from IPython.display import display
    image = widgets.Image(value=array_to_png(image), format='png')
    display(image)
    

def save_image(image, filename):
    png_image = array_to_png(image)
    
    success = False
    attempts = 0
    while not success and attempts < 10:
        try:
            with open(filename, 'wb') as f:
                f.write(png_image)
            success = True
        except OSError as e:
            attempts += 1
            time.sleep(10)
    
    if attempts == 10:
        raise OSError(f'Saving {filename} failed 10 times.')


def load_image(filename):
    import cv2
    import numpy as np
    
    return np.flip(cv2.imread(filename), axis=2)

