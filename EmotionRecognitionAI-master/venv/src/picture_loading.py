import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

image_dir = "C:\\Users\\stav\\Desktop\\insta\\stav\\pics\\angry"
# image_dir = "C:\\Users\\stav\\Desktop\\EmotionRecognitionAI\\venv\\src\\samples\\train"

current_id = 0
file_id = 1
for root, dirs, files in os.walk(image_dir):

    for filename in files:

        if filename.endswith("png") or filename.endswith("jpg") or filename.endswith("JPG") or filename.endswith("webp"):
            path = os.path.join(root, filename)

            # new_path = os.path.join(root, filename+ '.jpg')
            new_path = os.path.join(root, filename)

            os.rename(path, new_path)
            file_id = file_id + 1

