FROM cypress/browser:latest
RUN apt-get install python 3 -y
RUN echo $(python3 -m site --user-base)
COPY requirments.txt .
ENV PATH /home/root/.local/bin:${PATH}
RUN apt-get update && apt-get install -y python 3-pip && pip install -r requirments.txt
COPY . .
CMD uvicorn main:app --host 0.0.0.0 --port 443