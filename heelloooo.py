Microsoft Windows [Versión 10.0.17134.48]
(c) 2018 Microsoft Corporation. Todos los derechos reservados.

C:\WINDOWS\system32>tracert daln@CPE64777d68ba83-CM64777d68ba80.cpe.net.cable.rogers.com
No se puede resolver el nombre del sistema de destino daln@CPE64777d68ba83-CM64777d68ba80.cpe.net.cab
le.rogers.com.

C:\WINDOWS\system32>tracert CPE64777d68ba83-CM64777d68ba80.cpe.net.cable.rogers.com

Traza a la dirección CPE64777d68ba83-CM64777d68ba80.cpe.net.cable.rogers.com [99.229.194.153]
sobre un máximo de 30 saltos:

  1    10 ms     4 ms     4 ms  192.168.1.254
  2   229 ms   197 ms   165 ms  ipdsl-bcs-lapazbcs-23-l0.uninet.net.mx [201.154.103.178]
  3   218 ms   207 ms   171 ms  bb-dallas-stemmons-7-be12.uninet.net.mx [201.125.20.110]
  4   384 ms   270 ms   431 ms  ae-39.a01.dllstx04.us.bb.gin.ntt.net [157.238.224.129]
  5   349 ms   342 ms   300 ms  ae-9.r10.dllstx09.us.bb.gin.ntt.net [129.250.4.177]
  6   253 ms   251 ms   238 ms  ae-2.r24.dllstx09.us.bb.gin.ntt.net [129.250.3.5]
  7   298 ms   289 ms   258 ms  ae-3.r20.chcgil09.us.bb.gin.ntt.net [129.250.4.153]
  8   298 ms   259 ms   456 ms  ae-12.r08.chcgil09.us.bb.gin.ntt.net [129.250.2.190]
  9   157 ms   181 ms   132 ms  ce-0-5-0-1.r08.chcgil09.us.ce.gin.ntt.net [128.241.3.190]
 10   142 ms   142 ms   159 ms  16-cgw01.ym.rmgt.net.rogers.com [209.148.230.133]
 11   418 ms   335 ms   325 ms  9403-cgw01.bloor.rmgt.net.rogers.com [209.148.235.229]
 12  1037 ms  2220 ms   796 ms  209.148.232.62
 13   257 ms   251 ms   243 ms  66.185.90.102
 14     *        *        *     Tiempo de espera agotado para esta solicitud.
 15     *        *        *     Tiempo de espera agotado para esta solicitud.
 16     *        *        *     Tiempo de espera agotado para esta solicitud.
 17     *        *        *     Tiempo de espera agotado para esta solicitud.
 18     *        *        *     Tiempo de espera agotado para esta solicitud.
 19     *        *        *     Tiempo de espera agotado para esta solicitud.
 20     *        *        *     Tiempo de espera agotado para esta solicitud.
 21     *        *        *     Tiempo de espera agotado para esta solicitud.
 22     *        *        *     Tiempo de espera agotado para esta solicitud.
 23     *        *        *     Tiempo de espera agotado para esta solicitud.
 24     *        *        *     Tiempo de espera agotado para esta solicitud.
 25     *        *        *     Tiempo de espera agotado para esta solicitud.
 26     *        *        *     Tiempo de espera agotado para esta solicitud.
 27     *        *        *     Tiempo de espera agotado para esta solicitud.
 28     *        *        *     Tiempo de espera agotado para esta solicitud.
 29     *        *        *     Tiempo de espera agotado para esta solicitud.
 30     *        *        *     Tiempo de espera agotado para esta solicitud.

Traza completa.

C:\WINDOWS\system32>tracert

Uso: tracert [-d] [-h saltos_máximos] [-j lista_de_hosts] [-w tiempo_de_espera]
             [-R] [-S srcaddr] [-4] [-6] nombre_destino

Opciones:
    -d                 No convierte direcciones en nombres de hosts.
    -h saltos_máximos  Máxima cantidad de saltos en la búsqueda del objetivo.
    -j lista-host      Enrutamiento relajado de origen a lo largo de la
                       lista de hosts (solo IPv4).
    -w tiempo_espera   Tiempo de espera en milisegundos para esperar cada
                       respuesta.
    -R                 Seguir la ruta de retorno (solo IPv6).
    -S srcaddr         Dirección de origen para utilizar (solo IPv6).
    -4                 Forzar usando IPv4.
    -6                 Forzar usando IPv6.



C:\WINDOWS\system32>tracert 62-210-129-144.rev.poneytelecom.eu
No se puede resolver el nombre del sistema de destino 62-210-129-144.rev.poneytelecom.eu.

