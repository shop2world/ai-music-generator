from file_processing import chat_text_openai
from generate_music import generate_music
import streamlit as st

def generate_music_from_prompt(prompt):
    # OpenAI를 통해 음악 프롬프트 생성
    prompt_data = chat_text_openai(prompt)

    # Suno AI API를 사용하여 음악 생성
    music_urls = generate_music(
        prompt_data["music_title"], prompt_data["music_style_tags"], prompt_data["music_lyric"]
    )
    return music_urls

st.title("AI 음악 생성기")
prompt = st.text_input("프롬프트를 입력하세요:")

if st.button("음악 생성"):
    if prompt:
        music_urls = generate_music_from_prompt(prompt)
        st.write("생성된 음악 URL:")
        for url in music_urls:
            st.write(url)
    else:
        st.warning("프롬프트를 입력해 주세요.")
