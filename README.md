# Elastic stack (ELK) + Filebeat on Docker

Project fork from [deviantony/docker-elk](https://github.com/deviantony/docker-elk).

This fork show how to implements ELK stack + filebeat on Docker + docker-compose.

# Structure
![Screen Shot 2021-05-31 at 09 24 34](https://user-images.githubusercontent.com/45940140/120192894-24e27780-c1f2-11eb-8a81-7911fbcd2a0c.png)

# About
We have one (or more) application (python for example) what write some logs on `application/logs/.log`, and the `filebeat` will read this file and send to `logstash` that will do regex filter and after also send to `elasticsearch` and finally we'll build some graphics on `kibana`.

# App example
This simple `python` example will write some logs for us.
```py
import os
import uuid
import time

import log


def hello_log():
    while True:
        log.registry(log.LOGGING_ENUM.INFO, f'Info {uuid.uuid4()}')
        log.registry(log.LOGGING_ENUM.WARNING, f'Warning {uuid.uuid4()}')
        log.registry(log.LOGGING_ENUM.ERROR, f'Error {uuid.uuid4()}')
        time.sleep(15)


if __name__ == '__main__':
    if not os.path.exists(os.path.join(os.getcwd(), 'logs', '.log')):
        os.mkdir(f'{os.getcwd()}/logs3')

    hello_log()
```

*ps: I split the logs in a specific module: `log.py`*

# Logs example
```
28/05/2021 20:33:19 INFO     || 3e860697f14e || my_module || Company Name || Info 2473c107-aff8-4b48-85d6-a7ef6cdf89a6
28/05/2021 20:33:19 WARNING  || 3e860697f14e || my_module || Company Name || Warning 9a2d445a-5859-4f6a-8496-059a04c461d3
28/05/2021 20:33:19 ERROR    || 3e860697f14e || my_module || Company Name || Error d336fe31-86f9-4abe-b0c1-3738f5965351
28/05/2021 20:33:24 INFO     || 3e860697f14e || my_module || Company Name || Info a469d96b-564e-4af9-a874-ef2237ae3e71
28/05/2021 20:33:24 WARNING  || 3e860697f14e || my_module || Company Name || Warning a8a123b3-3379-4000-8c8a-83629a4ecd05
28/05/2021 20:33:24 ERROR    || 3e860697f14e || my_module || Company Name || Error 6e07dbeb-8969-4b95-97df-c1253c934d19
28/05/2021 20:33:29 INFO     || 3e860697f14e || my_module || Company Name || Info 9c6c5e09-2001-48ba-a33a-f2f2729b68a8
```
Click [here](https://github.com/lfvilella/ELK/blob/main/logstash/patterns/default.conf#L103) to see the regex from this.

# Running
```
$ make build
```

This step takes a few minutes to start ELK and all services to connect.

# See what's happening
```sh
$ docker-compose logs -f  # all containers
$ docker-compose logs -f <name>  # [app, elasticsearch, logstash, filebeat, kibana]
```

# Kibana
Go to http://localhost:5601/ to access kibana.

### Default credentials
```
username: elastic
password: changeme
```

### Search for `index patterns`
<img width="1440" alt="Screen Shot 2021-05-31 at 10 03 42" src="https://user-images.githubusercontent.com/45940140/120197594-822cf780-c1f7-11eb-8acb-b3f797f11544.png">

### Create index patterns
We set the index to `my_index_patterns` on [logstash.conf](https://github.com/lfvilella/ELK/blob/main/logstash/pipeline/logstash.conf#L18)

![image](https://user-images.githubusercontent.com/45940140/120199138-485cf080-c1f9-11eb-8d18-299656032e7d.png)
*ps: don't care about my old tests*

![image](https://user-images.githubusercontent.com/45940140/120199367-89550500-c1f9-11eb-8a66-9516c25f8709.png)
Screen Shot 2021-05-31 at 10.22.40![image](https://user-images.githubusercontent.com/45940140/120199959-2a43c000-c1fa-11eb-856a-2102be03a91c.png)
*Select timestamp or not* and `CREATE INDEX PATTERNS`

![image](https://user-images.githubusercontent.com/45940140/120200568-df767800-c1fa-11eb-98b4-9ddbe2991998.png)

#### Select `my_index_patterns` and see the logs comming
![image](https://user-images.githubusercontent.com/45940140/120200655-f321de80-c1fa-11eb-8972-d08af423f1c7.png)

## Let's create one visualization

### Go to sidebar > dashboard > Create Dashboard
<img width="1440" alt="Screen Shot 2021-05-31 at 10 30 09" src="https://user-images.githubusercontent.com/45940140/120200862-2e241200-c1fb-11eb-8b15-59b175d7bd86.png">

### Click on `Create Panel` > `Aggregation Based`
![image](https://user-images.githubusercontent.com/45940140/120201104-6fb4bd00-c1fb-11eb-9bc7-c30388953147.png)

### Select bar chart and choose `my_index_patterns`
![image](https://user-images.githubusercontent.com/45940140/120201193-8a873180-c1fb-11eb-9ada-9f2469100189.png)

### Let's create X-axis
![image](https://user-images.githubusercontent.com/45940140/120201437-d20dbd80-c1fb-11eb-9b22-b888ef052043.png)

![image](https://user-images.githubusercontent.com/45940140/120201514-e8b41480-c1fb-11eb-9659-ae3b8772ee7d.png)

*Click to update to see changes*

### Create Split Series too, and select terms > status.keyword > update > save return
![image](https://user-images.githubusercontent.com/45940140/120202535-12217000-c1fd-11eb-97cb-275314fdf3a3.png)

## Dashboard created 🥳
![image](https://user-images.githubusercontent.com/45940140/120202646-38dfa680-c1fd-11eb-83fe-1f5449899545.png)
*just save to persist*


# References
- [deviantony/docker-elk](https://github.com/deviantony/docker-elk)
- [waldemarnt/elk-compose](https://github.com/waldemarnt/elk-compose)
