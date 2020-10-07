FROM python:3.8
MAINTAINER stoporinjail
ADD main.py
CMD ["python","main.py"]
ENTRYPOINT ["python"]