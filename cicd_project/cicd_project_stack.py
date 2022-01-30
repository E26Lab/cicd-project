import aws_cdk as cdk
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from aws_cdk.aws_codepipeline_actions import GitHubSourceActionProps as codepipeline_actions
import aws_cdk.aws_secretsmanager as secretsmanager
from constructs import Construct

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        pipeline =  CodePipeline(self, "Pipeline") 
        source_output = CodePipeline.Artifact()
        source_action = codepipeline_actions.GitHubSourceAction(
            action_name="GitHub_Source",
            owner="E26Lab",
            repo="cicd-project",
            oauth_token=secretsmanager.SecretValue.secrets_manager("github-token"),
            output=source_output,
            branch="main"
        )
        pipeline.add_stage(
            stage_name="Source",
            actions=[source_action]
        )
                       
                    