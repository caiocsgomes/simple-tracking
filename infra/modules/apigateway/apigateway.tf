resource "aws_api_gateway_rest_api" "restapi" {
  body = data.template_file.openapispec.rendered
  name = var.apiname
}

data "template_file" "openapispec" {
  template = file(var.openapispec_path)
}

resource "aws_api_gateway_deployment" "deployment" {
  rest_api_id = aws_api_gateway_rest_api.restapi.id

  triggers = {
    redeployment = sha1(jsonencode(aws_api_gateway_rest_api.restapi.body))
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "stage" {
  deployment_id = aws_api_gateway_deployment.deployment.id
  rest_api_id   = aws_api_gateway_rest_api.restapi.id
  for_each      = var.stages_config
  stage_name    = each.key
}