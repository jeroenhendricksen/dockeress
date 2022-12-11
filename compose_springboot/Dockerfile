FROM maven:3-eclipse-temurin-17 as builder
WORKDIR /usr/src/app
COPY pom.xml .
RUN mvn --no-transfer-progress dependency:go-offline -B

COPY src /usr/src/app/src
RUN mvn package

FROM eclipse-temurin:17-jre
COPY --from=builder /usr/src/app/target/java-demo-0.0.1-SNAPSHOT.jar /usr/app/app.jar
EXPOSE 8080
ENTRYPOINT exec java $JAVA_OPTS -jar /usr/app/app.jar
