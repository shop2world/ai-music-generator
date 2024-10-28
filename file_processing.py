# file_processing.py

import openai
import json
import logging
import re
from dotenv import load_dotenv
import os
from pydantic import BaseModel, ValidationError
from typing import List

# .env 파일 로드
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)

# Pydantic 모델 정의
class MusicPrompt(BaseModel):
    music_title: str
    music_style_tags: List[str]
    music_lyric: str

def extract_json(content: str) -> dict:
    """
    응답에서 JSON 객체를 추출하여 반환.
    JSON 형식이 아닌 경우에는 문자열로부터 JSON 객체를 파싱하고, 파싱 실패 시 예외 발생.
    """
    json_match = re.search(r'{.*}', content, re.DOTALL)
    if json_match:
        json_str = json_match.group()
        try:
            parsed_json = json.loads(json_str)
            return parsed_json
        except json.JSONDecodeError:
            logging.error("JSON 디코딩 실패. 올바른 JSON 형식이 아닙니다.")
            raise ValueError("OpenAI 응답에서 JSON 형식을 추출할 수 없습니다.")
    else:
        logging.error("JSON 형식을 포함하지 않은 응답입니다.")
        raise ValueError("OpenAI 응답에서 JSON 형식을 찾을 수 없습니다.")

def chat_text_openai(prompt: str) -> dict:
    for attempt in range(3):  # 최대 3회 시도
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "user",
                        "content": f"""{prompt}

반환 형식은 반드시 아래 JSON 형식만 사용하십시오:
{{
    "music_title": "제목",
    "music_style_tags": ["태그1", "태그2"],
    "music_lyric": "가사 내용"
}}
JSON 이외의 어떤 설명도 포함하지 마세요."""
                    }
                ]
            )

            result = response['choices'][0]['message']['content'].strip()
            logging.info(f"Response content: {result}")

            result_json = extract_json(result)
            validated_data = MusicPrompt(**result_json)
            return validated_data.dict()

        except (ValueError, ValidationError) as e:
            logging.warning(f"응답 파싱 실패 (시도 {attempt + 1}/3): {str(e)}")
            if attempt == 2:  # 마지막 시도 실패 시 예외 발생
                raise e
            prompt = "정확한 JSON 형식으로만 응답해 주세요."  # 명확한 응답 요청 메시지 추가
