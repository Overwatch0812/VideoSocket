
import cloudinary
from cloudinary import CloudinaryImage
from cloudinary.uploader import upload
import cloudinary.api
import json
from PIL import Image
import io
import cv2
import numpy as np

cloudinary.config(
    cloud_name='dxfeoomxq',
    api_key='161781681775932',
    api_secret='zZfLjYyOrMpEp183llo8xqVt7eU'
)

def uploadImage(image_data, name):
    try:
        success, encoded_image = cv2.imencode('.jpg', image_data)
        
        if not success:
            print("Error encoding image to JPEG format")
            return None
        
        image_data_bytes = np.array(encoded_image).tobytes()
        upload_result = upload(image_data_bytes, public_id=name, unique_filename=False, overwrite=True)

        print("Image uploaded successfully!")
        # print("Image URL:", upload_result['secure_url'])

        return upload_result['secure_url']
    except Exception as e:
        # print("Error uploading image:", e)
        return None