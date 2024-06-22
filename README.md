# OCI Generative AI Cohere Command R/R+ Chat Examples

This repository contains example scripts and notebooks demonstrating how to use Oracle Cloud Infrastructure (OCI) Generative AI with Cohere for chat applications.

## Contents

- `oci_genai_cohere_chat_example.ipynb`: Jupyter notebook example for OCI GenAI Cohere chat
- `oci_genai_cohere_chat_example.py`: Python script version of the chat example
- `oci_genai_cohere_chat_streaming_example.ipynb`: Jupyter notebook example for OCI GenAI Cohere chat with streaming
- `oci_genai_cohere_chat_streaming_example.py`: Python script version of the streaming chat example

## Requirements

To run these examples, you'll need:

- Python 3.x
- Required Python packages (listed in `requirements.txt`)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/kutsushitaneko/oci-genai-cohere-chat-examples.git
   cd oci-genai-cohere-chat-examples
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Copy `.env_sample` to `.env`
   - Fill in your OCI credentials and configuration in the `.env` file

## Usage

### Jupyter Notebooks

1. Start Jupyter Notebook:
   ```
   jupyter notebook
   ```

2. Open either `oci_genai_cohere_chat_example.ipynb` or `oci_genai_cohere_chat_streaming_example.ipynb`

3. Run the cells in the notebook to see the chat examples in action

### Python Scripts

Run either of the Python scripts directly:

```
python oci_genai_cohere_chat_example.py
```

or

```
python oci_genai_cohere_chat_streaming_example.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT No Attribution License (MIT-0). This license allows you to use, copy, modify, and distribute the software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

The full text of the license can be found here: https://opensource.org/licenses/MIT-0

## Contact

For any questions or issues, please open an issue in this repository.
