import os
import json
import re
from PIL import Image

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def process_dir(directory, prefix="img"):
    webp_files = []
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return []
        
    for i, file in enumerate(sorted(os.listdir(directory), key=natural_sort_key)):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.avif')) and not file.endswith('.webp'):
            img_path = os.path.join(directory, file)
            try:
                img = Image.open(img_path)
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")
                # Sanitize filename
                clean_name = re.sub(r'[^a-zA-Z0-9_-]', '_', file.rsplit('.', 1)[0])
                webp_name = f"{clean_name}.webp"
                webp_path = os.path.join(directory, webp_name)
                img.save(webp_path, 'webp')
                print(f"Converted {file} to {webp_name} in {directory}")
                webp_files.append(webp_name)
            except Exception as e:
                print(f"Error converting {file}: {e}")
        elif file.endswith('.webp'):
            webp_files.append(file)
            
    webp_files = list(set(webp_files))
    webp_files.sort(key=natural_sort_key)
    return webp_files

trust_dir = '/home/arun/SIDDAGANGA/trust'
events_dir = '/home/arun/SIDDAGANGA/events'
index_file = '/home/arun/SIDDAGANGA/index.html'

gallery_files = process_dir(trust_dir)
event_files = process_dir(events_dir)

# Update index.html directly to avoid CORS issues
if os.path.exists(index_file):
    with open(index_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    js_gallery = json.dumps(gallery_files)
    js_events = json.dumps(event_files)
    
    # We will look for // --- GALLERY DATA --- and replace everything until // --------------------
    
    pattern = r'(// --- GALLERY DATA ---\s*)([\s\S]*?)(\s*// --------------------)'
    
    replacement = rf'\1const galleryImages = {js_gallery};\n  const eventsImages = {js_events};\3'
    
    new_html = re.sub(pattern, replacement, html)
    
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Updated galleryImages and eventsImages inside index.html successfully.")
else:
    print("index.html not found!")
