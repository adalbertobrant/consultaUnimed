# consulta Unimed

Consulta de Autorização de Procedimentos  de maneira automatizada.

# Instruções :
<p>
1- Fazer uma conta no Tweeter e cadastrar a nova API --> https://apps.twitter.com/</p>
<p>1.1-Conferir em Permissions se o Access é read and write</p>
<p>2- Criar os Tokens necessários </p>
<p>3- Criar um arquivo keys.py que tenha a seguinte estrutura com os dados obtidos da nova API</p>
 
 !/usr/local/bin/python
 ## -*- coding: utf-8 -*-

  keys = dict(
    consumer_key =          'VALOR',
    consumer_secret =       'VALOR',
    access_token =          'VALOR',
    access_token_secret =   'VALOR',
)

<p>4- Editar a linha 22 do arquivo unimed.py , colocando o endereço de onde esta o formulário inicial de entrada</p>

<p>5- Caso deseje você pode automatizar a tarefa de consulta, gerando um script no shell e colocando o mesmo para rodar via cron ou caso o seu sistema utilize o systemd, no nosso caso utilizamos o systemd devido a versão e distribuição do S.O utilizado.</p>

# Exemplo de configuração do systemd para consulta a cada 6 horas

<p>1- criar um arquivo script para a shell e dar autoridade de execução ao mesmo</p>
<p>## 
#!/bin/sh
python2 /home/endereço de onde esta o script deve estar completo começando a partir da home/script.sh</p>


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
   









