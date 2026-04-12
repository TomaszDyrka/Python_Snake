FROM python:3.13-slim-trixie@sha256:d168b8d9eb761f4d3fe305ebd04aeb7e7f2de0297cec5fb2f8f6403244621664

LABEL author="Tomasz Dyrka"
LABEL description="A simple snake game in terminal"

RUN useradd -m snakeusr
WORKDIR /game

COPY . .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
RUN pip install --no-cache-dir .[test]

RUN chown -R snakeusr:snakeusr /game
USER snakeusr

ENTRYPOINT ["./entrypoint.sh"]
