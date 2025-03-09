import zipfile
import os

def create_archive(text_content, images, archive_name="socialsage_output.zip"):
    """
    Metin ve görselleri bir zip arşiv dosyası halinde paketler.
    
    Args:
        text_content (dict): 'posts' listesi ve 'weekly_report' metnini içerir.
        images (dict): 'post_images' listesi ve 'weekly_report_image' dosya yolunu içerir.
        archive_name (str): Oluşturulacak zip dosyasının adı.
        
    Returns:
        str: Oluşturulan arşiv dosyasının adı.
    """
    try:
        # Metin içerikleri için geçici dosyalar oluşturuluyor
        text_files = []
        for idx, post in enumerate(text_content.get("posts", [])):
            filename = f"post_{idx+1}.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(post)
            text_files.append(filename)
        
        weekly_filename = "weekly_report.txt"
        with open(weekly_filename, "w", encoding="utf-8") as f:
            f.write(text_content.get("weekly_report", ""))
        text_files.append(weekly_filename)
        
        # Zip dosyasını oluşturma
        with zipfile.ZipFile(archive_name, 'w') as zipf:
            for file in text_files:
                zipf.write(file)
            for image_file in images.get("post_images", []):
                zipf.write(image_file)
            weekly_image = images.get("weekly_report_image", "")
            if weekly_image and os.path.exists(weekly_image):
                zipf.write(weekly_image)
        
        return archive_name
    except Exception as e:
        print("Paketleme sırasında hata oluştu:", e)
        return ""