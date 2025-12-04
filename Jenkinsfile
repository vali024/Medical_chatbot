pipeline {
    agent {
        docker {
            // Docker image with AWS CLI + Docker CLI support
            image 'amazon/aws-cli:latest'
            args '-u root:root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        AWS_REGION = 'us-east-1'
        ECR_REPO = 'medicalchatbot'
        IMAGE_TAG = 'latest'
        SERVICE_NAME = 'llmops-medical-service'
    }

    stages {

        stage('Clone GitHub Repo') {
            steps {
                script {
                    echo 'Cloning GitHub repo to Jenkins...'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/vali024/Medical_chatbot.git'
                        ]]
                    )
                }
            }
        }

        stage('Build, Scan, and Push Docker Image to ECR') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-token'
                ]]) {
                    script {
                        echo "Fetching AWS Account ID..."
                        def accountId = sh(
                            script: "aws sts get-caller-identity --query Account --output text",
                            returnStdout: true
                        ).trim()

                        def ecrUrl = "${accountId}.dkr.ecr.${env.AWS_REGION}.amazonaws.com/${env.ECR_REPO}"
                        def imageFullTag = "${ecrUrl}:${IMAGE_TAG}"

                        sh """
                            echo "Logging into ECR..."
                            aws ecr get-login-password --region ${AWS_REGION} \
                                | docker login --username AWS --password-stdin ${ecrUrl}

                            echo "Building Docker Image..."
                            docker build -t ${env.ECR_REPO}:${IMAGE_TAG} .

                            echo "Running Trivy Scan..."
                            trivy image --severity HIGH,CRITICAL \
                                --format json -o trivy-report.json ${env.ECR_REPO}:${IMAGE_TAG} || true

                            echo "Tagging Image..."
                            docker tag ${env.ECR_REPO}:${IMAGE_TAG} ${imageFullTag}

                            echo "Pushing Image to ECR..."
                            docker push ${imageFullTag}
                        """

                        archiveArtifacts artifacts: 'trivy-report.json', allowEmptyArchive: true
                    }
                }
            }
        }
    }
}
