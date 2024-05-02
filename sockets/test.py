import cv2
from deepface import DeepFace
camera = cv2.VideoCapture(0)
def ver(imgPath, camera):
    
    if not camera.isOpened():
        print("Error: Unable to open camera.")
        return "error"

    ret, frame = camera.read()
    cv2.imwrite("fv.jpg", frame)
    image = cv2.imread('fv.jpg')

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        expanded_x = max(0, x - int(w * 0.5))
        expanded_y = max(0, y - int(h * 0.5))
        expanded_w = min(image.shape[1] - expanded_x, int(w * 2))
        expanded_h = min(image.shape[0] - expanded_y, int(h * 2))

        cropped_image = image[expanded_y:expanded_y+expanded_h, expanded_x:expanded_x+expanded_w]

        cv2.imwrite('mainImg.jpg', cropped_image)
        try:
            result = DeepFace.verify("mainImg.jpg", imgPath, model_name="VGG-Face", detector_backend="opencv", distance_metric="cosine", enforce_detection=True, align=True, normalization="base")
        
            if result["verified"]:
                return "v"
            else:
                return "f"
        except ValueError as e:
            print(e)
    else:
        return "n"

while True:
    v = ver('nikshe.png', camera)
    if v == 'v':
        print('Verified')
        break
    elif v == "f":
        print("Verification failed")
    elif v == "n":
        print("No face detected.")
