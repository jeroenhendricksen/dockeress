FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env
WORKDIR /source

# For MacOS amd64 (M1) set ARG RUNTIME to linux-arm64
ARG RUNTIME=linux-x64

# Copy necessary files and restore as distinct layer
COPY *.csproj .
RUN dotnet restore -r ${RUNTIME} /p:PublishReadyToRun=true

# Copy everything else and build
COPY . ./
# /p:PublishTrimmed=true
RUN dotnet publish -c Release -o /app -r ${RUNTIME} --self-contained true --no-restore /p:PublishReadyToRun=true /p:PublishSingleFile=true
#RUN dotnet publish -c Release -o /app --no-restore

# Build runtime image
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY --from=build-env /app .

EXPOSE 80

# Start
ENTRYPOINT ["./aspnetapp"]
