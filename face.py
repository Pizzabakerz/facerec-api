import face_recognition
import os
from pathlib import Path
def facecheck(unknown_image_path):
    try:
        files = os.listdir("registerdface")
        results_dic = {
            'name':"not found",
            'distance' : 100,
            'status': "False"
        }
        for i in range(len(files)):
            if files[i][0] != '.':
                known_image_one = face_recognition.load_image_file("/home/jacksonjegadheeson/facerec-api/registerdface/"+files[i])                
                unknown_image = face_recognition.load_image_file(unknown_image_path)

                known_image_encoding_one = face_recognition.face_encodings(known_image_one)[0]                
                unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

                result = face_recognition.compare_faces([known_image_encoding_one], unknown_encoding)                
                distance = face_recognition.face_distance([known_image_encoding_one], unknown_encoding)                                
                if result[0] == True:
                    file_name = Path("/home/jacksonjegadheeson/facerec-api/registerdface/"+files[i]).stem
                    if distance < results_dic['distance']:
                        results_dic['name'] = file_name
                        results_dic['distance'] = distance[0]
                        results_dic['status'] = "True"
            
    except IndexError as e:
        results = "invalid image"
        return results
    except Exception as e:
        results = e   
        return results 
    return results_dic

# distance = face_recognition.face_distance([known_image_encoding], unknown_encoding)

# result = facecheck("captured/unknown.jpg")
# print(result)