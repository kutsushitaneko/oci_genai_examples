import oci
import os
from dotenv import load_dotenv, find_dotenv
import uuid

_ = load_dotenv(find_dotenv())

CONFIG_PROFILE = "DEFAULT"
config = oci.config.from_file(file_location='~/.oci/config', profile_name=CONFIG_PROFILE)
config["region"] = "us-chicago-1"

compartment_id = os.getenv("OCI_COMPARTMENT_ID") 
model_id = "cohere.command-a-03-2025"

generative_ai_inference_client = oci.generative_ai_inference.GenerativeAiInferenceClient(config=config, retry_strategy=oci.retry.NoneRetryStrategy(), timeout=(10,240))

INPUT_TEXT = "yuji.arakawa@oracle.com"
PII_TYPES = ["EMAIL"]

opc_request_id = str(uuid.uuid4())
print(f"opc_request_id: {opc_request_id}")

apply_guardrails_response = generative_ai_inference_client.apply_guardrails(
    apply_guardrails_details=oci.generative_ai_inference.models.ApplyGuardrailsDetails(
        input=oci.generative_ai_inference.models.GuardrailsTextInput(
            type="TEXT",
            content=INPUT_TEXT,
            language_code="en"), # en | es | en-US | zh-CN
        guardrail_configs=oci.generative_ai_inference.models.GuardrailConfigs(
            personally_identifiable_information_config=oci.generative_ai_inference.models.PersonallyIdentifiableInformationConfiguration(
                types=PII_TYPES)),
        compartment_id=compartment_id),
    opc_request_id=opc_request_id)

print(f"apply_guardrails_response.data: {apply_guardrails_response.data}")