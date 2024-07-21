provider "aws" {
  region = "eu-west-2" # London region
}
resource "aws_s3_bucket" "zephrya00" {
  bucket = "zephrya00"
}