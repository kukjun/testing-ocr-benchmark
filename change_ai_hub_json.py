import json


def change_ai_hub_data():
    with open("ai_hub_training_data/printed_data_info.json", "r", encoding="utf-8") as file:
        data = json.load(file)  # JSON 데이터를 Python dict로 변환


    # 텍스트 파일로 저장하기
    with open("ai_hub_training_data/mdb_data/gt.txt", "w", encoding="utf-8") as txt_file:
        # 리스트의 각 항목을 텍스트 파일에 씁니다.
        for annotation in data["annotations"]:
            image_id = annotation['image_id']
            text = annotation['text']
            txt_file.write(f"images/{image_id}.png\t{text}\n")

change_ai_hub_data()
