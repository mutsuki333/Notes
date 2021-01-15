# Docker Cheat Sheet

## Common cmds

| Cmd                            | Description                   |
| ------------------------------ | ----------------------------- |
| docker image prune             | Prune unused images           |
| docker ps -a                   | list all containers           |
| docker stats                   | list running container status |
| docker exec -it NAME /bin/bash | Attach to shell               |
| docker logs --follow           | attach to see log             |
| docker network prune           | remove unused network         |
| docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' NAME | get ip of a cantainer|
