# Stop ChromeOS Updates

Stop updates on managed chromebooks through the use of a proxy. The proxy will redirect requests to get updates to a non-existent site.

## Usage

First clone the github repository and cd into it
```
git clone https://github.com/doctor112-1/stop_updates_chromeos.git
cd stop_updates_chromeos
```

Then run
```
./mitmdump -s intercept.py
```

On the chromebook, go to the network you are connected to, and edit the proxy settings to the the ip of the machine running the proxy and the port address (default is 8080).
