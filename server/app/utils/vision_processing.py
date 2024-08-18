import base64
import os
import cv2


def process_images_to_base64(images):
    base64_images = []
    for image in images:
        image_data = image.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
        base64_images.append(base64_image)
    return base64_images


def process_video(video_file):
    video_path = os.path.join('/tmp', video_file.filename)
    video_file.save(video_path)

    video = cv2.VideoCapture(video_path)
    base64Frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

    video.release()
    return base64Frames

def process_video(video_file):
    video_path = os.path.join('/tmp', video_file.filename)
    video_file.save(video_path)

    video = cv2.VideoCapture(video_path)
    base64Frames = []
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        _, buffer = cv2.imencode(".jpg", frame)
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

    video.release()
    return base64Frames

