import os
import PyPDF2
import json
import traceback

def read_file(file):
    if file.name.endswith(".pdf"):
        try:
            pdf_reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            raise Exception("Error while reading the pdf file")
    
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    
    else:
        raise Exception("Unsupported File Format")
    

def get_table_data(quiz_str):
    try:
        print(quiz_str)
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        for key,value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(
                [
                    f"{option}-> {option_value}" for option, option_value in value["options"].items()
                ]
            )
            correct=value["correct"]
            quiz_table_data.append({"MCQ":mcq,"Choices":options,"Correct":correct})
        return quiz_table_data
    except:
        raise Exception