# consulta Unimed

Consulta de Autorização de Procedimentos  de maneira automatizada.

# Instruções :

1- Fazer uma conta no Tweeter e cadastrar a nova API --> https://apps.twitter.com/
1.1-Conferir em Permissions se o Access é read and write
2- Criar os Tokens necessários 
3- Criar um arquivo keys.py que tenha a seguinte estrutura com os dados obtidos da nova API
 
 !/usr/local/bin/python
 ## -*- coding: utf-8 -*-

  keys = dict(
    consumer_key =          'VALOR',
    consumer_secret =       'VALOR',
    access_token =          'VALOR',
    access_token_secret =   'VALOR',
)

4- Editar a linha 22 do arquivo unimed.py , colocando o endereço de onde esta o formulário inicial de entrada

5- Caso deseje você pode automatizar a tarefa de consulta, gerando um script no shell e colocando o mesmo para rodar via cron ou caso o seu sistema utilize o systemd, no nosso caso utilizamos o systemd devido a versão e distribuição do S.O utilizado.

# Exemplo de configuração do systemd para consulta a cada 6 horas

1- criar um arquivo script para a shell e dar autoridade de execução ao mesmo
## 
#!/bin/sh
python2 /home/endereço de onde esta o script deve estar completo começando a partir da home/script.sh


2- Criar o arquivo .timer no diretório system do systemd 
# unimed.timer

[Unit]
Description=Roda o programa a cada 6horas

[Timer]
# tempo de espera deṕois do boot
OnBootSec=30min

# tempo entre cada execução
OnUnitActiveSec=6h
Unit=unimed.service

[Install]
WantedBy=multi-user.target

3- Criar o arquivo .service no diretório system do systemd
# unimed.service

[Unit]
Description=Consultar a Unimed

[Service]
ExecStart=/home/endereço do seu script/script.sh


4- Atualizar o 
   sudo systemctl daemon-reload

5- Iniciar o serviço 
   sudo systemctl start unimed.service
   
6- Verificar o status timer
  <p> systemctl list-timers --all</p>
   









