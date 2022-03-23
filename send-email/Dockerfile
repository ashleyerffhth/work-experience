FROM robd003/python3.10


WORKDIR /send-email
COPY send_email.py /send-email
COPY report.pdf /send-email

ADD send_email.py .


RUN pip install schedule
#CMD ["python", "send_email.py"]