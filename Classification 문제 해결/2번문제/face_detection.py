import cv2
import mediapipe as mp
from mediapipe.framework.formats import location_data_pb2
import math


# denormalized image!

def _normalized_to_pixel_coordinates(normalized_x: float, normalized_y: float, image_width: int,image_height: int):
    """Converts normalized value pair to pixel coordinates."""
    # Checks if the float value is between 0 and 1.

    def is_valid_normalized_value(value: float) -> bool:
        return (value > 0 or math.isclose(0, value)) and (value < 1 or math.isclose(1, value))
    
    if not (is_valid_normalized_value(normalized_x) and is_valid_normalized_value(normalized_y)):
        # TODO: Draw coordinates even if it's outside of the image bounds.
        return None
    
    x_px = min(math.floor(normalized_x * image_width), image_width - 1)
    y_px = min(math.floor(normalized_y * image_height), image_height - 1)

    return x_px, y_px





mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils



# For static images:
IMAGE_FILES = ["Test.jpg"] # input images to cut with face

with mp_face_detection.FaceDetection(
    model_selection=1, min_detection_confidence=0.5) as face_detection:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
    results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Draw face detections of each face.
    if not results.detections:
        continue
    annotated_image = image.copy()
    for detection in results.detections:
        

        # mp_drawing.draw_detection(annotated_image, detection) # This function drwaw all point not only boundary box

        if not detection.location_data:
            continue
        if annotated_image.shape[2] != 3:
            raise ValueError('Input image must contain three channel bgr data.')
        image_rows, image_cols, _ = annotated_image.shape

        location = detection.location_data
        if location.format != location_data_pb2.LocationData.RELATIVE_BOUNDING_BOX:
            raise ValueError(
                'LocationData must be relative for this drawing funtion to work.')

        # # Draws bounding box if exists.
        if not location.HasField('relative_bounding_box'):
            continue
        relative_bounding_box = location.relative_bounding_box
        rect_start_point = _normalized_to_pixel_coordinates(
            relative_bounding_box.xmin, relative_bounding_box.ymin, image_cols,
            image_rows)
        rect_end_point = _normalized_to_pixel_coordinates(
            relative_bounding_box.xmin + relative_bounding_box.width,
            relative_bounding_box.ymin + relative_bounding_box.height, image_cols,
            image_rows)

        # cv2.rectangle(annotated_image, rect_start_point, rect_end_point, (255,0,0) , 2)

        # print(rect_start_point) # (211, 59)
        # print(rect_end_point) # (292, 140)

        # Y , X , C
        annotated_image = annotated_image[rect_start_point[1]:rect_end_point[1],rect_start_point[0]:rect_end_point[0]]

    # save the image
    cv2.imwrite('./tmp/annotated_image' + str(idx) + '.png', annotated_image)

