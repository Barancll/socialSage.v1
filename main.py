import text_generator
import image_generator
import packaging

def run_pipeline():
    print("SocialSage pipeline başlatılıyor...")
    text_content = text_generator.generate_text_content()
    print("Metin içerikleri oluşturuldu.")
    
    # Eğer text_content string ise, onu sözlüğe çeviriyoruz.
    if isinstance(text_content, str):
        text_content = {"posts": [text_content], "weekly_report": ""}
    
    # Text generator'den alınan metni prompt olarak kullanıyoruz.
    if text_content.get("posts") and len(text_content["posts"]) > 0:
        image_prompt = text_content["posts"][0]
    else:
        image_prompt = "Modern technology illustration"  # Varsayılan prompt

    images = image_generator.generate_dalle_image(image_prompt)
    print("Görseller oluşturuldu.")
    
    archive_file = packaging.create_archive(text_content, images)
    print("İçerikler paketlendi. Oluşturulan dosya:", archive_file)

if __name__ == "__main__":
    run_pipeline()
