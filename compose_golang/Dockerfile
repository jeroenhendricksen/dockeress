FROM golang:1.17 as builder
WORKDIR /app
COPY . .
RUN go build -o app .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app .
CMD ["./app"]