FROM maven:3-jdk-8

WORKDIR /app

COPY . .

RUN mvn package

CMD ["tail", "-f", "/dev/null"]