# PkgsFedora27Offline

Title : packages fedora 27 offline installer 

Created by EBF LEARN | SOAK

Date : 30-12-2018

Pour installer les pakages fedora 27 offline utiliser le ficher install.py

<h2>Methode d'utilisation</h2>

ouvrir le terminal dans le dossier PkgsFedora27Offline <br />
su <br />
python install.py <br />

Et selectionnez le numero de package que vous souhaitez installer .

 <img src="https://f.top4top.net/p_11188xc7q1.png" alt="fedora27" > 

<h2>Pour installer d'autre packages</h2>

Pour installer d'autre packages utiliser cette commande : 
 
yum install --downloadonly --downloaddir=/home/path/path [package]

il permet de changer la direction d'installation pour les packages installer


Pour eviter les conflis entre les packages installer avec l'outils rpm 
utilser l'options --force 
