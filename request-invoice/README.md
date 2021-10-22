# Http Invoice Request Server plugin


This plugin starts a minimal, rate limited HTTP Server and returns an invoice on the following GET requests:

``/invoice/<amount>/<description>``

```
$ lightning-cli invoiceserver start
started server successfully on port 8089

$ curl http://localhost:8809/invoice/100000/some-text-here
{"bolt11":"...","expires_at":...,"payment_hash":"...", ...}
```

``/payRequest?amount=...&comment=...``

```
$ lightning-cli invoiceserver start
started server successfully on port 8089

$ curl "http://localhost:8809/payRequest?amount=100000&comment=some-text-here"
{"pr":"...","routes":[]}
```

The webserver is rate-limited, meaning that only a certain amount of request per minute is allowed (to prevent DoS attacks).

The json invoice can be used by other services, for example a service for tipping, donations, PoS devicesen , ...


Once the plugin is active you can run `lightning-cli help invoiceserver` to
learn about the command line API:

Commands: `start`/`stop`/`restart`/`status`.

In the file `.lightning/bitcoin/.env` the `port` can be set (default 8089).

##### Onion routing
Exposing the url using Onion routing is easy. Install tor and 
add the service to `/etc/tor/torrc`
```
HiddenServiceDir /home/bitcoin/tor/request-invoice-service_v2/
HiddenServicePort 80 127.0.0.1:8809

```
and restart tor to create the url
```
$ systemctl stop tor && systemctl start tor
$ cat /home/bitcoin/tor/request-invoice-service_v2/hostname
fkfuvjrbj6cfqppq6xcgfwmp4p23wq2unzlnqmdi6ibqtg2aq7thp2qd.onion
```

Use tor browser to visit the url and create a invoice (and make a donation?).
http://fkfuvjrbj6cfqppq6xcgfwmp4p23wq2unzlnqmdi6ibqtg2aq7thp2qd.onion/invoice/1000/donation

##### Configuration

You can intialize the plugin with a specific port and address:

- `--requestinvoice-address=... (default 127.0.0.1)`
- `--requestinvoice-port=... (default 8809)`
