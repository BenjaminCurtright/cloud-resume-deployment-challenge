
output "cloudfront_domain_name" {
  description = "CloudFront domain for the resume site"
  value       = aws_cloudfront_distribution.site.domain_name
}

output "api_gateway_invoke_url" {
  description = "Base invoke URL for the visitor counter API"
  value       = aws_apigatewayv2_stage.api_stage.invoke_url
}
