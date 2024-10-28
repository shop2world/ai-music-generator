import requests
import time
import os

# API 설정
endpoint = "https://api.sunoaiapi.com/api/v1"
headers = {
    "api-key": os.getenv("SUNO_API_KEY"),  # 환경 변수에서 Suno API 키를 불러옵니다
    "Content-Type": "application/json"
}

def create_music_task(title, tags, prompt, negative_tags="", model="chirp-v3-5"):
    # 태그가 리스트인 경우 쉼표로 구분된 문자열로 변환
    if isinstance(tags, list):
        tags = ",".join(tags)
    data = {
        "title": title,
        "tags": tags,
        "prompt": prompt,
        "negative_tags": negative_tags,
        "mv": model,
    }
    try:
        response = requests.post(f"{endpoint}/gateway/generate/music", headers=headers, json=data)
        response.raise_for_status()  # 상태 코드가 200이 아닐 경우 예외 발생
        return response.json()
    except Exception as e:
        return {"error": f"API 요청 중 오류가 발생했습니다: {e}"}

def query_result(ids):
    ids_str = ",".join(ids)  # ID들을 쉼표로 구분된 문자열로 결합
    try:
        response = requests.get(f"{endpoint}/gateway/query?ids={ids_str}", headers=headers)
        response.raise_for_status()  # 상태 코드가 200이 아닐 경우 예외 발생
        return response.json()
    except Exception as e:
        return {"error": f"API 요청 중 오류가 발생했습니다: {e}"}

def generate_music(title, tags, prompt, negative_tags="", model="chirp-v3-5"):
    task_data = create_music_task(title, tags, prompt, negative_tags, model)

    # task_data에서 song_id를 안전하게 추출
    task_ids = []
    if 'data' in task_data:
        task_ids = [task.get("song_id") for task in task_data["data"] if "song_id" in task]

    # 작업 완료 확인
    while task_ids:  # task_ids가 비어 있지 않을 때만 반복
        results = query_result(task_ids)

        # 결과가 리스트인지 확인하고, 각 결과의 상태를 체크
        if isinstance(results, list) and all(isinstance(result, dict) for result in results):
            if all(result.get("status") in ["complete", "error"] for result in results):
                return [result.get("audio_url") for result in results if result.get("status") == "complete"]
        
        time.sleep(1)  # 상태 확인 대기
    
    return []  # 작업이 완료되지 않거나 오류가 발생한 경우 빈 리스트 반환
