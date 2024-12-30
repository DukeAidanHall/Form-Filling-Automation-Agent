# Advanced AI Form-Filling Automation Agent

This repository contains a Python-based automation agent designed to interact with online forms (e.g., Google Forms) and provide intelligent responses using a GPT-based model from Hugging Face. The agent mimics human behavior during form completion, making it ideal for advanced automation tasks that require thoughtful, AI-generated inputs.

## Features

- **Human-Like Form Filling**: Automates form-filling tasks with randomized delays and human-like typing behavior.
- **Hugging Face GPT-Neo Integration**: Uses GPT-Neo (EleutherAI/gpt-neo-2.7B) to generate intelligent responses to form questions.
- **Customizable Configuration**: Easy to configure target form URLs and other parameters.
- **Logging with Loguru**: Provides robust logging to track the agent's actions and debug issues.

---

## Components

### 1. Configuration

The program uses the following key configuration variables:
- `TASK_URL`: The URL of the form to automate (e.g., a Google Form).
- `GECKO_PATH`: Path to the GeckoDriver executable for Selenium.
- `MODEL_NAME`: Hugging Face model name (e.g., `EleutherAI/gpt-neo-2.7B`).

### 2. Dependencies

- **Core Libraries**: `time`, `random`, `re`
- **Selenium**: For browser automation.
- **Loguru**: For advanced logging.
- **Transformers**: For GPT-Neo model integration.

To install dependencies, use:
```bash
pip install selenium loguru transformers
```

### 3. AI Integration

- **Model Initialization**:
  The agent initializes a GPT-Neo model from Hugging Face:
  ```python
  tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
  model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
  ```
- **Text Generation**:
  The `call_huggingface_model` function generates AI-driven responses to questions provided by the form:
  ```python
  input_ids = tokenizer.encode(question, return_tensors="pt")
  output = model.generate(input_ids, max_length=100, temperature=0.7, num_return_sequences=1)
  answer = tokenizer.decode(output[0], skip_special_tokens=True)
  ```

### 4. Selenium Automation

- **Browser Setup**:
  The program uses Selenium to automate Firefox with GeckoDriver:
  ```python
  service = Service(GECKO_PATH)
  driver = webdriver.Firefox(service=service)
  ```
- **Form Interaction**:
  Randomized delays and human-like typing simulate natural user interaction:
  ```python
  def send_keys_human_like(element, text):
      for char in text:
          element.send_keys(char)
          time.sleep(random.uniform(0.02, 0.08))
  ```

### 5. Logging

Logs are generated using Loguru, making it easy to track execution and debug issues:
```python
logger.add("data_input.log", rotation="10 MB")
```
Key logs include:
- Model loading and response generation.
- Browser actions and interactions.
- Error handling and troubleshooting.

### 6. Main Program Flow

The `__main__` function provides an interactive CLI for the user:
- **Start**: Launch the automation process.
- **Stop**: Exit the program.
```python
while True:
    cmd = input("\nType 'start' to run the automation, or 'stop' to exit: ").strip().lower()
    if cmd == "start":
        run_automation()
    elif cmd == "stop":
        print("Exiting the program.")
        break
    else:
        print("Unrecognized input. Type 'start' or 'stop'.")
```

---

## Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-form-filling-agent.git
```

2. Install dependencies:
```bash
pip install selenium loguru transformers
```

3. Download GeckoDriver and set the `GECKO_PATH` in the script:
   - [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)
   - Update the path in the configuration section.

4. Update the `TASK_URL` to your target form.

5. Run the program:
```bash
python main.py
```

---

## Troubleshooting

1. **Hugging Face Model Freezing**:
   - Use a smaller model (e.g., `EleutherAI/gpt-neo-125M`) for testing.
   - Ensure sufficient memory (16GB+ RAM recommended).

2. **Selenium Issues**:
   - Verify GeckoDriver is installed and `GECKO_PATH` is correct.
   - Ensure Firefox is updated.

3. **Debugging Logs**:
   - Check `data_input.log` for detailed execution logs.

---

## Future Improvements

- Add support for other browsers (e.g., Chrome).
- Enable dynamic form parsing to handle complex forms.
- Add GPU support for faster Hugging Face model inference.

