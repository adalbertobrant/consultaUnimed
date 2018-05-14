# Consulta Unimed
Consulta de autorização de procedimentos de maneira automatizada.

## Instruções:
1. Crie uma conta no Twitter e cadastre uma nova [API](https://apps.twitter.com/)
1. Confira nas permissões se o acesso é read and write
1. Crie os tokens necessários
1. Crie um arquivo keys.py que tenha a seguinte estrutura com os dados obtidos da nova API
 
```shell
#!/usr/local/bin/python
keys = dict(consumer_key = 'VALOR', consumer_secret = 'VALOR', access_token = 'VALOR', access_token_secret = 'VALOR')
```

1. Edite a linha 22 do arquivo unimed.py, inserindo o endereço de onde está o formulário inicial de entrada
1. Caso deseje, você pode automatizar a tarefa de consulta, gerando um script no shell e colocando o mesmo para rodar via cron ou caso o seu sistema utilize o systemd, no nosso caso utilizamos o systemd devido a versão e distribuição do S.O utilizado.

## Exemplo de configuração do systemd para consulta a cada 6 horas
1. Crie um arquivo script para a shell e dê autoridade de execução ao mesmo

```shell
#!/bin/sh
python2 /home/nome_do_usuario/script.sh
```

1. Crie um arquivo chamado **unimed.timer** no diretório system do systemd
```
[Unit]
Description=Roda o programa a cada 6horas

[Timer]
OnBootSec=30min
OnUnitActiveSec=6h
Unit=unimed.service

[Install]
WantedBy=multi-user.target
```

1. Crie um arquivo chamado **unimed.service** no diretório system do systemd</p>
```
[Unit]
Description=Consultar a Unimed

[Service]
ExecStart=/home/nome_do_usuario/script.sh
```

1. Atualize o daemon
```sudo systemctl daemon-reload```

1. Inicie o serviço
```sudo systemctl start unimed.service```
   
1. Verifique o status do timer
```systemctl list-timers --all```
