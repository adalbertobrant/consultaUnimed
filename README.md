# Consulta Unimed
Consulta de autorização de procedimentos de maneira automatizada.

## Instruções:
1. Crie uma conta no Twitter e cadastre uma nova [API](https://apps.twitter.com/)
1. Confira nas permissões se o acesso é read and write
1. Crie os tokens necessários
1. Crie um arquivo keys.py que tenha a seguinte estrutura com os dados obtidos da nova API
 
```shell
!/usr/local/bin/python
keys = dict(consumer_key = 'VALOR', consumer_secret = 'VALOR', access_token = 'VALOR', access_token_secret = 'VALOR')
```

1. Edite a linha 22 do arquivo unimed.py, inserindo o endereço de onde está o formulário inicial de entrada
1. Caso deseje, você pode automatizar a tarefa de consulta, gerando um script no shell e colocando o mesmo para rodar via cron ou caso o seu sistema utilize o systemd, no nosso caso utilizamos o systemd devido a versão e distribuição do S.O utilizado.

## Exemplo de configuração do systemd para consulta a cada 6 horas
1. Crie um arquivo script para a shell e dar autoridade de execução ao mesmo

```shell
#!/bin/sh
python2 /home/nome_do_usuario/script.sh
```

<p>2- Criar o arquivo .timer no diretório system do systemd </p>
#unimed.timer

<p>[Unit]</p>
<p>Description=Roda o programa a cada 6horas</p>

<p>[Timer]</p>
<p>##tempo de espera deṕois do boot</p>
<p>OnBootSec=30min</p>

<p>##tempo entre cada execução</p>
<p>OnUnitActiveSec=6h</p>
<p>Unit=unimed.service</p>

<p>[Install]</p>
<p>WantedBy=multi-user.target</p>

<p>3- Criar o arquivo .service no diretório system do systemd</p>
<p>##unimed.service</p>

<p>[Unit]</p>
<p>Description=Consultar a Unimed</p>

<p>[Service]</p>
<p>ExecStart=/home/endereço do seu script/script.sh</p>


<p>4- Atualizar o daemon</p>
<p>   sudo systemctl daemon-reload</p>

<p>5- Iniciar o serviço </p>
   <p>sudo systemctl start unimed.service</p>
   
<p>6- Verificar o status timer</p>
  <p> systemctl list-timers --all</p>
   









