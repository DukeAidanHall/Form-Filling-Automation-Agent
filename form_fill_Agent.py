import time
import random
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from loguru import logger
from transformers import AutoModelForCausalLM, AutoTokenizer

logger.add("data_input.log", rotation="10 MB")

# -------------------------------------------------------------------------
# CONFIGURATION
# -------------------------------------------------------------------------

TASK_URL = "[Insert Link]"
GECKO_PATH = r"C:\Tools\geckodriver.exe"

# Hugging Face model configuration
MODEL_NAME = "EleutherAI/gpt-neo-125M"  # Free and open-source
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def random_delay(min_t=0.4, max_t=1.2):
    time.sleep(random.uniform(min_t, max_t))

def send_keys_human_like(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.02, 0.08))

def call_huggingface_model(question):
    """
    Call Hugging Face's GPT-Neo model to generate text.
    """
    logger.info(f"Asking Hugging Face model: {question}")
    try:
        # Tokenize the input
        input_ids = tokenizer.encode(question, return_tensors="pt")
        
        # Generate text
        output = model.generate(
            input_ids,
            max_length=100,
            temperature=0.7,
            num_return_sequences=1
        )
        
        # Decode the response
        answer = tokenizer.decode(output[0], skip_special_tokens=True)
        logger.info(f"Hugging Face model answered: {answer}")
        return answer
    except Exception as e:
        logger.error(f"Hugging Face model call failed: {e}")
        return "Error: Could not fetch answer from Hugging Face model."

def run_automation():
    logger.info("Starting advanced AI form-filling automation.")
    
    service = Service(GECKO_PATH)
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()

    try:
        driver.get(TASK_URL)
        random_delay(1, 2)

        # ... (the rest of your form-filling logic)
        # Example usage:
        question_text = "What is AI?"
        answer = call_huggingface_model(question_text)
        # Then fill the form with 'answer'
        # Example form filling logic
        # element = driver.find_element(By.XPATH, "your_xpath_here")
        # send_keys_human_like(element, answer)

        random_delay(2, 3)
    except Exception as e:
        logger.error(f"Error during form automation: {e}")
    finally:
        driver.quit()
        logger.info("Browser closed. Automation finished.")

if __name__ == "__main__":
    while True:
        cmd = input("\nType 'start' to run the automation, or 'stop' to exit: ").strip().lower()
        if cmd == "start":
            run_automation()
        elif cmd == "stop":
            print("Exiting the program.")
            break
        else:
            print("Unrecognized input. Type 'start' or 'stop'.")
