import openai
from datetime import datetime
import os
import json

# config.json dosyasını okuyarak API anahtarını alıyoruz
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

openai.api_key = config.get("OPENAI_API_KEY")

def generate_text_content():
    """
    GPT-4 kullanarak:
      - 2 adet sosyal medya gönderisi (posts)
      - 1 adet haftalık rapor (weekly_report)
    oluşturur.
    
    Returns:
        dict:
            {
                "posts": ["...gönderi metni 1...", "...gönderi metni 2..."],
                "weekly_report": "...haftalık rapor metni..."
            }
    """
    try:
        # 1) Sosyal medya gönderileri için promptlar
        post_prompts = [
            "Teknoloji alanındaki en son trendleri anlatan yaratıcı bir gönderi oluştur.",
            "Yeni yazılım inovasyonları hakkında ilgi çekici bir gönderi hazırla."
        ]

        posts = []
        for prompt in post_prompts:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a creative social media content generator."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                top_p=1.0,
                max_tokens=250
            )
            text = response.choices[0].message["content"].strip()
            posts.append(text)

        # 2) Haftalık rapor üretme
        weekly_report = generate_weekly_report()

        # 3) Metin içeriklerini sözlük olarak döndür
        return {
            "posts": posts,
            "weekly_report": weekly_report
        }

    except Exception as e:
        print("Metin içerik oluşturulurken hata oluştu:", e)
        return {
            "posts": [],
            "weekly_report": ""
        }

def generate_weekly_report():
    """
    Haftalık raporu oluşturmak için ayrı bir fonksiyon.
    """
    current_time = datetime.now().strftime("%d %B %Y, %H:%M")

    # Haftalık rapor için prompt
    weekly_prompt = (
        f"Bu haftanın teknoloji ve yazılım alanında en popüler konuları içeren bir haftalık rapor yaz. "
        f"Bugünün tarihi ve saati: {current_time}. "
        "Raporda öne çıkan trendler, önemli haberler, geleceğe yönelik öngörüler ve kısa öneriler bulunsun."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4",  # Erişiminiz yoksa gpt-3.5-turbo
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a knowledgeable content generator specializing in startup tech "
                    "and software topics."
                )
            },
            {"role": "user", "content": weekly_prompt}
        ],
        max_tokens=500,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.5
    )

    return response.choices[0].message["content"].strip()

if __name__ == "__main__":
    content = generate_text_content()
    #print("Gönderiler (posts):", content["posts"])
    #print("Haftalık Rapor (weekly_report):", content["weekly_report"])
