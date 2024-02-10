# Pdf Extract 
import os
import fitz
import requests
import base64
from concurrent.futures import ThreadPoolExecutor


# pdf Extract func
def extract_images_from_pdf(pdf_path, output_folder):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    # Iterate through each page
    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        # Iterate through each image on the page
        for image_index, img in enumerate(page.get_images(full=True)):
            # Get the XREF of the image
            xref = img[0]
            # Extract the image data
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Save the image to a file
            image_path = f"{output_folder}/page{page_number + 1}_image{image_index + 1}.png"
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)

    # Close the PDF document
    pdf_document.close()



# Function to perform OCR on an image
def ocr_image(image_path, api_key):
    endpoint = "https://vision.googleapis.com/v1/images:annotate"
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
        "User-Agent": "FirebaseML_[DEFAULT] Google-API-Java-Client Google-HTTP-Java-Client/1.25.0-SNAPSHOT (gzip)",
        "x-android-package": "com.inverseai.image_to_text_OCR_scannes",
        "x-android-cert": "C9E5C6094C5B966C4DD3C8E65B144622E21AC254"
    }
    params = {
        "key": api_key
    }

    with open(image_path, "rb") as image_file:
        image_content = base64.b64encode(image_file.read()).decode("utf-8")

    request_body = {
        "requests": [{
            "image": {"content": image_content},
            "features": [{"type": "TEXT_DETECTION"}]
        }]
    }

    response = requests.post(
        endpoint,
        headers=headers,
        params=params,
        json=request_body
    )

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        print(response.text)
        return None

# Function to process image and save OCR result
def process_image(image_path, output_folder, api_key):
    result = ocr_image(image_path, api_key)
    if result:
        output_path = os.path.join(output_folder, os.path.splitext(
            os.path.basename(image_path))[0] + ".txt")
        with open(output_path, "w", encoding="utf-8") as output_file:
            if "textAnnotations" in result["responses"][0]:
                text = result["responses"][0]["textAnnotations"][0]["description"]
                output_file.write(text.encode("utf-8").decode("utf-8"))
            else:
                output_file.write("No text found.")

# Function to process images in a folder using multiple threads
def process_images_in_folder(input_folder, output_folder, api_key):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    with ThreadPoolExecutor(max_workers=25) as executor:
        image_paths = [os.path.join(input_folder, filename) for filename in os.listdir(
            input_folder) if filename.endswith(('.jpg', '.jpeg', '.png'))]
        executor.map(lambda x: process_image(
            x, output_folder, api_key), image_paths)
        






# This func for Local Single Photos
def ocr_image_single(image_path, api_key):
    endpoint = "https://vision.googleapis.com/v1/images:annotate"
    headers = {
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip",
        "User-Agent": "FirebaseML_[DEFAULT] Google-API-Java-Client Google-HTTP-Java-Client/1.25.0-SNAPSHOT (gzip)",
        "x-android-package": "com.inverseai.image_to_text_OCR_scannes",
        "x-android-cert": "C9E5C6094C5B966C4DD3C8E65B144622E21AC254"
    }
    params = {
        "key": api_key
    }

    with open(image_path, "rb") as image_file:
        image_content = base64.b64encode(image_file.read()).decode("utf-8")

    request_body = {
        "requests": [{
            "image": {"content": image_content},
            "features": [{"type": "TEXT_DETECTION"}]
        }]
    }

    response = requests.post(
        endpoint,
        headers=headers,
        params=params,
        json=request_body
    )

    if response.status_code == 200:
        result = response.json()
        if "textAnnotations" in result["responses"][0]:
            text = result["responses"][0]["textAnnotations"][0]["description"]
            return text
        else:
            return "No Text Tound, Please Provide Photos."
    else:
        return "Error: {}".format(response.status_code)
