import face_recognition
import os
from pathlib import Path
def facecheck(unknown_image_path):
    try:
        files = os.listdir("/home/jacksonjegadheeson/facerec-api/registerdface")
        for i in range(len(files)):
            if files[i][0] != '.':
                known_image = face_recognition.load_image_file("/home/jacksonjegadheeson/facerec-api/registerdface/"+files[i])
                unknown_image = face_recognition.load_image_file(unknown_image_path)

                known_image_encoding = face_recognition.face_encodings(known_image)[0]
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

                results = face_recognition.compare_faces([known_image_encoding], unknown_encoding)
                if results[0] ==  True:
                    results = Path("/home/jacksonjegadheeson/facerec-api/registerdface/"+files[i]).stem
                    return results                    
    except IndexError as e:
        results = "invalid image"
        return results
    except Exception as e:
        results = e   
        return results 
    return results[0]
# distance = face_recognition.face_distance([known_image_encoding], unknown_encoding)

# result = facecheck("captured/unknown2.jpeg")
# print(result)