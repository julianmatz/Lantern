import argparse
import base64
import json
import os
import subprocess

# Get the current script's directory
__dir__ = os.path.dirname(os.path.realpath(__file__))

# Initialize the argument parser
parser = argparse.ArgumentParser(description='Create Kubernetes secrets and .env file for Lantern.')

# Add arguments for specifying environment and controller namespace
parser.add_argument('--env', default='local', help='Environment to create the secrets for (default: local)')
parser.add_argument('--namespace', default='lantern', help='Namespace to use for the controllers (default: lantern)')

args = parser.parse_args()

# Set environment and namespace based on user inputs
env = args.env
namespace = args.namespace

# Define the paths for the input and output files
secrets_file = os.path.join(__dir__, ".secrets/.", env, ".json")
sealed_secrets_yaml_file = os.path.join(__dir__, "kubernetes/sealedsecrets.yml")  # Sealed secrets file
env_file = os.path.join(__dir__, ".env")  # .env file in the project's root directory

# Check if the secrets file exists
if not os.path.isfile(secrets_file):
    print(f"Secrets file {secrets_file} not found.")
    sys.exit(1)

# Load secrets from json file
with open(secrets_file) as file:
    secrets = json.load(file)

# Write secrets to .env file
with open(env_file, 'w') as env_file:
    for key, value in secrets.items():
        try:
            numeric_value = int(value)
            if str(numeric_value) == value:  # ensure the conversion doesn't lose precision
                value = numeric_value  # replace the string value with the integer if possible
        except ValueError:
            pass  # not a numeric string, keep as is

        env_file.write(f'{key}={value}\n')

# Encode secrets to base64
encoded_secrets = {key: base64.b64encode(value.encode()).decode() for key, value in secrets.items()}

# Prepare the secret dictionary
data = {key: encoded_secret for key, encoded_secret in encoded_secrets.items()}

secret = {
    "apiVersion": "v1",
    "kind": "Secret",
    "metadata": {"name": "secrets", "namespace": namespace},
    "type": "Opaque",
    "data": data,
}

# Run kubeseal command to seal the secrets
with open(sealed_secrets_yaml_file, "w") as out_file:
    process = subprocess.Popen(
        ["kubeseal", "--format=yaml", f"--controller-namespace={namespace}"], stdin=subprocess.PIPE, stdout=out_file
    )
    process.communicate(input=json.dumps(secret).encode("utf-8"))

# Check the return code of the subprocess
if process.returncode != 0:
    print(f"kubeseal command failed with return code: {process.returncode}.")
    sys.exit(1)
