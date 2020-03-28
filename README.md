# COVID-19 PL
☣️ monitoring data regarding COVID-19 (coronavirus) situation in Poland

usage
-----

- installing dependencies: `pip install -r requirements.txt`
- getting data of all regions: `python app.py regions`
- getting data for the single region: `python app.py region <name>`, e.g. `python app.py region śląskie`
- getting summary for whole country: `python app.py summary`

collecting timeline data
-------------------------

create `covid_log_archive.sh` script:

```bash
#!/usr/bin/env bash
stat=$(python /path/to/repo/app.py summary | tail -n1)
when=$(date "+%Y-%m-%d %H:%M:%S")
echo "$when,$stat" | sed "s/;/,/g"  >> /path/to/log/covid_19_pl_archive.log
```

and add it as a cron job in your system, e.g.:

```
15 * * * * /path/to/script/covid_log_archive.sh
```

using script in i3 status bar
-----------------------------

clone this repo and create a bash script `covid_log.sh`:

```bash
#!/usr/bin/env bash
python /path/to/repo/app.py summary | tail -n1 | awk -F ";" '{print "☣ " $1 " ☠ " $2 }' > /path/to/log/covid_19_pl.log
```

then create `covid_19_pl.log` file, make it writeable and create a new cron job for this script, e.g.:

```
20 * * * * /path/to/script/covid_log.sh
```

next, add i3 config in your `~/.config/i3/config` file:

```

...
order += "read_file covid"
...

read_file covid {
        format = "%content"
        path = "/path/to/log/covid_19_pl.log"
}

...
```

references
----------

source of data: https://www.gov.pl/web/koronawirus/wykaz-zarazen-koronawirusem-sars-cov-2
