# VULNERABILITY: Hardcoding sensitive credentials.
# These values will be stored in plain text in your version control system (Git),
# making them visible to anyone with access to the repository.

provider "aws" {
  region     = "us-east-1"
  access_key = "AKIAEXAMPLE123456789"  # CRITICAL: Secret leaked
  secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" # CRITICAL: Secret leaked
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
