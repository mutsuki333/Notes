# Drone cli

## Add ssh public key to drone secrets

```shell
drone secret add --repository Repo/Name --name deploy_key --data @/PATH/TO/SSH/id_rsa
```
