FROM robd003/python3.10

WORKDIR /selenium
ADD Report2.py .
COPY Report2.py /selenium
COPY report.csv /selenium



RUN pip install selenium
CMD ["python", "Report2.py"]