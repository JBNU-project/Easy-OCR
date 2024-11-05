/* Converting Learning Data Format to lmdb format */
import os

def generate_gt_file(image_dir, gt_file_path, input_txt_dir):
    """
    이미지 폴더에 있는 파일 경로를 기반으로 gt.txt 파일을 생성합니다.
    각 이미지에 대한 레이블은 이미지와 같은 이름의 텍스트 파일에서 읽어옵니다.

    Args:
        image_dir (str): 이미지 파일들이 있는 디렉터리 경로.
        gt_file_path (str): 생성될 gt.txt 파일의 경로.
        input_txt_dir (str): 레이블 텍스트 파일들이 있는 디렉터리 경로.
    """
    # gt.txt 파일 열기 (쓰기 모드)
    with open(gt_file_path, "w", encoding="utf-8") as gt_file:
        # 이미지 폴더 탐색
        for filename in os.listdir(image_dir):
            # 이미지 파일만 처리
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                # 이미지의 전체 경로
                image_path = os.path.join(image_dir, filename)
                
                # 같은 이름의 텍스트 파일 경로 설정
                label_file_path = os.path.join(input_txt_dir, os.path.splitext(filename)[0] + ".txt")
                
                # 텍스트 파일에서 라벨 읽기
                if os.path.exists(label_file_path):
                    with open(label_file_path, "r", encoding="utf-8") as label_file:
                        label = label_file.read().strip()  # 텍스트 파일 내용을 레이블로 사용
                else:
                    print(f"경고: {label_file_path} 파일이 존재하지 않습니다. 해당 이미지에 대한 레이블이 없습니다.")
                    continue  # 해당 이미지 건너뛰기
                
                # gt.txt에 이미지 경로와 레이블 기록
                gt_file.write(f"{image_path}\t{label}\n")
                print(f"{image_path}\t{label} 추가 완료")

# 사용 예시
image_dir = "/home/jbnu/바탕화면/Capstone4/images"  # 이미지 파일들이 있는 폴더 경로
gt_file_path = "/home/jbnu/바탕화면/Capstone4/gt.txt"  # 생성될 gt.txt 파일 경로
input_txt_dir = "/home/jbnu/바탕화면/Capstone4/labels"  # 텍스트 파일들이 있는 폴더 경로
generate_gt_file(image_dir, gt_file_path, input_txt_dir)
