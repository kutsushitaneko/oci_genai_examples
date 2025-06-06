# OCI Generative AI Cohere Command R/R+/A Chat Examples
[日本語](https://github.com/kutsushitaneko/oci_genai_examples/blob/main/README_ja.md)

This repository contains example scripts and notebooks demonstrating how to use Oracle Cloud Infrastructure (OCI) Generative AI with Cohere Command R/R+/A for chat applications.

## Articles (Japanese)
- [OCI Generative AI で Cohere Command R/R+ の Chat API を試してみる（Update: ストリームチャット対応）](https://qiita.com/yuji-arakawa/items/597c4bd9f3d5b4212b51)
- [地球爆破計画が未遂に終わった件、あるいは Safety Modes - OCI Generative AI サービス](https://qiita.com/yuji-arakawa/items/a8514999463363d13ec6)

## Contents

- `oci_genai_cohere_chat_example.ipynb`: Jupyter notebook example for OCI Generative AI Cohere Command R/R+/A chat
- `oci_genai_cohere_chat_example.py`: Python script version of the chat example
- `oci_genai_cohere_chat_streaming_example.ipynb`: Jupyter notebook example for OCI Generative AI Cohere Command R/R+/A chat with streaming
- `oci_genai_cohere_chat_streaming_example.py`: Python script version of the streaming chat example
- `oci_genai_cohere_chat_streaming_safety_modes_example.ipynb`: Jupyter notebook example for Safety Modes
   - [Related article (Japanese): 地球爆破計画が未遂に終わった件、あるいは Safety Modes - OCI Generative AI サービス](https://qiita.com/yuji-arakawa/items/a8514999463363d13ec6)
- `oci_genai_cohere_chat_streaming_ai_guardrails_api_example.ipynb`: Jupyter notebook example for PII masking using AI Guardrails API

## Requirements

Prerequisites for running the sample programs:

- Python 3.11.9 (tested)
- Required Python packages (listed in `requirements.txt`)

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/kutsushitaneko/oci_genai_examples
   cd oci_genai_examples
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Copy `.env_sample` to `.env`
   - Fill in your OCI credentials and model ID in the `.env` file

## Usage

### Jupyter Notebooks

1. Start Jupyter Notebook:
   ```
   jupyter notebook
   ```

2. Open `oci_genai_cohere_chat_example.ipynb`, `oci_genai_cohere_chat_streaming_example.ipynb`, or other notebooks

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

## License

This project is licensed under the MIT No Attribution License (MIT-0). This license allows you to use, copy, modify, and distribute the software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

The full text of the license can be found here: https://opensource.org/licenses/MIT-0

## Contact

For any questions or issues, please open an issue in this repository.
