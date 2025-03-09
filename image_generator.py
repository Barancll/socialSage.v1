import openai
import requests
import os
import json

# config.json dosyasından API anahtarını çekiyoruz.
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)
openai.api_key = config.get("OPENAI_API_KEY")

def generate_dalle_image(prompt, image_size="1024x1024"):
    """
    OpenAI'nın DALL-E modelini kullanarak yüksek kaliteli görsel üretir.
    
    Args:
        prompt (str): Görsel oluşturmak için açıklayıcı metin.
        image_size (str): Görselin boyutu. (Örnek: "1024x1024" daha yüksek çözünürlüktedir.)
    
    Returns:
        str veya None: Oluşturulan görselin dosya adı, hata durumunda None.
    """
    try:
        # OpenAI DALL-E API çağrısı; model parametresi yoktur, kullanılan model API tarafından belirlenir.
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=image_size
        )
        # API yanıtındaki ilk görsel URL'sini çekiyoruz.
        image_url = response["data"][0]["url"]
        image_data = requests.get(image_url).content
        # Görsel dosyasını kaydediyoruz.
        image_filename = "dalle_generated_image.png"
        with open(image_filename, "wb") as f:
            f.write(image_data)
        return image_filename
    except Exception as e:
        print("Görsel oluşturulurken hata:", e)
        return None

if __name__ == "__main__":
    # Örnek kullanım: Text generator'den alınan metni prompt olarak kullanabilirsiniz.
    sample_prompt = "A futuristic technology conference with vibrant neon lights, intricate details, and a modern urban skyline in the background."
    image_file = generate_dalle_image(sample_prompt)
    print("Oluşturulan görsel dosyası:", image_file)
