FROM python:3
MAINTAINER stoporinjail
RUN pip install requests
ADD launcher.py
CMD ["python", "launcher.py"]
ENTRYPOINT ["python"]
