# Sample Hello World ASP.NET application

Example taken from [here](https://learn.microsoft.com/en-us/visualstudio/get-started/csharp/tutorial-aspnet-core?view=vs-2022).

## To run this on Mac OS with an ARM processor (locally)

First off, [download the binary](https://dotnet.microsoft.com/en-us/download) and install it.

Then download [dotnet-install.sh](https://dot.net/v1/dotnet-install.sh), make it executable and run:

    $./dotnet-install.sh --channel 7.0 --runtime aspnetcore

Now you have `dotnet` available from the shell, including asp.net support.

    dotnet --info
