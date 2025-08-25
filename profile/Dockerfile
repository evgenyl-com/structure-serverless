FROM public.ecr.aws/lambda/python:3.13
COPY . .
RUN dnf install -y gcc g++ make python3-devel
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
CMD [ "lambda_function.lambda_handler" ]
