import os
from pathlib import Path

# 처리할 두 폴더 경로
image_dir = Path("/home/soyun/bee/dataset_ready/0619/images")
label_dir = Path("/home/soyun/bee/dataset_ready/0619/labels")

# 삭제 대상: 'Zone.Identifier'가 포함된 파일
def delete_zone_identifier_files(directory):
    deleted = 0
    for file in directory.iterdir():
        if "Zone.Identifier" in file.name:
            try:
                file.unlink()
                print(f"🗑️ 삭제됨: {file}")
                deleted += 1
            except Exception as e:
                print(f"⚠️ 삭제 실패: {file} -> {e}")
    print(f"\n✅ {directory} 폴더에서 총 {deleted}개 삭제 완료")

# 실행
delete_zone_identifier_files(image_dir)
delete_zone_identifier_files(label_dir)
