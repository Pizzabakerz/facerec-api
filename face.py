import face_recognition
def facecheck(known_image_path,unknown_image_path):
    known_image = face_recognition.load_image_file("test/rajinikanth.jpg")
    unknown_image = face_recognition.load_image_file("test/rajinikanth.jpg")

    known_image_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces([known_image_encoding], unknown_encoding)
    return results[0]
# distance = face_recognition.face_distance([known_image_encoding], unknown_encoding)

