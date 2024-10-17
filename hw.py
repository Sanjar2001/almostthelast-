import re

def extract_image_descriptions(text):
    pattern = r'\[IMAGE\]\{(.*?)\}'
    return re.findall(pattern, text)

def extract_plain_text(text):
    pattern = r'\[IMAGE\]\{.*?\}'
    return [part.strip() for part in re.split(pattern, text) if part.strip()]

def parse_text_with_images(text):
    result = []
    parts = re.split(r'(\[IMAGE\]\{.*?\})', text)
    for part in parts:
        if part.startswith('[IMAGE]'):
            content = re.search(r'\{(.*?)\}', part).group(1)
            result.append({"type": "image", "content": content})
        elif part.strip():
            result.append({"type": "text", "content": part.strip()})
    return result

# Тесты для проверки функций
if __name__ == "__main__":
    # Тест для задачи 1
    text1 = "[IMAGE]{imagedescription}[IMAGE]{imagedescription2}Sometext[IMAGE]{imagedescription3}"
    text2 = "[IMAGE]{imagedescription}Sometext[IMAGE]{imagedescription2}"
    
    print("Задача 1:")
    print(extract_image_descriptions(text1))
    print(extract_image_descriptions(text2))

    # Тест для задачи 2
    text3 = "[IMAGE]{imagedescription}[IMAGE]{imagedescription2}Sometext[IMAGE]{imagedescription3}Sometext2"
    text4 = "[IMAGE]{imagedescription}Sometext[IMAGE]{imagedescription2}"
    
    print("\nЗадача 2:")
    print(extract_plain_text(text3))
    print(extract_plain_text(text4))

    # Тест для задачи 3
    text5 = "Some[IMAGE]{image1}text[IMAGE]{image2}here."
    text6 = "[IMAGE]{imagedescription}Sometext[IMAGE]{imagedescription2}"
    
    print("\nЗадача 3:")
    print(parse_text_with_images(text5))
    print(parse_text_with_images(text6))

