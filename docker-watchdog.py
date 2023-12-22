#!/usr/bin/python3

import docker
import time
import sdnotify

notifier = sdnotify.SystemdNotifier()

client = docker.from_env()

notifier.notify('READY=1')

while True:
    notifier.notify('STATUS=Watching containers')
    health_states = {}

    for container in client.containers.list():
        container_state = container.attrs['State']
        if 'Health' in container_state:
            health_state = container_state['Health']
            health_states[container.id] = health_state

    healthy = all([health != 'unhealthy' for health in health_states])

    if not healthy:
        message = 'Containers unhealthy. Attempting to restart...'
        notifier.notify(f'STATUS={message}')
        for container in client.containers.list():
            container.restart()

    time.sleep(60)
