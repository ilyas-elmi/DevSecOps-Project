provider "aws" {
  region = "eu-west-2" # London region
}
resource "aws_s3_bucket" "zephrya00" {
  bucket = "zephrya00"
}
terraform {
  backend "s3" {
    # Replace this with your bucket name!
    bucket         = "zephrya00"
    key            = "global/s3/terraform.tfstate"
    region         = "eu-west-2"
  }
}