<?php 
$json = file_get_contents('source.json');
  
// Decode the JSON file
$json_data = json_decode($json);
$n=0;
$last_data = [];

foreach($json_data->data as $jd)
{
    foreach($jd as $j)
    {
        if(in_array($j->tanggal, $last_data)){
            continue;
        }
        array_push($last_data, $j->tanggal);
        $n++;
?>
<a href='https://bos.polri.go.id/laporan/dds-warga/pdf/<?=$j->id?>'><?=$n.'. '.$j->id?> | <?=$j->tanggal?><br>
        
<?php
    }
}
?>
