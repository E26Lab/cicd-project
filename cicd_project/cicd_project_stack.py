import aws_cdk as cdk
from aws_cdk.aws_codepipeline import Pipeline, Artifact
from aws_cdk.aws_codepipeline_actions import GitHubSourceActionProps as codepipeline_actions
import aws_cdk.aws_secretsmanager as secretsmanager
import aws_cdk.aws_codecommit as codecommit
from constructs import Construct
from aws_cdk import pipelines


class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        source_artifact = cdk.aws_codepipeline.Artifact()
        cloud_assembly_artifact = cdk.aws_codepipeline.Artifact()
        
        pipeline = Pipeline(self, "Pipeline",
        cloud_assembly_artifact=cloud_assembly_artifact,
        pipeline_name="E26Pipeline",
        source_action = codepipeline_actions(
            action_name="GitHub_Source",
            owner="E26Lab",
            repo="cicd-project",
            oauth_token=cdk.SecretValue.secrets_manager("github-token"),
            output=source_artifact,
            branch="main"
        ), 
        synth_action=pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                install_command='npm install -g aws-cdk && pip install -r requirements.txt',
                synth_command= 'cdk synth'))









        
      
    
                    