# Resume webite Class

from aws_cdk import core as cdk
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_s3_deployment as s3deploy


class ResumeWebsiteCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self,"MyFirstBucket-letsago", 
            versioned=False,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_ssl=True,
            website_index_document="index.html",
            public_read_access=True
        )
        
        s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset('./content.zip')],
            destination_bucket=bucket,
            destination_key_prefix="/"
        )
