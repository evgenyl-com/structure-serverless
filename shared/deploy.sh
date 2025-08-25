BRANCH=main
REGION=us-east-1
COMPANY=example
ACCOUNT=123430161152
DNS=example.com
ZONE=Z01234335N5678D3MZLU
SSL=arn:aws:acm:us-east-1:123430161152:certificate/1234cba1-f4e9-46f1-84c8-0676160a0e4a
FOLDER=$(basename "$(pwd)")
BUILD=$(git rev-parse --short HEAD)
ECR=${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com
ECR_FULL=${ECR}/${FOLDER}
IMAGE=${ECR_FULL}:${BUILD}


sam deploy --stack-name ${BRANCH}-${REGION}-${COMPANY}-${FOLDER} \
           --region ${REGION} \
           --capabilities CAPABILITY_NAMED_IAM \
           --parameter-overrides "ParameterKey=BRANCH,ParameterValue=${BRANCH}" \
                                 "ParameterKey=REGION,ParameterValue=${REGION}" \
                                 "ParameterKey=BLOCK,ParameterValue=${FOLDER}" \
                                 "ParameterKey=COMPANY,ParameterValue=${COMPANY}" \
                                 "ParameterKey=DNS,ParameterValue=${DNS}" \
                                 "ParameterKey=SSL,ParameterValue=${SSL}" \
                                 "ParameterKey=IMAGE,ParameterValue=${IMAGE}" \
           --image-repository ${ECR_FULL}