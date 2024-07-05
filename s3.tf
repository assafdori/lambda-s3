resource "aws_s3_bucket" "source_bucket" {
  bucket = "source-bucket-26121996"
  acl    = "private"

  versioning {
    enabled = true
  }

  tags = {
    Name        = "source-bucket-26121996"
  }
}

resource "aws_s3_bucket" "destination_bucket" {
  bucket = "destination-bucket-26121996"
  acl    = "private"

  versioning {
    enabled = true
  }

  tags = {
    Name        = "destination-bucket-26121996"
  }
}
