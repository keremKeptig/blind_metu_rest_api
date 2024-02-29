FROM python:3.10
WORKDIR "C:\Users\userpc\Desktop\pyCharm\rest_api_blind_metu:/app"
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["/bin/bash", "docker-entrypoint.sh"]

