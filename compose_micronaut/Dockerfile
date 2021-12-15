FROM maven:3.8-openjdk-17 as builder
WORKDIR /usr/src/app
COPY micronaut-ws/pom.xml /usr/src/app/pom.xml
RUN mvn --no-transfer-progress dependency:go-offline -B

COPY micronaut-ws/src /usr/src/app/src
RUN mvn package

FROM openjdk:17-alpine
LABEL Maintainer="jeroen.hendricksen@infosupport.com"
COPY --from=builder /usr/src/app/target/micronaut-ws-0.1.jar /usr/app/app.jar
EXPOSE 8080
ENTRYPOINT exec java $JAVA_OPTS -jar /usr/app/app.jar