C:\WINDOWS\system32>tracert 62-210-129-144.rev.poneytelecom.eu

Traza a la dirección 62-210-129-144.rev.poneytelecom.eu [62.210.129.144]
sobre un máximo de 30 saltos:

  1     4 ms     6 ms     4 ms  192.168.1.254
  2   189 ms   278 ms   514 ms  ipdsl-bcs-lapazbcs-23-l0.uninet.net.mx [201.154.103.178]
  3   489 ms   534 ms   591 ms  bb-dallas-stemmons-7-be12.uninet.net.mx [201.125.20.110]
  4   479 ms   549 ms   643 ms  66.110.57.154
  5   303 ms   296 ms   226 ms  206.82.142.46
  6     *        *      251 ms  4.69.140.34
  7     *        *        *     Tiempo de espera agotado para esta solicitud.
  8     *        *        *     Tiempo de espera agotado para esta solicitud.
  9   771 ms   864 ms   450 ms  62-210-129-144.rev.poneytelecom.eu [62.210.129.144]

Traza completa.

C:\WINDOWS\system32>tracert gateway/shell/matrix.org/x-ivjrqhyevirepahq
No se puede resolver el nombre del sistema de destino gateway/shell/matrix.org/x-ivjrqhyevirepahq.

C:\WINDOWS\system32>tracert gateway/shell/matrix.org
No se puede resolver el nombre del sistema de destino gateway/shell/matrix.org.

C:\WINDOWS\system32>tracert matrix.org

Traza a la dirección matrix.org [104.24.207.27]
sobre un máximo de 30 saltos:

  1     4 ms     5 ms     9 ms  192.168.1.254
  2   805 ms  1639 ms  1379 ms  ipdsl-bcs-lapazbcs-23-l0.uninet.net.mx [201.154.103.178]
  3   706 ms  1070 ms   790 ms  bb-dallas-stemmons-7-be12.uninet.net.mx [201.125.20.110]
  4   501 ms   307 ms  1327 ms  ext-189-247-253-109.uninet.net.mx [189.247.253.109]
  5   338 ms   875 ms   496 ms  104.24.207.27

Traza completa.

C:\WINDOWS\system32>tracert -j 62.210.129.144

Traza a la dirección 62-210-129-144.rev.poneytelecom.eu [62.210.129.144]
sobre un máximo de 30 saltos:

  1     *        *        *     Tiempo de espera agotado para esta solicitud.
  2     *        *        *     Tiempo de espera agotado para esta solicitud.
  3     *        *        *     Tiempo de espera agotado para esta solicitud.
  4     *        *        *     Tiempo de espera agotado para esta solicitud.
  5     *        *        *     Tiempo de espera agotado para esta solicitud.
  6     *        *        *     Tiempo de espera agotado para esta solicitud.
  7     *        *        *     Tiempo de espera agotado para esta solicitud.
  8     *        *        *     Tiempo de espera agotado para esta solicitud.
  9     *        *        *     Tiempo de espera agotado para esta solicitud.
 10     *        *        *     Tiempo de espera agotado para esta solicitud.
 11     *        *        *     Tiempo de espera agotado para esta solicitud.
 12     *        *        *     Tiempo de espera agotado para esta solicitud.
 13     *        *        *     Tiempo de espera agotado para esta solicitud.
 14     *        *        *     Tiempo de espera agotado para esta solicitud.
 15     *        *        *     Tiempo de espera agotado para esta solicitud.
 16     *        *        *     Tiempo de espera agotado para esta solicitud.
 17     *        *        *     Tiempo de espera agotado para esta solicitud.
 18     *        *        *     Tiempo de espera agotado para esta solicitud.
 19     *        *        *     Tiempo de espera agotado para esta solicitud.
 20     *        *        *     Tiempo de espera agotado para esta solicitud.
 21     *        *        *     Tiempo de espera agotado para esta solicitud.
 22     *        *        *     Tiempo de espera agotado para esta solicitud.
 23     *        *        *     Tiempo de espera agotado para esta solicitud.
 24     *        *        *     Tiempo de espera agotado para esta solicitud.
 25     *        *        *     Tiempo de espera agotado para esta solicitud.
 26     *        *        *     Tiempo de espera agotado para esta solicitud.
 27     *        *        *     Tiempo de espera agotado para esta solicitud.
 28     *        *        *     Tiempo de espera agotado para esta solicitud.
 29     *        *        *     Tiempo de espera agotado para esta solicitud.
 30     *        *        *     Tiempo de espera agotado para esta solicitud.

Traza completa.

C:\WINDOWS\system32>tracert nine_mill@c-76-23-234-152.hsd1.ct.comcast.net
No se puede resolver el nombre del sistema de destino nine_mill@c-76-23-234-152.hsd1.ct.comcast.net.

