resource "aws_api_gateway_rest_api" "restapi" {
  body = "${data.template_file.openapispec.rendered}"
  name = var.apiname
}

data "template_file" "openapispec" {
  template = "${file(var.openapispec_path)}"
}