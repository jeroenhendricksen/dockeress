FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build-env
WORKDIR /app

# Copy necessary files and restore as distinct layer
COPY *.csproj ./
RUN dotnet restore

# Copy everything else and build
COPY . ./
RUN dotnet publish -c Release -o out

# Build runtime image
# We need aspnet image here (instead of runtime) because
# of Apple M1 architecture shizzle
FROM mcr.microsoft.com/dotnet/aspnet:6.0
COPY --from=build-env /app/out .

# Start
ENTRYPOINT ["dotnet", "com.infosupport.dockeress.example.dll"]