C:\WINDOWS\system32>tracert c-76-23-234-152.hsd1.ct.comcast.net

Traza a la dirección c-76-23-234-152.hsd1.ct.comcast.net [76.23.234.152]
sobre un máximo de 30 saltos:

  1     8 ms     2 ms     1 ms  192.168.1.254
  2   476 ms   706 ms   581 ms  ipdsl-bcs-lapazbcs-23-l0.uninet.net.mx [201.154.103.178]
  3   550 ms   606 ms   691 ms  bb-dallas-stemmons-7-be12.uninet.net.mx [201.125.20.110]
  4   780 ms   851 ms   599 ms  66.110.57.154
  5   509 ms   742 ms   589 ms  66.110.57.10
  6   340 ms   347 ms   299 ms  be-12495-cr02.dallas.tx.ibone.comcast.net [68.86.85.193]
  7   331 ms   341 ms   297 ms  be-12124-cr02.1601milehigh.co.ibone.comcast.net [68.86.84.229]
  8   341 ms   537 ms   429 ms  be-10521-cr02.350ecermak.il.ibone.comcast.net [68.86.85.169]
  9   379 ms   429 ms   400 ms  be-7922-ar01.woburn.ma.boston.comcast.net [68.86.91.6]
 10   777 ms     *        *     be-6-ar01.berlin.ct.hartford.comcast.net [68.87.182.82]
 11   425 ms   289 ms   284 ms  96.108.158.150
 12   530 ms   349 ms   380 ms  te-1-0-0-ten01.naugatuck.ct.hartford.comcast.net [68.86.237.122]
 13     *        *        *     Tiempo de espera agotado para esta solicitud.
 14     *        *        *     Tiempo de espera agotado para esta solicitud.
 15     *        *        *     Tiempo de espera agotado para esta solicitud.
 16     *        *        *     Tiempo de espera agotado para esta solicitud.
 17     *        *        *     Tiempo de espera agotado para esta solicitud.
 18     *        *        *     Tiempo de espera agotado para esta solicitud.
 19     *        *        *     Tiempo de espera agotado para esta solicitud.
 20     *        *        *     Tiempo de espera agotado para esta solicitud.
 21     *        *        *     Tiempo de espera agotado para esta solicitud.
 22     *        *        *     Tiempo de espera agotado para esta solicitud.
 23     *        *        *     Tiempo de espera agotado para esta solicitud.
 24     *        *        *     Tiempo de espera agotado para esta solicitud.
 25     *        *        *     Tiempo de espera agotado para esta solicitud.
 26     *        *        *     Tiempo de espera agotado para esta solicitud.
 27     *        *        *     Tiempo de espera agotado para esta solicitud.
 28     *        *        *     Tiempo de espera agotado para esta solicitud.
 29     *        *        *     Tiempo de espera agotado para esta solicitud.
 30     *        *        *     Tiempo de espera agotado para esta solicitud.

Traza completa.

C:\WINDOWS\system32>208.115.99.10
"208.115.99.10" no se reconoce como un comando interno o externo,
programa o archivo por lotes ejecutable.

C:\WINDOWS\system32>tracert 208.115.99.10

Traza a 208.115.99.10 sobre caminos de 30 saltos como máximo.

  1    14 ms     6 ms    15 ms  192.168.1.254
  2   300 ms   359 ms   637 ms  ipdsl-bcs-lapazbcs-23-l0.uninet.net.mx [201.154.103.178]
  3   251 ms   429 ms   450 ms  bb-dallas-stemmons-7-be12.uninet.net.mx [201.125.20.110]
  4   473 ms   282 ms   311 ms  66.110.57.154
  5   334 ms   375 ms   460 ms  66.110.56.5
  6   461 ms   167 ms    98 ms  66.110.56.82
  7   414 ms   368 ms   399 ms  las-b21-link.telia.net [62.115.123.137]
  8   431 ms   348 ms   293 ms  sjo-b21-link.telia.net [62.115.116.40]
  9   726 ms   455 ms   546 ms  sea-b2-link.telia.net [62.115.118.168]
 10   692 ms   402 ms   837 ms  serverhub-ic-333262-sea-b2.c.telia.net [62.115.161.3]
 11   315 ms   358 ms   377 ms  216.244.88.47
 12   366 ms   383 ms   334 ms  216.244.88.49
 13   524 ms   656 ms   928 ms  216.244.88.43
 14   358 ms   378 ms   577 ms  216.244.88.105
 15   380 ms   669 ms   376 ms  208.115.99.10

Traza completa.

C:\WINDOWS\system32>