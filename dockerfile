FROM python:3.10.12-alpine3.18

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies:
COPY requirements.txt .
RUN pip install -r requirements.txt

# Run the application:
COPY bot.py .
COPY app.py .
COPY db.py .
COPY main.py .

CMD ["python", "main.py"]
