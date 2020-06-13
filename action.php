<?php

$COUNT=0;

$memes=array();
// if($_GET['a']!=NULL){$memes[$COUNT]=1; $COUNT+=1;}
// if($_GET['b']!=NULL){$memes[$COUNT]=2; $COUNT+=1;}
// if($_GET['c']!=NULL){$memes[$COUNT]=3; $COUNT+=1;}
// if($_GET['d']!=NULL){$memes[$COUNT]=4; $COUNT+=1;}
// if($_GET['e']!=NULL){$memes[$COUNT]=5; $COUNT+=1;}
// if($_GET['f']!=NULL){$memes[$COUNT]=6; $COUNT+=1;} 
// if($_GET['g']!=NULL){$memes[$COUNT]=7; $COUNT+=1;}
// if($_GET['h']!=NULL){$memes[$COUNT]=8; $COUNT+=1;}
// if($_GET['i']!=NULL){$memes[$COUNT]=9; $COUNT+=1;} 

if(isset($_GET['a'])){$memes[$COUNT]=1; $COUNT+=1;}
if(isset($_GET['b'])){$memes[$COUNT]=2; $COUNT+=1;}
if(isset($_GET['c'])){$memes[$COUNT]=3; $COUNT+=1;}
if(isset($_GET['d'])){$memes[$COUNT]=4; $COUNT+=1;}
if(isset($_GET['e'])){$memes[$COUNT]=5; $COUNT+=1;}
if(isset($_GET['f'])){$memes[$COUNT]=6; $COUNT+=1;}
if(isset($_GET['g'])){$memes[$COUNT]=7; $COUNT+=1;}
if(isset($_GET['h'])){$memes[$COUNT]=8; $COUNT+=1;}
if(isset($_GET['i'])){$memes[$COUNT]=9; $COUNT+=1;}


for ($x = 0; $x < $COUNT; $x+=1) {
    echo $memes[$x] . " ";
}
$command =exec("python test1.py .$memes");
// $command = escapeshellcmd('test1.py' $memes);
// $output = shell_exec($command);
echo $output;


?>